import matplotlib
matplotlib.use('Agg')
import ROOT
import os, sys, errno
import math
from array import array
import pandas
import numpy
import uproot
# from sklearn.model_selection import train_test_split
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
from keras_models import GetListOfModels
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
import matplotlib.pyplot as plt
ROOT.gStyle.SetOptStat(0)


class KerasTrainer(object):
    def __init__(self, framework, package):
        self.framework = framework
        self.package = package
        self.sum_weights = {}
        # self.category_wgts_dict = {}
        # self.category_wgts = []
        self.spect_labels = []
        self.mass_bin_labels = []
        self.category_labels = self.framework.signal_categories+self.framework.bkg_categories
        self.expected_counts = [1,1,1,1]
        self.expectedS = 1
        self.expectedB = 1
        self.signal_mask = [1,1,1,1]
        self.mass_histograms = []
        self.bkg_histogram = []
        self.mass_histograms_th1d = {}
        self.bkg_mask = []
        self.truth_labels = []
        self.color_pool = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kOrange, ROOT.kViolet, ROOT.kCyan]
        for category in self.category_labels:
            if category in self.framework.bkg_categories:
                self.bkg_mask.append(1)
            else:
                self.bkg_mask.append(0)
            self.mass_histograms_th1d[category] = ROOT.TH1D("input_"+category, "", 10, 110, 150)
    def __enter__(self):
        self.df = pandas.DataFrame()
        self.data = pandas.DataFrame()
        return self


    def __exit__(self, *args):
        del self.df 


    def convert_to_pandas(self):
        for file in self.framework.files + self.framework.data_files:
            with uproot.open(file.path) as f: 
                uproot_tree = f[self.framework.treePath]
                single_file_df = pandas.DataFrame()

                if file.isData:
                    label_list = self.framework.variable_list + self.framework.data_spectator_list
                else:
                    label_list = self.framework.variable_list + self.framework.spectator_list

                for var in label_list:
                    # print "Adding variable:", var.name
                    if  "met.pt" in var.name:   # quick fix for met
                        up_var =  uproot_tree["met"]["pt"].array()
                    else:
                        up_var = uproot_tree[var.name].array()
                    if var.isMultiDim:
                        
                        # splitting the multidimensional input variables so each column corresponds to a one-dimensional variable
                        # Only <itemsAdded> objects are kept
        
                        single_var_df = pandas.DataFrame(data = up_var.tolist())
                        single_var_df.drop(single_var_df.columns[var.itemsAdded:],axis=1,inplace=True)
                        single_var_df.columns = [var.name+"[%i]"%i for i in range(var.itemsAdded)]
                        if var in self.framework.spectator_list:
                            self.spect_labels.extend(single_var_df.columns)
                        single_file_df = pandas.concat([single_file_df, single_var_df], axis=1)
                        single_file_df.fillna(var.replacement, axis=0, inplace=True) # if there are not enough jets
                        # print "Entries in file: ", single_file_df.count()+1
        
                    else:
                        single_file_df[var.name] = up_var
                        if var in self.framework.spectator_list:
                            self.spect_labels.append(var.name)

                for category in self.category_labels:  
                    single_file_df[category] = 0

                if file.isData:
                    single_file_df['weight'] = 1
                    single_file_df['weight_over_lumi'] = 1
                    self.data = pandas.concat([self.data, single_file_df]) 

                else:
                    if "2016" in self.framework.year:
                        SF = (0.5*(single_file_df['IsoMu_SF_3'] + single_file_df['IsoMu_SF_4'])*0.5*(single_file_df['MuID_SF_3'] + single_file_df['MuID_SF_4'])*0.5*(single_file_df['MuIso_SF_3'] + single_file_df['MuIso_SF_4']))
                        mc_weight = SF * single_file_df['GEN_wgt'] * single_file_df['PU_wgt']
                        single_file_df['weight'] = file.weight * mc_weight
                    elif "2017" in self.framework.year:
                        SF = single_file_df['IsoMu_SF_3'] * single_file_df['MuID_SF_3'] * single_file_df['MuIso_SF_3']
                        mc_weight = SF * single_file_df['GEN_wgt'] * single_file_df['PU_wgt']
                        single_file_df['weight'] = file.weight * mc_weight
                    elif "ucsd" in self.framework.year:
                        mc_weight = single_file_df['weight']
                    elif "latinos" in self.framework.year:
                        mc_weight = single_file_df['XSWeight']*single_file_df['SFweight']*single_file_df['GenLepMatch']*single_file_df['METFilter_MC']
                    else:
                        mc_weight = single_file_df['GEN_wgt'] * single_file_df['PU_wgt']
                        single_file_df['weight'] = file.weight * mc_weight
    
                    single_file_df[file.category] = 1
                    single_file_df['weight_over_lumi'] = file.weight_over_lumi * mc_weight
                    print "Added %s with %i events"%(file.name, single_file_df.shape[0])
                    single_file_df = self.apply_cuts(single_file_df, self.framework.year)
                    for i in range(file.repeat):
                        self.df = pandas.concat([self.df,single_file_df])
        
        # for category in self.category_labels:
        #     self.category_wgts.append(self.category_wgts_dict[category]) # want to preserve order

        self.labels = list(self.df.drop(['weight', 'weight_over_lumi']+self.spect_labels+self.category_labels, axis=1))
        self.df.reset_index(inplace=True, drop=True)

        # if self.framework.multiclass:
        #     for lbl in self.category_labels:
        #         self.expected_counts.append(self.df.loc[self.df[lbl]>0,['weight']].sum())
        #         print "Expected %s = %f"%(lbl, self.df.loc[self.df[lbl]>0,['weight']].sum())
        #         if lbl in self.framework.signal_categories:
        #             self.signal_mask.append(1)
        #         else:
        #             self.signal_mask.append(0)
        # else:
        #     self.expectedS = self.df.loc[self.df['signal']>0,['weight']].sum()
        #     self.expectedB = self.df.loc[self.df['background']>0,['weight']].sum()
        #     print "Expected signal = ", self.expectedS
        #     print "Expected background = ", self.expectedB

        # print self.df["muPairs.mass_Roch[0]"]
        # self.df = self.apply_cuts(self.df, self.framework.year)
        # print self.df["muPairs.mass_Roch[0]"]

        if self.framework.custom_loss:
            self.df = self.make_mass_bins(self.df, 10, 110, 150)

        if self.framework.data_files:
            self.data.reset_index(inplace=True, drop=True)
            self.data = self.apply_cuts(self.data, self.framework.year)
            if self.framework.custom_loss:
                self.data = self.make_mass_bins(self.data, 10, 110, 150, isMC=False)

        self.truth_labels.extend(self.category_labels)
        self.df = shuffle(self.df)

        if self.framework.data_files:
           self.data = self.add_columns(self.data)
        
        self.df = self.add_columns(self.df)

        self.df_train, self.df_test = train_test_split(self.df,test_size=0.2, random_state=7)
    

    def train_models(self):
        self.df_train_scaled, self.df_test_scaled, self.data_scaled = self.scale(self.df_train, self.df_test, self.data, self.labels)

        training_data = self.apply_training_cuts(self.df_train_scaled)

        if self.framework.multiclass:
            self.expected_counts = []
            self.signal_mask = []
            for lbl in self.category_labels:
                self.expected_counts.append(training_data.loc[training_data[lbl]>0,['weight']].sum())
                print "Expected %s = %f"%(lbl, training_data.loc[training_data[lbl]>0,['weight']].sum())
                if lbl in self.framework.signal_categories:
                    self.signal_mask.append(1)
                    print lbl+" is signal"
                else:
                    self.signal_mask.append(0)
                    print lbl+" is background"
        else:
            self.expectedS = training_data.loc[training_data['signal']>0,['weight']].sum()
            self.expectedB = training_data.loc[training_data['background']>0,['weight']].sum()
            print "Expected signal = ", self.expectedS
            print "Expected background = ", self.expectedB

        self.list_of_models = GetListOfModels(self)
        for obj in self.list_of_models:
            if obj.name not in self.framework.method_list:
                continue

            try:
                os.makedirs(self.package.mainDir+'/'+obj.name+'/')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

            try:
                os.makedirs(self.package.mainDir+'/'+obj.name+'/png/')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

            try:
                os.makedirs(self.package.mainDir+'/'+obj.name+'/root/')
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise


            obj.CompileModel(self.package.dirs['modelDir'])
            # early_stopping = EarlyStopping(monitor='val_loss', patience=10)
            # tensorboard = TensorBoard(log_dir=self.package.dirs['logDir']+obj.name)
            # model_checkpoint = ModelCheckpoint(self.package.dirs['modelDir']+obj.name+'_trained_lwstValLoss.h5', monitor='val_loss', 
   #                                       verbose=0, save_best_only=True, 
   #                                       save_weights_only=False, mode='auto', 
   #                                       period=1)


            if 'resweights' in obj.name:
                self.train_labels = self.truth_labels
                for category in self.category_labels:
                    training_data[category] = training_data[category]*training_data['hmerr']
                # print self.labels
            elif 'multi' in obj.name:
                self.train_labels = self.truth_labels                
            elif 'sigloss' in obj.name:
                self.train_labels = 'signal'
            else:
                self.train_labels = self.truth_labels

            history = obj.model.fit(            
                                    training_data[self.labels].values,
                                    training_data[self.train_labels].values,
                                    # training_data[self.truth_labels].values,
                                    epochs=obj.epochs, 
                                    batch_size=obj.batchSize, 
                                    verbose=1,
                                    # callbacks=[
                                        # early_stopping, 
                                        # model_checkpoint,
                                        # tensorboard
                                        # ], 
                                    validation_split=0.25,
                                    #steps_per_epoch = None,
                                    shuffle=True)
    
            obj.model.save(self.package.dirs['modelDir']+obj.name+'_trained.h5')

            if "sigloss" in obj.name:
                train_prediction = pandas.DataFrame(data=obj.model.predict(self.df_train_scaled[self.labels].values), columns=['pred_sig_%s'%obj.name], index=self.df_train_scaled.index)
                test_prediction = pandas.DataFrame(data=obj.model.predict(self.df_test_scaled[self.labels].values), columns=['pred_sig_%s'%obj.name], index=self.df_test_scaled.index)
                if self.framework.data_files:
                    data_prediction = pandas.DataFrame(data=obj.model.predict(self.data_scaled[self.labels].values), columns=['pred_sig_%s'%obj.name], index=self.data_scaled.index)
            else:
                train_prediction = pandas.DataFrame(data=obj.model.predict(self.df_train_scaled[self.labels].values), columns=["pred_%s_%s"%(n,obj.name) for n in self.train_labels], index=self.df_train_scaled.index)
                test_prediction = pandas.DataFrame(data=obj.model.predict(self.df_test_scaled[self.labels].values), columns=["pred_%s_%s"%(n,obj.name) for n in self.train_labels], index=self.df_test_scaled.index)
                if self.framework.data_files:
                    data_prediction = pandas.DataFrame(data=obj.model.predict(self.data_scaled[self.labels].values), columns=["pred_%s_%s"%(n,obj.name) for n in self.train_labels], index=self.data_scaled.index)

            self.df_train_scaled = pandas.concat([self.df_train_scaled, train_prediction], axis=1)
            self.df_test_scaled = pandas.concat([self.df_test_scaled, test_prediction], axis=1)
            if self.framework.data_files:
                self.data_scaled = pandas.concat([self.data_scaled, data_prediction], axis=1)


            self.fill_out_root_files("test", self.df_test_scaled, obj.name, self.category_labels, False)
            self.fill_out_root_files("train", self.df_train_scaled, obj.name, self.category_labels, False)
            if self.framework.data_files:
                self.fill_out_root_files("Data", self.data_scaled, obj.name, ["Data"], True)

            self.plot_history(history.history, obj.name)


    def scale(self, train, test, data, labels):
        df_train = train.loc[:,labels]
        df_test = test.loc[:,labels]
        if self.framework.data_files:
            df_data = data.loc[:, labels]
        scaler = StandardScaler().fit(df_train.values)
        df_train = scaler.transform(df_train.values)
        df_test = scaler.transform(df_test.values)
        if self.framework.data_files:
            df_data = scaler.transform(df_data.values)  
        train[labels] = df_train
        test[labels] = df_test
        if self.framework.data_files:
            data[labels] = df_data
        return train, test, data

    def fill_out_root_files(self, output_name, df, method_name, category_list, isData):

        trees               = {}
        mass                = {}
        max_abs_eta_mu      = {}
        min_abs_eta_mu      = {}
        mu1_eta             = {}
        mu2_eta             = {}
        dimu_eta            = {}
        weight              = {}
        weight_over_lumi    = {}
        DY_prediction       = {}
        ttbar_prediction    = {}
        ggH_prediction      = {}
        VBF_prediction      = {}
        sig_prediction      = {}
        bkg_prediction      = {}
        nJets               = {}

        for category in category_list:
            mass[category]= array('f', [0])
            max_abs_eta_mu[category]= array('f', [0])
            min_abs_eta_mu[category]= array('f', [0])
            mu1_eta[category] = array('f', [0])
            mu2_eta[category] = array('f', [0])
            dimu_eta[category] = array('f', [0])
            weight[category]= array('f', [0])
            weight_over_lumi[category]= array('f', [0])
            DY_prediction[category]= array('f', [0])
            ttbar_prediction[category]= array('f', [0])
            ggH_prediction[category]= array('f', [0])
            VBF_prediction[category]= array('f', [0])
            sig_prediction[category]= array('f', [0])
            bkg_prediction[category]= array('f', [0])
            nJets[category]=array('i', [0])
            trees[category] = ROOT.TTree("tree_%s"%category,"tree_%s"%category)
            if "ucsd" in self.framework.year:
                trees[category].Branch("mass",               mass[category]            , "mass/F")
                trees[category].Branch("weight",             weight[category]          , "weight/F")
            elif "sigloss" in self.framework.year:
                trees[category].Branch("mass",               mass[category]            , "mass/F")
                trees[category].Branch("weight",             weight[category]          , "weight/F")
            elif "latinos" in self.framework.year:
                trees[category].Branch("mass",               mass[category]            , "mass/F")
                trees[category].Branch("weight",             weight[category]          , "weight/F")
            else:                
                trees[category].Branch("mass",               mass[category]            , "mass/F")
                trees[category].Branch("max_abs_eta_mu",     max_abs_eta_mu[category]  , "max_abs_eta_mu/F")
                trees[category].Branch("min_abs_eta_mu",     min_abs_eta_mu[category]  , "min_abs_eta_mu/F")
                trees[category].Branch("weight",             weight[category]          , "weight/F")
                trees[category].Branch("nJets",     nJets[category]  , "nJets/F")
                trees[category].Branch("mu1_eta",     mu1_eta[category]  , "mu1_eta/F")
                trees[category].Branch("mu2_eta",     mu2_eta[category]  , "mu2_eta/F")
                trees[category].Branch("dimu_eta",     dimu_eta[category]  , "dimu_eta/F")
            if self.framework.multiclass and not ("sigloss" in self.framework.year):
                trees[category].Branch("DY_prediction",      DY_prediction[category]   , "DY_prediction/F")
                trees[category].Branch("ttbar_prediction",   ttbar_prediction[category], "ttbar_prediction/F")
                trees[category].Branch("ggH_prediction",     ggH_prediction[category]  , "ggH_prediction/F")
                trees[category].Branch("VBF_prediction",     VBF_prediction[category]  , "VBF_prediction/F")
            else:
                trees[category].Branch("sig_prediction",      sig_prediction[category]   , "sig_prediction/F")
                trees[category].Branch("bkg_prediction",      bkg_prediction[category],    "bkg_prediction/F")

            trees[category].Branch("weight_over_lumi",             weight_over_lumi[category]          , "weight_over_lumi/F")

        new_file = ROOT.TFile(self.package.mainDir+'/'+method_name+"/root/output_"+output_name+".root","recreate")
        new_file.cd()

        for index, row in df.iterrows():
            if isData:
                mass["Data"][0]             = row["muPairs.mass_Roch[0]"]
                max_abs_eta_mu["Data"][0]   = row["max_abs_eta_mu"]
                min_abs_eta_mu["Data"][0]   = row["min_abs_eta_mu"]
                weight["Data"][0]           = 1
                weight_over_lumi["Data"][0] = 1
                if self.framework.multiclass:
                    DY_prediction["Data"][0]    = row["pred_%s_%s"%(self.framework.dy_label, method_name)]
                    ttbar_prediction["Data"][0] = row["pred_%s_%s"%(self.framework.top_label, method_name)]
                    ggH_prediction["Data"][0]   = row["pred_%s_%s"%(self.framework.ggh_label, method_name)] 
                    VBF_prediction["Data"][0]   = row["pred_%s_%s"%(self.framework.vbf_label, method_name)] 
                else:
                    sig_prediction["Data"][0]   = row["pred_%s_%s"%(self.framework.sig_label, method_name)]
                    # bkg_prediction["Data"][0]   = row["pred_%s_%s"%(self.framework.bkg_label, method_name)]
                nJets["Data"][0]            = row["nJets"] 
                mu1_eta["Data"][0]          = row["muons.eta[0]"]
                mu2_eta["Data"][0]          = row["muons.eta[1]"]
                dimu_eta["Data"][0]         = row["muPairs.eta[0]"]
                trees["Data"].Fill() 
            else:
                for category in category_list:
                    if row[category]==1:
                        if "ucsd" in self.framework.year:
                            mass[category][0]             = row["hmass"]
                            weight[category][0]           = row["weight"]
                            weight_over_lumi[category][0] = row["weight_over_lumi"]
                        elif "sigloss" in self.framework.year:
                            mass[category][0]             = row["hmass"]
                            weight[category][0]           = row["weight"]
                            weight_over_lumi[category][0] = row["weight_over_lumi"]
                        elif "latinos" in self.framework.year:
                            mass[category][0]             = row["mll"]
                            weight[category][0]           = row["weight"]
                            weight_over_lumi[category][0] = row["weight_over_lumi"]                            
                        else:
                            mass[category][0]             = row["muPairs.mass_Roch[0]"]
                            max_abs_eta_mu[category][0]   = row["max_abs_eta_mu"]
                            min_abs_eta_mu[category][0]   = row["min_abs_eta_mu"]
                            weight[category][0]           = row["weight"]
                            weight_over_lumi[category][0] = row["weight_over_lumi"]
                            nJets[category][0]            = row["nJets"]
                            mu1_eta[category][0]          = row["muons.eta[0]"]
                            mu2_eta[category][0]          = row["muons.eta[1]"]
                            dimu_eta[category][0]         = row["muPairs.eta[0]"]

                        if self.framework.multiclass and not ("sigloss" in self.framework.year):
                            DY_prediction[category][0]    = row["pred_%s_%s"%(self.framework.dy_label, method_name)]
                            ttbar_prediction[category][0] = row["pred_%s_%s"%(self.framework.top_label, method_name)]
                            ggH_prediction[category][0]   = row["pred_%s_%s"%(self.framework.ggh_label, method_name)] 
                            VBF_prediction[category][0]   = row["pred_%s_%s"%(self.framework.vbf_label, method_name)] 
                        else:
                            sig_prediction[category][0]   = row["pred_%s_%s"%(self.framework.sig_label, method_name)]
                            # bkg_prediction[category][0]   = row["pred_%s_%s"%(self.framework.bkg_label, method_name)]  
                        trees[category].Fill() 

        for category in category_list:
            trees[category].Write()
        new_file.Close()                    


    def plot_history(self, history, method_name):
        plt.plot(history['acc'])
        plt.plot(history['val_acc'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.savefig(self.package.mainDir+'/'+method_name+'/png/'+"acc.png")
        plt.clf()
        print "Accuracy plot saved as "+self.package.mainDir+'/'+method_name+'/png/'+"acc.png"
        plt.plot(history['loss'])
        plt.plot(history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.savefig(self.package.mainDir+'/'+method_name+'/png/'+"loss.png")
        print "Loss plot saved as "+self.package.mainDir+'/'+method_name+'/png/'+"loss.png" 
        plt.clf()   

        
    def add_columns(self, df):
        if "latinos" in self.framework.year:
            pass
        elif "ucsd" in self.framework.year:
            pass
        else:
            df["abs_eta_1"] = df["muons.eta[0]"].abs()
            df["abs_eta_2"] = df["muons.eta[1]"].abs()
            df["max_abs_eta_mu"] = df[["abs_eta_1", "abs_eta_2"]].max(axis=1)
            df["min_abs_eta_mu"] = df[["abs_eta_1", "abs_eta_2"]].min(axis=1)
        return df

    def apply_cuts(self, df, year):
        if "ucsd_inclusive" in year:
            mass = df["hmass"]
            flag = (mass>110)&(mass<150)
            return df.loc[flag]
        if "ucsd_01jet" in year:
            mass = df["hmass"]
            njets = df["njets"]
            flag = (mass>110)&(mass<150)&(njets<2)
            return df.loc[flag]
        if "ucsd_2jet_bveto" in year:
            mass = df["hmass"]
            njets = df["njets"]
            nbjets = df["nbjets"]
            flag = (mass>110)&(mass<150)&(njets>=2)&(nbjets==0)
            return df.loc[flag]

        if "latinos" in year:
            mass = df["mll"]
            njets = df["nJet"]
            # nbjets = df["nbjets"]
            flag = (mass>110)&(mass<150)
            return df.loc[flag]            

        muon1_pt    = df['muons.pt[0]']
        muon2_pt    = df['muons.pt[1]']
        muon1_ID    = df['muons.isMediumID[0]']
        muon2_ID    = df['muons.isMediumID[1]']
        muPair_mass = df['muPairs.mass_Roch[0]']
        nJets       = df['nJets']

        if year is "2016":
            flag =  ((muPair_mass>110)&
                (muPair_mass<150)&
                (muon1_ID>0)&
                (muon2_ID>0)&
                (muon1_pt>26)&
                (muon2_pt>20))    

        elif year is "2017":
            flag =  ((muPair_mass>110)&
                (muPair_mass<150)&
                (muon1_ID>0)&
                (muon2_ID>0)&
                (muon1_pt>30)&
                (muon2_pt>20))

        return df.loc[flag]

    def apply_training_cuts(self, df):
        if "ucsd" in self.framework.year:
            muPair_mass = df['hmass']
        elif "latinos" in self.framework.year:
            muPair_mass = df['mll']
        else:  
            muPair_mass = df['muPairs.mass_Roch[0]']
        flag =  ((muPair_mass>self.framework.massWindow[0])&
                (muPair_mass<self.framework.massWindow[1]))
        return df.loc[flag]

    def make_mass_bins(self, df, nbins, min, max, isMC=True):

        if "muPairs.mass_Roch[0]" not in df.columns:
            print "Add muPairs.mass_Roch[0] to spectators!"
            return

        bin_width = float((max-min)/nbins)

        if isMC:

            for i in range(nbins):
                df["mass_bin_%i"%i] = 0
                df.loc[(df["muPairs.mass_Roch[0]"]>min+i*bin_width) & (df["muPairs.mass_Roch[0]"]<min+(i+1)*bin_width), "mass_bin_%i"%i] = 1
                self.mass_bin_labels.append("mass_bin_%i"%i)
                self.bkg_histogram.append(0)
    
            self.truth_labels.extend(self.mass_bin_labels)
    
            self.bkg_histogram = df.loc[df[self.framework.bkg_categories].sum(axis=1)>0,self.mass_bin_labels].multiply(df["weight"], axis="index").sum(axis=0).values.tolist()
            self.bkg_histogram = [x/sum(self.bkg_histogram) for x in self.bkg_histogram]
    
            for category in self.category_labels:
    
                mass_hist = df.loc[(df[category]>0),self.mass_bin_labels].sum(axis=0)
                mass_hist = mass_hist / mass_hist.sum()
                self.mass_histograms.append(mass_hist.values.tolist())  
                for i in range(nbins):
                    self.mass_histograms_th1d[category].SetBinContent(i+1, mass_hist.values.tolist()[i])

        else:
            for i in range(nbins):
                df["mass_bin_%i"%i] = 0
                df.loc[(df["muPairs.mass_Roch[0]"]>min+i*bin_width) & (df["muPairs.mass_Roch[0]"]<min+(i+1)*bin_width), "mass_bin_%i"%i] = 1
        return df