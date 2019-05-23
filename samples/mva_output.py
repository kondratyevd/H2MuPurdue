import ROOT

class MVASource(object):
    def __init__(self, name, title, path):
        self.name = name
        self.title = title 
        self.path = path
        self.samples = []
        self.data_hist = None
        self.signal_hists = []
        self.mc_stack = ROOT.THStack()
        self.lumi = 0

    class Sample(object):
        def __init__(self, name, title, filename, treename, isData, isStacked, color, isWeightOverLumi=True, additional_cut="1"):
            # self.source = source
            self.name = name
            self.title = title
            self.filename = filename
            self.treename = treename
            self.isData = isData
            self.isStacked = isStacked
            self.color = color          
            self.isWeightOverLumi = isWeightOverLumi
            self.additional_cut = additional_cut



dnn_local = MVASource("DNN_local", "DNN_local", "/Users/dmitrykondratyev/ML_output/Run_2019-04-08_11-37-05/Keras_multi/model_50_D2_25_D2_25_D2/root/")
dnn_local.Sample("tt", "ttbar", "output_t*root", "tree_tt_ll_POW", False, True, ROOT.kYellow, True)
dnn_local.Sample("dy", "Drell-Yan", "output_t*root", "tree_ZJets_aMC", False, True, ROOT.kOrange-3, True)
dnn_local.Sample("ggh", "ggH", "output_t*root", "tree_H2Mu_gg", False, False, ROOT.kRed, True)
dnn_local.Sample("vbf", "VBF", "output_t*root", "tree_H2Mu_VBF", False, False, ROOT.kViolet-1, True)
dnn_local.Sample("data", "Data 2017 (40.5/fb)", "output_Data.root", "tree_Data", True, False, ROOT.kBlack)
dnn_local.lumi=40490.712


# Option 6
dnn_multi = MVASource("DNN_Multi", "DNN_Multi", "/scratch/gilbreth/dkondra/ML_output/Run_2019-04-08_11-37-05//Keras_multi/model_50_D2_25_D2_25_D2/root/")
dnn_multi.Sample("tt", "ttbar", "output_t*root", "tree_tt_ll_POW", False, True, ROOT.kYellow, True)
dnn_multi.Sample("dy", "Drell-Yan", "output_t*root", "tree_ZJets_aMC", False, True, ROOT.kOrange-3, True)
dnn_multi.Sample("ggh", "ggH", "output_t*root", "tree_H2Mu_gg", False, False, ROOT.kRed, True)
dnn_multi.Sample("vbf", "VBF", "output_t*root", "tree_H2Mu_VBF", False, False, ROOT.kViolet-1, True)
dnn_multi.Sample("data", "Data 2017 (40.5/fb)", "output_Data.root", "tree_Data", True, False, ROOT.kBlack)
dnn_multi.lumi=40490.712



# Option 7
dnn_multi_hiStat = MVASource("DNN_Multi_hiStat", "DNN_Multi_hiStat", "/scratch/gilbreth/dkondra/ML_output/Run_2019-04-08_11-51-21//Keras_multi/model_50_D2_25_D2_25_D2/root/")
dnn_multi_hiStat.Sample("tt", "ttbar", "output_t*root", "tree_tt_ll_POW", False, True, ROOT.kYellow, True)
dnn_multi_hiStat.Sample("dy", "Drell-Yan", "output_t*root", "tree_ZJets_aMC", False, True, ROOT.kOrange-3, True)
dnn_multi_hiStat.Sample("ggh", "ggH", "output_t*root", "tree_H2Mu_gg", False, False, ROOT.kRed, True)
dnn_multi_hiStat.Sample("vbf", "VBF", "output_t*root", "tree_H2Mu_VBF", False, False, ROOT.kViolet-1, True)
dnn_multi_hiStat.Sample("data", "Data 2017 (40.5/fb)", "output_Data.root", "tree_Data", True, False, ROOT.kBlack)
dnn_multi_hiStat.lumi=40490.712


# Option 8
dnn_multi_hiStat_ebe = MVASource("DNN_Multi_hiStat_ebe", "DNN_Multi_hiStat_ebe", "/scratch/gilbreth/dkondra/ML_output/Run_2019-04-08_11-37-09//Keras_multi/model_50_D2_25_D2_25_D2/root/")
dnn_multi_hiStat_ebe.Sample("tt", "ttbar", "output_t*root", "tree_tt_ll_POW", False, True, ROOT.kYellow, True)
dnn_multi_hiStat_ebe.Sample("dy", "Drell-Yan", "output_t*root", "tree_ZJets_aMC", False, True, ROOT.kOrange-3, True)
dnn_multi_hiStat_ebe.Sample("ggh", "ggH", "output_t*root", "tree_H2Mu_gg", False, False, ROOT.kRed, True)
dnn_multi_hiStat_ebe.Sample("vbf", "VBF", "output_t*root", "tree_H2Mu_VBF", False, False, ROOT.kViolet-1, True)
dnn_multi_hiStat_ebe.Sample("data", "Data 2017 (40.5/fb)", "output_Data.root", "tree_Data", True, False, ROOT.kBlack)
dnn_multi_hiStat_ebe.lumi=40490.712

# Option 9
dnn_binary_hiStat = MVASource("DNN_Binary_hiStat", "DNN_Binary_hiStat", "/scratch/gilbreth/dkondra/ML_output/Run_2019-04-08_11-37-12//Keras_multi/model_50_D2_25_D2_25_D2/root/")
dnn_binary_hiStat.Sample("bkg", "bkg", "output_t*root", "tree_bkg", False, True, ROOT.kYellow, True)
dnn_binary_hiStat.Sample("sig", "sig", "output_t*root", "tree_sig", False, False, ROOT.kRed, True)
dnn_binary_hiStat.Sample("data", "Data 2017 (40.5/fb)", "output_Data.root", "tree_Data", True, False, ROOT.kBlack)
dnn_binary_hiStat.lumi=40490.712


# Option 10
dnn_binary_hiStat_ebe = MVASource("DNN_Binary_hiStat_ebe", "DNN_Binary_hiStat_ebe", "/scratch/gilbreth/dkondra/ML_output/Run_2019-04-08_11-37-16//Keras_multi/model_50_D2_25_D2_25_D2/root/")
dnn_binary_hiStat_ebe.Sample("bkg", "bkg", "output_t*root", "tree_bkg", False, True, ROOT.kYellow, True)
dnn_binary_hiStat_ebe.Sample("sig", "sig", "output_t*root", "tree_sig", False, False, ROOT.kRed, True)
dnn_binary_hiStat_ebe.Sample("data", "Data 2017 (40.5/fb)", "output_Data.root", "tree_Data", True, False, ROOT.kBlack)
dnn_binary_hiStat_ebe.lumi=40490.712


# Option 11
dnn_binary = MVASource("DNN_Binary", "DNN_Binary", "/scratch/gilbreth/dkondra/ML_output/Run_2019-04-09_16-22-10//Keras_multi/model_50_D2_25_D2_25_D2/root/")
dnn_binary.Sample("bkg", "bkg", "output_t*root", "tree_bkg", False, True, ROOT.kYellow, True)
dnn_binary.Sample("sig", "sig", "output_t*root", "tree_sig", False, False, ROOT.kRed, True)
dnn_binary.Sample("data", "Data 2017 (40.5/fb)", "output_Data.root", "tree_Data", True, False, ROOT.kBlack)
dnn_binary.lumi=40490.712


# Option 12
dnn_multi_hiStat_m120To130 = MVASource("DNN_Multi_hiStat_m120To130", "DNN_Multi_hiStat_m120To130", "/scratch/gilbreth/dkondra/ML_output/Run_2019-04-11_14-31-12//Keras_multi/model_50_D2_25_D2_25_D2/root/")
dnn_multi_hiStat_m120To130.Sample("tt", "ttbar", "output_t*root", "tree_tt_ll_POW", False, True, ROOT.kYellow, True)
dnn_multi_hiStat_m120To130.Sample("dy", "Drell-Yan", "output_t*root", "tree_ZJets_aMC", False, True, ROOT.kOrange-3, True)
dnn_multi_hiStat_m120To130.Sample("ggh", "ggH", "output_t*root", "tree_H2Mu_gg", False, False, ROOT.kRed, True)
dnn_multi_hiStat_m120To130.Sample("vbf", "VBF", "output_t*root", "tree_H2Mu_VBF", False, False, ROOT.kViolet-1, True)
dnn_multi_hiStat_m120To130.Sample("data", "Data 2017 (40.5/fb)", "output_Data.root", "tree_Data", True, False, ROOT.kBlack)
dnn_multi_hiStat_m120To130.lumi=40490.712


# Option 13
dnn_multi_hiStat_m120To130_repeated = MVASource("DNN_Multi_hiStat_m120To130_repeated", "DNN_Multi_hiStat_m120To130_repeated", "/scratch/gilbreth/dkondra/ML_output/Run_2019-04-15_18-13-46//Keras_multi/model_50_D2_25_D2_25_D2/root/")
dnn_multi_hiStat_m120To130_repeated.Sample("tt", "ttbar", "output_t*root", "tree_tt_ll_POW", False, True, ROOT.kYellow, True, "1./15.")
dnn_multi_hiStat_m120To130_repeated.Sample("dy", "Drell-Yan", "output_t*root", "tree_ZJets_aMC", False, True, ROOT.kOrange-3, True)
dnn_multi_hiStat_m120To130_repeated.Sample("ggh", "ggH", "output_t*root", "tree_H2Mu_gg", False, False, ROOT.kRed, True, "1./4.")
dnn_multi_hiStat_m120To130_repeated.Sample("vbf", "VBF", "output_t*root", "tree_H2Mu_VBF", False, False, ROOT.kViolet-1, True, "1./6.")
dnn_multi_hiStat_m120To130_repeated.Sample("data", "Data 2017 (40.5/fb)", "output_Data.root", "tree_Data", True, False, ROOT.kBlack)
dnn_multi_hiStat_m120To130_repeated.lumi=40490.712


