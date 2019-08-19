
class SmpNtuple(object):
    def __init__(self, name, title, path, isData, isDir, xSec, lumi):
        self.name = name
        self.title = title
        self.path = path
        self.isData = isData
        self.xSec = xSec
        self.lumi = lumi


# Local files

ggh_local = SmpNtuple("H2Mu_gg","H2Mu_gg", "/Users/dmitrykondratyev/Documents/HiggsToMuMu/test_files/ggh/", False, True, 0.009618  ,1 )
vbf_local = SmpNtuple("H2Mu_VBF","H2Mu_VBF", "/Users/dmitrykondratyev/Documents/HiggsToMuMu/test_files/vbf/", False, True, 0.0008208 ,1  )
dy_local = SmpNtuple("ZJets_aMC", "ZJets_aMC", "/Users/dmitrykondratyev/Documents/HiggsToMuMu/test_files/dy/",  False, True, 5765.4, 1)
tt_local = SmpNtuple("tt_ll_POW", "tt_ll_POW", "/Users/dmitrykondratyev/Documents/HiggsToMuMu/test_files/tt/", False, True, 85.656, 1)


# Latinos ntuples (need to fix paths)

latinos_path = "/mnt/hadoop/store/group/local/hmm/ntuples/"

mc2016_path = "/2016/MCl2loose2016hmm__MCCorr2016hmm__l2tightOR2016hmm/"
data2016_path = "/2016/DATAl2loose2016hmm__l2tightOR2016hmm/"

latinos_data_2016 = SmpNtuple("SingleMu_2016","SingleMu_2016", latinos_path+data2016_path, True, True, 1, 35867)

latinos_ggh_2016 = SmpNtuple("ggH_2016","ggH 2016", latinos_path+mc2016_path+"*GluGluH*", False, False, 1, 1)
latinos_vbf_2016 = SmpNtuple("VBF_2016","VBF 2016", latinos_path+mc2016_path+"*VBFH*", False, False, 1, 1)
latinos_vh_2016 = SmpNtuple("VH_2016","VH 2016", latinos_path+mc2016_path+"*ZH_H*", False, False, 1, 1)
latinos_tth_2016 = SmpNtuple("ttH_2016","ttH 2016", latinos_path+mc2016_path+"*ttH*", False, False, 1, 1)

latinos_dy_2016 = SmpNtuple("DY_2016","DY 2016", latinos_path+mc2016_path+"*DYJetsToLL_M-105To160*", False, False, 1, 1)
latinos_top_2016 = SmpNtuple("top_2016","top 2016", latinos_path+mc2016_path+"*TTJets_DiLept*", False, False, 1, 1)
latinos_vv_2016 = SmpNtuple("VV_2016","VV 2016", latinos_path+mc2016_path+"*WZTo2L2Q*", False, False, 1, 1)


# UCSD files with trained BDTs
# Don't care about cross sections here because the event weights are already in the trees

ucsd_path = "/mnt/hadoop/store/user/dkondrat/UCSD_files/"

ucsd_ggh_2016 = SmpNtuple("ggH_2016","ggH 2016", ucsd_path+"/2016/"+"tree_ggH.root", False, False, 1, 1)
ucsd_ggh_2017 = SmpNtuple("ggH_2017","ggH 2017", ucsd_path+"/2017/"+"tree_ggH.root", False, False, 1, 1)
ucsd_ggh_2018 = SmpNtuple("ggH_2018","ggH 2018", ucsd_path+"/2018/"+"tree_ggH.root", False, False, 1, 1)

ucsd_vbf_2016 = SmpNtuple("VBF_2016","VBF 2016", ucsd_path+"/2016/"+"tree_VBF.root", False, False, 1, 1)
ucsd_vbf_2017 = SmpNtuple("VBF_2017","VBF 2017", ucsd_path+"/2017/"+"tree_VBF.root", False, False, 1, 1)
ucsd_vbf_2018 = SmpNtuple("VBF_2018","VBF 2018", ucsd_path+"/2018/"+"tree_VBF.root", False, False, 1, 1)

ucsd_vh_2016 = SmpNtuple("VH_2016","VH 2016", ucsd_path+"/2016/"+"tree_VH.root", False, False, 1, 1)
ucsd_vh_2017 = SmpNtuple("VH_2017","VH 2017", ucsd_path+"/2017/"+"tree_VH.root", False, False, 1, 1)
ucsd_vh_2018 = SmpNtuple("VH_2018","VH 2018", ucsd_path+"/2018/"+"tree_VH.root", False, False, 1, 1)

ucsd_tth_2016 = SmpNtuple("ttH_2016","ttH 2016", ucsd_path+"/2016/"+"tree_ttH.root", False, False, 1, 1)
ucsd_tth_2017 = SmpNtuple("ttH_2017","ttH 2017", ucsd_path+"/2017/"+"tree_ttH.root", False, False, 1, 1)
ucsd_tth_2018 = SmpNtuple("ttH_2018","ttH 2018", ucsd_path+"/2018/"+"tree_ttH.root", False, False, 1, 1)

ucsd_dy_2016 = SmpNtuple("DY_2016","DY 2016", ucsd_path+"/2016/"+"tree_DY.root", False, False, 1, 1)
ucsd_dy_2017 = SmpNtuple("DY_2017","DY 2017", ucsd_path+"/2017/"+"tree_DY.root", False, False, 1, 1)
ucsd_dy_2018 = SmpNtuple("DY_2018","DY 2018", ucsd_path+"/2018/"+"tree_DY.root", False, False, 1, 1)

ucsd_top_2016 = SmpNtuple("top_2016","top 2016", ucsd_path+"/2016/"+"tree_top.root", False, False, 1, 1)
ucsd_top_2017 = SmpNtuple("top_2017","top 2017", ucsd_path+"/2017/"+"tree_top.root", False, False, 1, 1)
ucsd_top_2018 = SmpNtuple("top_2018","top 2018", ucsd_path+"/2018/"+"tree_top.root", False, False, 1, 1)

ucsd_vv_2016 = SmpNtuple("VV_2016","VV 2016", ucsd_path+"/2016/"+"tree_VV.root", False, False, 1, 1)
ucsd_vv_2017 = SmpNtuple("VV_2017","VV 2017", ucsd_path+"/2017/"+"tree_VV.root", False, False, 1, 1)
ucsd_vv_2018 = SmpNtuple("VV_2018","VV 2018", ucsd_path+"/2018/"+"tree_VV.root", False, False, 1, 1)


# April 6, 2019 production: most of variables present, except angles in CS frame

ggH_2017_powheg_Apr6 = SmpNtuple("H2Mu_gg","H2Mu_gg 2017 powheg", "/mnt/hadoop/store/user/dkondrat/GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_gg_powheg/190406_001015/0000/", False, True, 0.009618  ,1 )
VBF_2017_powheg_Apr6 = SmpNtuple("H2Mu_VBF","H2Mu_VBF 2017 powheg", "/mnt/hadoop/store/user/dkondrat/VBFHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_VBF_powheg/190406_001029/0000/", False, True, 0.0008208 ,1  )

ZJets_aMC_2017_Apr6 = SmpNtuple("ZJets_aMC","ZJets_aMC 2017 low-stat", "/mnt/hadoop/store/user/dkondrat/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/ZJets_AMC/190406_001043/0000/", False, True, 5765.4, 1)
ZJets_aMC_2017_hiStat_Apr6 = SmpNtuple("ZJets_aMC", "ZJets_aMC 2017 high-stat", "/mnt/hadoop/store/user/dkondrat/DYJetsToLL_M-105To160_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/ZJets_AMC_hiStat/190406_001056/0000/", False, True, 47.17, 1)

tt_ll_POW_2017_Apr6 = SmpNtuple("tt_ll_POW","tt_ll 2017 powheg", "/mnt/hadoop/store/user/dkondrat/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/tt_ll_POW/190406_001138/0000/", False, True, 85.656, 1)

SingleMu2017B_Apr6 = SmpNtuple("SingleMu_2017B","SingleMu_2017B", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017B/190406_000906/0000/", True, True, 1, 4793.961)
SingleMu2017C_Apr6 = SmpNtuple("SingleMu_2017C","SingleMu_2017C", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017C/190406_000919/0000/", True, True, 1, 9631.612)
SingleMu2017D_Apr6 = SmpNtuple("SingleMu_2017D","SingleMu_2017D", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017D/190406_000933/0000/", True, True, 1, 4208.785)
SingleMu2017E_Apr6 = SmpNtuple("SingleMu_2017E","SingleMu_2017E", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017E/190406_000946/0000/", True, True, 1, 8955.851)
SingleMu2017F_Apr6 = SmpNtuple("SingleMu_2017F","SingleMu_2017F", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017F/190406_001000/0000/", True, True, 1, 12900.503)
 
# April 15, 2019 production: angles in CS frame included

ggH_2017_powheg_Apr15 = SmpNtuple("H2Mu_gg","H2Mu_gg 2017 powheg", "/mnt/hadoop/store/user/dkondrat/GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_gg_powheg/190415_222833/0000/", False, True, 0.009618  ,1 )
VBF_2017_powheg_Apr15 = SmpNtuple("H2Mu_VBF","H2Mu_VBF 2017 powheg", "/mnt/hadoop/store/user/dkondrat/VBFHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_VBF_powheg/190415_222848/0000/", False, True, 0.0008208 ,1  )

ZJets_aMC_2017_hiStat_Apr15 = SmpNtuple("ZJets_aMC", "ZJets_aMC 2017 high-stat", "/mnt/hadoop/store/user/dkondrat/DYJetsToLL_M-105To160_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/ZJets_AMC_hiStat/190415_222904/0000/", False, True, 47.17, 1)

tt_ll_POW_2017_Apr15 = SmpNtuple("tt_ll_POW","tt_ll 2017 powheg", "/mnt/hadoop/store/user/dkondrat/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/tt_ll_POW/190415_222920/0000/", False, True, 85.656, 1)

SingleMu2017B_Apr15 = SmpNtuple("SingleMu_2017B","SingleMu_2017B", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017B/190415_222712/0000/", True, True, 1,  4793.961)
SingleMu2017C_Apr15 = SmpNtuple("SingleMu_2017C","SingleMu_2017C", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017C/190415_222730/0000/", True, True, 1,  9591.411)
SingleMu2017D_Apr15 = SmpNtuple("SingleMu_2017D","SingleMu_2017D", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017D/190415_222746/0000/", True, True, 1,  4247.682)
SingleMu2017E_Apr15 = SmpNtuple("SingleMu_2017E","SingleMu_2017E", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017E/190415_222801/0000/", True, True, 1,  9284.706)
SingleMu2017F_Apr15 = SmpNtuple("SingleMu_2017F","SingleMu_2017F", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017F/190415_222818/0000/", True, True, 1,  13476.461)

###

# April 15, 2019 production: angles in CS frame included; fixed phiCS

ggH_2017_powheg_Apr19 = SmpNtuple("H2Mu_gg","H2Mu_gg 2017 powheg", "/mnt/hadoop/store/user/dkondrat/GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_gg_powheg/190419_161651/0000/", False, True, 0.009618  ,1 )
VBF_2017_powheg_Apr19 = SmpNtuple("H2Mu_VBF","H2Mu_VBF 2017 powheg", "/mnt/hadoop/store/user/dkondrat/VBFHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_VBF_powheg/190419_161716/0000/", False, True, 0.0008208 ,1  )

ZJets_aMC_2017_hiStat_Apr19 = SmpNtuple("ZJets_aMC", "ZJets_aMC 2017 high-stat", "/mnt/hadoop/store/user/dkondrat/DYJetsToLL_M-105To160_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/ZJets_AMC_hiStat/190419_161740/0000/", False, True, 47.17, 1)

tt_ll_POW_2017_Apr19 = SmpNtuple("tt_ll_POW","tt_ll 2017 powheg", "/mnt/hadoop/store/user/dkondrat/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/tt_ll_POW/190419_161808/0000/", False, True, 85.656, 1)

SingleMu2017B_Apr19 = SmpNtuple("SingleMu_2017B","SingleMu_2017B", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017B/190419_161448/0000/", True, True, 1,  4723.411) 
SingleMu2017C_Apr19 = SmpNtuple("SingleMu_2017C","SingleMu_2017C", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017C/190419_161512/0000/", True, True, 1,  9631.612) 
SingleMu2017D_Apr19 = SmpNtuple("SingleMu_2017D","SingleMu_2017D", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017D/190419_161536/0000/", True, True, 1,  4247.682) 
SingleMu2017E_Apr19 = SmpNtuple("SingleMu_2017E","SingleMu_2017E", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017E/190419_161602/0000/", True, True, 1,  9028.733)
SingleMu2017F_Apr19 = SmpNtuple("SingleMu_2017F","SingleMu_2017F", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017F/190419_161626/0000/", True, True, 1,  13443.249) # recalculate lumi!
