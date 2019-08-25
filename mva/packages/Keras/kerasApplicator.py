import matplotlib
matplotlib.use('Agg')
import ROOT
import os, sys, errno
import math
import glob
from array import array
import pandas
import numpy
import uproot
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
from keras.models import load_model
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
import matplotlib.pyplot as plt
ROOT.gStyle.SetOptStat(0)


class KerasApplicator(object):
    def __init__(self, framework, package):
        self.framework = framework
        self.package = package
        self.sum_weights = {}
        self.spect_labels = []
        self.mass_bin_labels = []
        self.category_labels = self.framework.signal_categories+self.framework.bkg_categories
        self.truth_labels = []
    def __enter__(self):
        self.df = pandas.DataFrame()
        self.data = pandas.DataFrame()
        return self

    def __exit__(self, *args):
        del self.df 


    def convert_to_pandas(self):
        for files in self.framework.files + self.framework.data_files:
            for file in glob.glob(files.path):
                with uproot.open(file) as f: 
                    uproot_tree = f[self.framework.treePath]
                    single_file_df = pandas.DataFrame()
                    label_list = self.framework.variable_list

                    for var in label_list:
                        # print "Adding variable:", var.name
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
                        else:
                            single_file_df[var.name] = up_var
                            if var in self.framework.spectator_list:
                                self.spect_labels.append(var.name)

                        self.df = pandas.concat([self.df,single_file_df])
        
        return self.df    

    def apply_models(self):
        # dnn_vars = dnn_variables(m1,m2,j1,j2,nsoft,j1_qgl,j2_qgl)
        # varlist_order = ['softJet5', 'dRmm','dEtamm','M_jj','pt_jj','eta_jj','phi_jj','M_mmjj','eta_mmjj','phi_mmjj','dEta_jj','Zep','dRmin_mj', 'dRmax_mj'
        #                    ,'dRmin_mmj','dRmax_mmj','dPhimm','leadingJet_pt','subleadingJet_pt',
        #                        'leadingJet_eta','subleadingJet_eta','leadingJet_qgl','subleadingJet_qgl','cthetaCS','Higgs_pt','Higgs_eta','Higgs_mass']
        # dnn_vars_arr = numpy.vstack([dnn_vars[k] for k in varlist_order]).T
        dnn_vars_df = self.df.values
        model_STDwt = numpy.load(self.framework.standartization_path)
        dnn_mean = model_STDwt[0,:]
        dnn_std = model_STDwt[1,:]

        dnn_vars_df-=dnn_mean
        dnn_vars_df/=dnn_std

        m_caltech = load_model(self.framework.trained_model_path)
        caltech_dnn_score=m_caltech.predict(dnn_vars_df)
        print caltech_dnn_score
        return caltech_dnn_score



