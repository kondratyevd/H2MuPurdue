import os, sys
sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )

class Variable(object):
    def __init__(self, _name, _leaf, _title, _nBins, _min, _max, _units, _type, _isMultiDim, _validation, _replacement, _abs):
        self.name = _name
        self.leaf = _leaf
        self.title = _title
        self.nBins = _nBins
        self.min = _min
        self.max = _max
        self.units = _units
        self.type = _type
        self.isMultiDim = _isMultiDim
        self.itemsAdded = 0                 
        self.replacement = _replacement
        self.validation = _validation
        self.abs = _abs
        self.comma = ' ' if self.units is '' else ', '

variables = []

variables.append(Variable("muPairs.pt"      ,   "pt"                ,"Dimuon p_{T}",        100, 0, 300,    "GeV",      'F', True,      "nMuPairs"  ,   0   , False ))
variables.append(Variable("muPairs.eta"     ,   "eta"               ,"Dimuon #eta",         100, -10, 10,   "",         'F', True,      "nMuPairs"  ,   -5  , False ))
variables.append(Variable("muPairs.phi"     ,   "phi"               ,"Dimuon #phi",         100, -3.2, 3.2, "",         'F', True,      "nMuPairs"  ,   -5  , False ))
variables.append(Variable("muPairs.dEta"    ,   "dEta"              ,"Dimuon |#delta#eta|", 100, 0, 5,      "",         'F', True,      "nMuPairs"  ,   -1  , True  ))
variables.append(Variable("muPairs.dPhi"    ,   "dPhi"              ,"Dimuon |#delta#phi|", 100, 0, 3.2,    "",         'F', True,      "nMuPairs"  ,   -1  , True  ))
variables.append(Variable("muPairs.mass"    ,   "mass"              ,"Dimuon mass",         100, 50, 200,   "GeV",      'F', True,      "nMuPairs"  ,   0   , False ))
variables.append(Variable("muPairs.mass_Roch",  "mass"              ,"Dimuon mass",         100, 50, 200,   "GeV",      'F', True,      "nMuPairs"  ,   0   , False ))

variables.append(Variable("muPairs.mass_res",   "mass_res"          ,"Ev-by-ev resolution", 100, 0, 5,      "GeV",      'F', True,      "nMuPairs"  ,   0   , False ))
variables.append(Variable("muPairs.cosThetaCS"  ,   "cosThetaCS"    ,"cosThetaCS",          100, -1, 1,      "",        'F', True,      "nMuPairs"  ,   -5  , False ))
variables.append(Variable("muPairs.phiCS"   ,   "phiCS"             ,"phiCS",               100, -3.2, 3.2,  "",        'F', True,      "nMuPairs"  ,   -1  , False ))

variables.append(Variable("muons.pt"        ,   "pt"                ,"Muon p_{T}",          100, 0, 200,    "GeV",      'F', True,      "nMuons"    ,   0   , False ))

variables.append(Variable("mu1_pt_Roch_over_mass",  "mu1_pt_Roch_over_mass" ,"Muon1 p_{T} / Mmm", 100, 0, 2,"",         'F', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("mu2_pt_Roch_over_mass",  "mu2_pt_Roch_over_mass" ,"Muon2 p_{T} / Mmm", 100, 0, 2,"",         'F', False,     "nMuons"    ,   0   , False ))

variables.append(Variable("muons.eta"       ,   "eta"               ,"Muon #eta",          100, -3,     3,  "",         'F', True,      "nMuons"    ,   -5  , False ))
variables.append(Variable("muons.phi"       ,   "phi"               ,"Muon #phi",          100, -3.2, 3.2,  "",         'F', True,      "nMuons"    ,   -5  , False ))
variables.append(Variable("muons.isMediumID",   "isMediumID"        ,"Muon ID",            2,    0,     2,  "",         'I', True,      "nMuons"    ,   0   , False ))
variables.append(Variable("muons.isHltMatched", "isHltMatched"      ,"muons.isHltMatched", 2,    0,     2,  "",         'I', True,      "nMuons"    ,   0   , False ))
variables.append(Variable("met.pt"          ,   "pt"                ,"MET",                100,  0,   300,  "GeV",      'F', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("nJets"           ,   "nJets"             ,"nJets",              8,    0,     8,  "",         'I', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("nJetsCent"       ,   "nJetsCent"         ,"nJetsCent",          8,    0,     8,  "",         'I', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("nJetsFwd"        ,   "nJetsFwd"          ,"nJetsFwd",           8,    0,     8,  "",         'I', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("nBMed"           ,   "nBMed"             ,"nBMed",              8,    0,     8,  "",         'I', False,     "nMuons"    ,   0   , False ))

variables.append(Variable("jets.pt"         ,   "pt"                ,"Jet p_{T}",          100,  0,    300, "GeV",      'F', True,      "nJets"     ,   -5  , False ))
variables.append(Variable("jets.eta"        ,   "eta"               ,"Jet #eta",           100,  -10,  10,  "",         'F', True,      "nJets"     ,   -5  , False ))
variables.append(Variable("jets.phi"        ,   "phi"               ,"Jet #phi",           100,  -3.2, 3.2, "",         'F', True,      "nJets"     ,   -5  , False )) 
variables.append(Variable("jetPairs.dEta"   ,   "dEta"              ,"jj |#delta#eta|",    100,  0,    5,   "",         'F', True,      "nJetPairs" ,   -5  , True  )) 
variables.append(Variable("jetPairs.dPhi"   ,   "dPhi"              ,"jj |#delta#phi|",    100,  0,    3.2, "",         'F', True,      "nJetPairs" ,   -5  , True  )) 
variables.append(Variable("jetPairs.mass"   ,   "mass"              ,"jj mass",            100,  0,    300, "GeV",      'F', True,      "nJetPairs" ,   -5  , False ))

variables.append(Variable("min_dR_mu_jet"   ,   "min_dR_mu_jet"     ,"min_dR_mu_jet",      100,  0,    7,   "",         'F', False,     "nJets" ,   -5  ,     False ))
variables.append(Variable("max_dR_mu_jet"   ,   "max_dR_mu_jet"     ,"max_dR_mu_jet",      100,  0,    7,   "",         'F', False,     "nJets" ,   -5  ,     False ))
variables.append(Variable("min_dR_mumu_jet" ,   "min_dR_mumu_jet"   ,"min_dR_mumu_jet",    100,  0,    7,   "",         'F', False,     "nJets" ,   -5  ,     False ))
variables.append(Variable("max_dR_mumu_jet" ,   "max_dR_mumu_jet"   ,"max_dR_mumu_jet",    100,  0,    7,   "",         'F', False,     "nJets" ,   -5  ,     False ))
variables.append(Variable("zeppenfeld"      ,   "zeppenfeld"        ,"zeppenfeld",         100,  -5,   5,   "",         'F', False,     "nJetPairs" ,-5 ,     False ))
 
variables.append(Variable("PU_wgt"          ,   "PU_wgt"                ,"PU_wgt",         100, -1000, 1000,"",         'F', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("GEN_wgt"         ,   "GEN_wgt"               ,"GEN_wgt",        100, -1000, 1000,"",         'F', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("IsoMu_SF_3"      ,   "IsoMu_SF_3"            ,"IsoMu_SF_3",     100, -1000, 1000,"",         'F', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("MuID_SF_3"       ,   "MuID_SF_3"             ,"MuID_SF_3",      100, -1000, 1000,"",         'F', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("MuIso_SF_3"      ,   "MuIso_SF_3"            ,"MuIso_SF_3",     100, -1000, 1000,"",         'F', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("IsoMu_SF_4"      ,   "IsoMu_SF_4"            ,"IsoMu_SF_4",     100, -1000, 1000,"",         'F', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("MuID_SF_4"       ,   "MuID_SF_4"             ,"MuID_SF_4",      100, -1000, 1000,"",         'F', False,     "nMuons"    ,   0   , False ))
variables.append(Variable("MuIso_SF_4"      ,   "MuIso_SF_4"            ,"MuIso_SF_4",     100, -1000, 1000,"",         'F', False,     "nMuons"    ,   0   , False ))


#### Variables in UCSD ntuples ####

variables.append(Variable("hmmpt"   ,   "hmmpt"         ,"Dimuon p_{T}",       100, 0, 100, "GeV",      'F', False,         "hmmpt" ,   0   , False ))
variables.append(Variable("hmmrap"  ,   "hmmrap"        ,"Dimuon #eta",        100, 0, 100, "",         'F', False,         "hmmpt" ,   0   , False ))
variables.append(Variable("hmass"   ,   "hmass"         ,"Dimuon mass",        100, 0, 100, "GeV",      'F', False,         "hmmpt" ,   0   , False ))
variables.append(Variable("hmerr"   ,   "hmerr"         ,"hmerr",              100, 0, 100, "",         'F', False,         "hmmpt" ,   0   , False ))
variables.append(Variable("hmmthetacs", "hmmthetacs"    ,"hmmthetacs",         100, 0, 100, "",         'F', False,         "hmmpt" ,   0   , False ))
variables.append(Variable("hmmphics",   "hmmphics"      ,"hmmphics",           100, 0, 100, "",         'F', False,         "hmmpt" ,   0   , False ))
variables.append(Variable("m1ptOverMass",   "m1ptOverMass"  ,"m1ptOverMass",   100, 0, 100, "",         'F', False,         "hmmpt" ,   0   , False ))
variables.append(Variable("m2ptOverMass",   "m2ptOverMass"  ,"m2ptOverMass",   100, 0, 100, "",         'F', False,         "hmmpt",    0   , False ))
variables.append(Variable("m1eta",          "m1eta"         ,"m1eta",          100, 0, 100, "",         'F', False,         "hmmpt" ,   0   , False ))
variables.append(Variable("m2eta",          "m2eta"         ,"m2eta",          100, 0, 100, "",         'F', False,         "hmmpt",    0   , False ))
variables.append(Variable("j1pt",           "j1pt"          ,"j1pt",           100, 0, 100, "",         'F', False,         "njets" ,   0   , False ))
variables.append(Variable("j2pt",           "j2pt"          ,"j2pt",           100, 0, 100, "",         'F', False,         "njets" ,   0   , False ))
variables.append(Variable("j3pt",           "j3pt"          ,"j3pt",           100, 0, 100, "",         'F', False,         "njets" ,   0   , False ))
variables.append(Variable("j1eta",          "j1eta"         ,"j1eta",          100, 0, 100, "",         'F', False,         "njets" ,   0   , False ))
variables.append(Variable("j2eta",          "j2eta"         ,"j2eta",          100, 0, 100, "",         'F', False,         "njets" ,   0   , False ))
variables.append(Variable("j3eta",          "j3eta"         ,"j3eta",          100, 0, 100, "",         'F', False,         "njets" ,   0   , False ))
# variables.append(Variable("detajj",         "detajj"        ,"detajj",         100, 0, 100, "",         'F', False,         "mjj"   ,   0   , False ))
# variables.append(Variable("mjj",            "mjj"           ,"mjj",            100, 0, 100, "",         'F', False,         "mjj"   ,   0   , False ))
variables.append(Variable("dphijj",         "dphijj"        ,"dphijj",         100, 0, 100, "",         'F', False,         "mjj"   ,   0   , False ))
variables.append(Variable("nbjets",         "nbjets"        ,"nbjets",         100, 0, 100, "",         'F', False,         "njets" ,   0   , False ))
variables.append(Variable("njets",          "njets"         ,"njets",          100, 0, 100, "",         'F', False,         "njets" ,   0   , False ))
variables.append(Variable("zepen",          "zepen"         ,"zepen",          100, 0, 100, "",         'F', False,         "mjj"   ,   0   , False ))
variables.append(Variable("drmj",           "drmj"          ,"drmj",           100, 0, 100, "",         'F', False,         "njets" ,   0   , False ))
variables.append(Variable("met",            "met"           ,"met",            100, 0, 100, "",         'F', False,         "met"   ,   0   , False ))
variables.append(Variable("weight",         "weight"            ,"weight",     100, 0, 100, "",         'F', False,         "hmmpt" ,   0   , False ))

#### Variables in Latinos ntuples ####

variables.append(Variable("ptll"   ,    "ptll"          ,"Dimuon p_{T}",       100, 0, 300, "GeV",      'F', False,         "ptll" ,   0   , False ))
variables.append(Variable("yll"  ,      "yll"           ,"Dimuon #eta",        100, -10, 10, "",         'F', False,         "ptll" ,   0   , False ))
# variables.append(Variable("mll"   ,     "mll"           ,"Dimuon mass",        80, 70, 110, "GeV",      'F', False,         "ptll" ,   0   , False ))
variables.append(Variable("mll"   ,     "mll"           ,"Dimuon mass",        160, 70, 150, "GeV",      'F', False,         "ptll" ,   0   , False ))
variables.append(Variable("mllErr"   ,  "mllErr"        ,"mllErr",             100, 0, 5, "GeV",         'F', False,         "ptll" ,   0   , False ))
variables.append(Variable("cosThetaCS", "cosThetaCS"    ,"cosThetaCS",         100, -1, 1, "",         'F', False,         "ptll" ,   0   , False ))
variables.append(Variable("phiCS",      "phiCS"         ,"phiCS",              100, -3.2, 3.2, "",         'F', False,         "ptll" ,   0   , False ))
variables.append(Variable("pt1omll",    "pt1omll"       ,"pt1omll",            100, 0, 100, "",         'F', False,         "ptll" ,   0   , False ))
variables.append(Variable("pt2omll",    "pt2omll"       ,"pt2omll",            100, 0, 100, "",         'F', False,         "ptll",    0   , False ))
variables.append(Variable("Muon_pt",   "Muon_pt"      ,"Muon_pt",              180, 20, 200, "",         'F', True,          "ptll" ,   0   , False ))
variables.append(Variable("Muon_eta",   "Muon_eta"      ,"Muon_eta",           48, -2.4, 2.4, "",         'F', True,          "ptll" ,   0   , False ))
variables.append(Variable("Jet_pt",     "Jet_pt"        ,"Jet_pt",             220, 30, 250, "",         'F', True,          "njet" ,   0   , False ))
variables.append(Variable("Jet_eta",    "Jet_eta"       ,"Jet_eta",            47, -4.7, 4.7, "",         'F', True,         "njet" ,   0   , False ))
variables.append(Variable("Jet_qgl",    "Jet_qgl"       ,"Jet_qgl",            100, 0, 1, "",         'F', True,         "njet" ,   0   , False ))

variables.append(Variable("CleanJet_pt", "CleanJet_pt"  ,"CleanJet_pt",        220, 30, 250, "",         'F', True,          "njet" ,   0   , False ))
variables.append(Variable("CleanJet_eta", "CleanJet_eta" ,"CleanJet_eta",      47, -4.7, 4.7, "",         'F', True,         "njet" ,   0   , False ))
variables.append(Variable("detajj",     "detajj"        ,"detajj",             35, 0, 7, "",         'F', False,         "mjj"   ,   0   , False ))
variables.append(Variable("mjj",        "mjj"           ,"mjj",                100, 0, 500, "",         'F', False,         "mjj"   ,   0   , False ))
# variables.append(Variable("dphijj",         "dphijj"        ,"dphijj",         100, 0, 100, "",         'F', False,         "mjj"   ,   0   , False ))
# variables.append(Variable("nbjets",         "nbjets"        ,"nbjets",         100, 0, 100, "",         'F', False,         "nJet" ,   0   , False ))
variables.append(Variable("nJet",       "nJet"          ,"nJet",               8, 0, 8, "",         'F', False,         "njet" ,   0   , False ))
variables.append(Variable("nbjet",         "nbjet"        ,"nbjet",         8, 0, 8, "",         'F', False,         "njet" ,   0   , False ))
variables.append(Variable("njet",          "njet"         ,"njet",          8, 0, 8, "",         'F', False,         "njet" ,   0   , False ))

variables.append(Variable("nCleanJet",  "nCleanJet"      ,"nCleanJet",         8, 0, 8, "",         'F', False,         "njet" ,   0   , False ))
variables.append(Variable("zeppjj",     "zeppjj"        ,"zeppjj",             100, -5, 5, "",         'F', False,         "mjj"   ,   0   , False ))
variables.append(Variable("drlj",       "drlj"          ,"drlj",               100, 0, 7, "",         'F', False,         "nJet" ,   0   , False ))
variables.append(Variable("MET_pt",     "MET_pt"        ,"MET_pt",             50, 0, 150, "",         'F', False,         "MET_pt"   ,   0   , False ))
variables.append(Variable("XSWeight",   "XSWeight"      ,"XSWeight",           100, 0, 100, "",         'F', False,         "ptll" ,   0   , False ))
variables.append(Variable("SFweight",   "SFweight"      ,"SFweight",           100, 0, 100, "",         'F', False,         "ptll" ,   0   , False ))
variables.append(Variable("GenLepMatch","GenLepMatch"   ,"GenLepMatch",        100, 0, 100, "",         'F', False,         "ptll" ,   0   , False ))
variables.append(Variable("METFilter_MC","METFilter_MC" ,"METFilter_MC",       100, 0, 100, "",         'F', False,         "ptll" ,   0   , False ))
    
variables.append(Variable("detajj*(njet>=2)",     "detajj*(njet>=2)"        ,"detajj*(njet>=2)",             35, 0, 7, "",         'F', False,         "mjj"   ,   0   , False ))
variables.append(Variable("mjj*(njet>=2)",        "mjj*(njet>=2)"           ,"mjj*(njet>=2)",                100, 0, 500, "",         'F', False,         "mjj"   ,   0   , False ))
variables.append(Variable("zeppjj*(njet>=2)",     "zeppjj*(njet>=2)"        ,"zeppjj*(njet>=2)",             100, -5, 5, "",         'F', False,         "mjj"   ,   0   , False ))
