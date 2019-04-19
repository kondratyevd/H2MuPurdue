
class SmpNtuple(object):
    def __init__(self, name, title, path, isData, xSec, lumi):
        self.name = name
        self.title = title
        self.path = path
        self.isData = isData
        self.xSec = xSec
        self.lumi = lumi


# Local files

ggh_local = SmpNtuple("H2Mu_gg","H2Mu_gg", "/Users/dmitrykondratyev/Documents/HiggsToMuMu/test_files/ggh/", False, 0.009618  ,1 )
vbf_local = SmpNtuple("H2Mu_VBF","H2Mu_VBF", "/Users/dmitrykondratyev/Documents/HiggsToMuMu/test_files/vbf/", False, 0.0008208 ,1  )
dy_local = SmpNtuple("ZJets_aMC", "ZJets_aMC", "/Users/dmitrykondratyev/Documents/HiggsToMuMu/test_files/dy/",  False, 5765.4, 1)
tt_local = SmpNtuple("tt_ll_POW", "tt_ll_POW", "/Users/dmitrykondratyev/Documents/HiggsToMuMu/test_files/tt/", False, 85.656, 1)


# April 6, 2019 production: most of variables present, except angles in CS frame

ggH_2017_powheg_Apr6 = SmpNtuple("H2Mu_gg","H2Mu_gg 2017 powheg", "/mnt/hadoop/store/user/dkondrat/GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_gg_powheg/190406_001015/0000/", False, 0.009618  ,1 )
VBF_2017_powheg_Apr6 = SmpNtuple("H2Mu_VBF","H2Mu_VBF 2017 powheg", "/mnt/hadoop/store/user/dkondrat/VBFHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_VBF_powheg/190406_001029/0000/", False, 0.0008208 ,1  )

ZJets_aMC_2017_Apr6 = SmpNtuple("ZJets_aMC","ZJets_aMC 2017 low-stat", "/mnt/hadoop/store/user/dkondrat/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/ZJets_AMC/190406_001043/0000/", False, 5765.4, 1)
ZJets_aMC_2017_hiStat_Apr6 = SmpNtuple("ZJets_aMC", "ZJets_aMC 2017 high-stat", "/mnt/hadoop/store/user/dkondrat/DYJetsToLL_M-105To160_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/ZJets_AMC_hiStat/190406_001056/0000/", False, 47.17, 1)

tt_ll_POW_2017_Apr6 = SmpNtuple("tt_ll_POW","tt_ll 2017 powheg", "/mnt/hadoop/store/user/dkondrat/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/tt_ll_POW/190406_001138/0000/", False, 85.656, 1)

SingleMu2017B_Apr6 = SmpNtuple("SingleMu_2017B","SingleMu_2017B", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017B/190406_000906/0000/", True, 1, 4793.961)
SingleMu2017C_Apr6 = SmpNtuple("SingleMu_2017C","SingleMu_2017C", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017C/190406_000919/0000/", True, 1, 9631.612)
SingleMu2017D_Apr6 = SmpNtuple("SingleMu_2017D","SingleMu_2017D", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017D/190406_000933/0000/", True, 1, 4208.785)
SingleMu2017E_Apr6 = SmpNtuple("SingleMu_2017E","SingleMu_2017E", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017E/190406_000946/0000/", True, 1, 8955.851)
SingleMu2017F_Apr6 = SmpNtuple("SingleMu_2017F","SingleMu_2017F", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017F/190406_001000/0000/", True, 1, 12900.503)
 
# April 15, 2019 production: angles in CS frame included

ggH_2017_powheg_Apr15 = SmpNtuple("H2Mu_gg","H2Mu_gg 2017 powheg", "/mnt/hadoop/store/user/dkondrat/GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_gg_powheg/190415_222833/0000/", False, 0.009618  ,1 )
VBF_2017_powheg_Apr15 = SmpNtuple("H2Mu_VBF","H2Mu_VBF 2017 powheg", "/mnt/hadoop/store/user/dkondrat/VBFHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_VBF_powheg/190415_222848/0000/", False, 0.0008208 ,1  )

ZJets_aMC_2017_hiStat_Apr15 = SmpNtuple("ZJets_aMC", "ZJets_aMC 2017 high-stat", "/mnt/hadoop/store/user/dkondrat/DYJetsToLL_M-105To160_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/ZJets_AMC_hiStat/190415_222904/0000/", False, 47.17, 1)

tt_ll_POW_2017_Apr15 = SmpNtuple("tt_ll_POW","tt_ll 2017 powheg", "/mnt/hadoop/store/user/dkondrat/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/tt_ll_POW/190415_222920/0000/", False, 85.656, 1)

SingleMu2017B_Apr15 = SmpNtuple("SingleMu_2017B","SingleMu_2017B", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017B/190415_222712/0000/", True, 1,  4793.961)
SingleMu2017C_Apr15 = SmpNtuple("SingleMu_2017C","SingleMu_2017C", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017C/190415_222730/0000/", True, 1,  9591.411)
SingleMu2017D_Apr15 = SmpNtuple("SingleMu_2017D","SingleMu_2017D", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017D/190415_222746/0000/", True, 1,  4247.682)
SingleMu2017E_Apr15 = SmpNtuple("SingleMu_2017E","SingleMu_2017E", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017E/190415_222801/0000/", True, 1,  9284.706)
SingleMu2017F_Apr15 = SmpNtuple("SingleMu_2017F","SingleMu_2017F", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017F/190415_222818/0000/", True, 1,  13476.461)

###

# April 15, 2019 production: angles in CS frame included; fixed phiCS

ggH_2017_powheg_Apr19 = SmpNtuple("H2Mu_gg","H2Mu_gg 2017 powheg", "/mnt/hadoop/store/user/dkondrat/GluGluHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_gg_powheg/190419_161651/0000/", False, 0.009618  ,1 )
VBF_2017_powheg_Apr19 = SmpNtuple("H2Mu_VBF","H2Mu_VBF 2017 powheg", "/mnt/hadoop/store/user/dkondrat/VBFHToMuMu_M-125_TuneCP5_PSweights_13TeV_powheg_pythia8/H2Mu_VBF_powheg/190419_161716/0000/", False, 0.0008208 ,1  )

ZJets_aMC_2017_hiStat_Apr19 = SmpNtuple("ZJets_aMC", "ZJets_aMC 2017 high-stat", "/mnt/hadoop/store/user/dkondrat/DYJetsToLL_M-105To160_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8/ZJets_AMC_hiStat/190419_161740/0000/", False, 47.17, 1)

tt_ll_POW_2017_Apr19 = SmpNtuple("tt_ll_POW","tt_ll 2017 powheg", "/mnt/hadoop/store/user/dkondrat/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/tt_ll_POW/190419_161808/0000/", False, 85.656, 1)

SingleMu2017B_Apr19 = SmpNtuple("SingleMu_2017B","SingleMu_2017B", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017B/190419_161448/0000/", True, 1,  4793.961) # recalculate lumi!
SingleMu2017C_Apr19 = SmpNtuple("SingleMu_2017C","SingleMu_2017C", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017C/190419_161512/0000/", True, 1,  9591.411) # recalculate lumi!
SingleMu2017D_Apr19 = SmpNtuple("SingleMu_2017D","SingleMu_2017D", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017D/190419_161536/0000/", True, 1,  4247.682) # recalculate lumi!
SingleMu2017E_Apr19 = SmpNtuple("SingleMu_2017E","SingleMu_2017E", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017E/190419_161602/0000/", True, 1,  9284.706) # recalculate lumi!
SingleMu2017F_Apr19 = SmpNtuple("SingleMu_2017F","SingleMu_2017F", "/mnt/hadoop/store/user/dkondrat/SingleMuon/SingleMu_2017F/190419_161626/0000/", True, 1,  13476.461) # recalculate lumi!
