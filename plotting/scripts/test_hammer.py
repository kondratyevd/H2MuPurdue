import os,sys
sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )

import ROOT
 
import argparse
from plotter import NTuplePlotter
from samples.ntuples import *

parser = argparse.ArgumentParser(description='')
parser.add_argument('--out_path', action='store', dest='output_path', help='Output path')
args = parser.parse_args()

p = NTuplePlotter()


# vbf = p.add_signal("VBF", ROOT.kViolet)
# vbf.get_dir(vbf_local.name, vbf_local.path, vbf_local.xSec)

# ggh = p.add_signal("ggH", ROOT.kRed)
# ggh.get_dir(ggh_local.name, ggh_local.path, ggh_local.xSec)

# ttst = p.add_source("t#bar{t} + Single top", ROOT.kYellow)
# ttst.get_dir(tt_local.name, tt_local.path, tt_local.xSec)

# dy = p.add_source("Drell-Yan", ROOT.kOrange-3)
# dy.get_dir(dy_local.name, dy_local.path, dy_local.xSec)


# p.add_data_dir(dy_local.name, dy_local.path, 40000)

vbf = p.add_signal("VBF", ROOT.kViolet)
vbf.get_file(VBF_2017_powheg_Apr19.name, VBF_2017_powheg_Apr19.path+"/tuple_*.root", VBF_2017_powheg_Apr19.xSec)

ggh = p.add_signal("ggH", ROOT.kRed)
ggh.get_file(ggH_2017_powheg_Apr19.name, ggH_2017_powheg_Apr19.path+"/tuple_*.root", ggH_2017_powheg_Apr19.xSec)

ttst = p.add_source("t#bar{t} + Single top", ROOT.kYellow)
ttst.get_file(tt_ll_POW_2017_Apr19.name, tt_ll_POW_2017_Apr19.path+"/tuple_*.root", tt_ll_POW_2017_Apr19.xSec)

dy = p.add_source("Drell-Yan", ROOT.kOrange-3)
dy.get_file(ZJets_aMC_2017_hiStat_Apr19.name, ZJets_aMC_2017_hiStat_Apr19.path+"/tuple_*.root", ZJets_aMC_2017_hiStat_Apr19.xSec)

p.add_data_dir(SingleMu2017B_Apr19.name, SingleMu2017B_Apr19.path, SingleMu2017B_Apr19.lumi)   
# p.add_data_dir(SingleMu2017C_Apr15.name, SingleMu2017C_Apr15.path, SingleMu2017C_Apr15.lumi) 
# p.add_data_dir(SingleMu2017D_Apr15.name, SingleMu2017D_Apr15.path, SingleMu2017D_Apr15.lumi) 
# p.add_data_dir(SingleMu2017E_Apr15.name, SingleMu2017E_Apr15.path, SingleMu2017E_Apr15.lumi) 
# p.add_data_dir(SingleMu2017F_Apr15.name, SingleMu2017F_Apr15.path, SingleMu2017F_Apr15.lumi)    


# p.add_variable("muPairs.mass_res", 1)
p.add_variable("muPairs.phiCS", 1)
p.add_variable("muPairs.cosThetaCS", 1)
# p.add_variable("muPairs.mass_Roch", 1)
# p.add_variable("nJets", 1)

p.set_out_dir(args.output_path)
selection = "(nMuons>1)&(nMuPairs>0)&(muPairs.mass_Roch>110)&(muPairs.mass_Roch<150)&(muons.pt_Roch[0]>30)&(muons.pt_Roch[1]>20)&(muons.isHltMatched[0][2] || muons.isHltMatched[0][3] || (muons.pt_Roch[1]>30 & muons.isHltMatched[1][2]) || (muons.pt_Roch[1]>30 & muons.isHltMatched[1][3])  )"

p.add_selection(selection)

p.add_wgt_sf("(IsoMu_SF_3 * MuID_SF_3 * MuIso_SF_3)*(PU_wgt*GEN_wgt)")
p.setLogY() 


p.plot_stack()
#================================================
