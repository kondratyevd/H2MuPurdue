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
