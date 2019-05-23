import os, sys
sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
import argparse
from classifier import Framework

from samples.ntuples import *

parser = argparse.ArgumentParser(description='')
parser.add_argument('--out_path', action='store', dest='output_path', help='Output path')
args = parser.parse_args()


c = Framework(outPath=args.output_path)
c.label = "local"
comment = "local dnn test"  
                # change this line for each run
c.add_comment(comment)
print comment

treePath = 'dimuons/tree'
metadataPath = 'dimuons/metadata'

c.set_tree_path(treePath)
c.set_metadata_path(metadataPath)

c.set_year("2017")

c.multiclass = True
c.dy_label = "ZJets_aMC"
c.tt_label = "tt_ll_POW"
c.ggh_label = "H2Mu_gg"
c.vbf_label = "H2Mu_VBF"


##################### Input samples #######################


c.add_category(c.ggh_label, True)
c.add_dir_to_category(ggh_local.name, ggh_local.path, ggh_local.xSec, c.ggh_label, True)

c.add_category(c.vbf_label, True)
c.add_dir_to_category(vbf_local.name, vbf_local.path, vbf_local.xSec, c.vbf_label, True)

c.add_category(c.dy_label, False)
c.add_dir_to_category(dy_local.name, dy_local.path, dy_local.xSec, c.dy_label, True)

c.add_category(c.tt_label, False)
c.add_dir_to_category(tt_local.name, tt_local.path, tt_local.xSec, c.tt_label, True)



# c.add_signal_dir(ggh_local.name, ggh_local.path, ggh_local.xSec, True)
# c.add_signal_dir(vbf_local.name, vbf_local.path, vbf_local.xSec, True)
# c.add_background_dir(dy_local.name, dy_local.path, dy_local.xSec, True)
# c.add_background_dir(tt_local.name, tt_local.path, tt_local.xSec, True)
##########################################################



###  ------   Raffaele's variables   ------ ###
c.add_variable("muPairs.pt") 
c.add_variable("muPairs.eta")
c.add_variable("muPairs.dEta") 
c.add_variable("muPairs.dPhi")
c.add_variable("met.pt")

# c.add_variable("mu1_pt_Roch_over_mass")
# c.add_variable("mu2_pt_Roch_over_mass")
c.add_variable('muons.eta',                 2)
# c.add_variable("min_dR_mu_jet")
c.add_variable("nJets")
c.add_variable("nBMed")
# c.add_variable("zeppenfeld")

c.add_variable("jets.pt",                   2)
c.add_variable("jetPairs.mass")
c.add_variable("jetPairs.dEta")
c.add_variable("jetPairs.dPhi")
###############################################


c.add_data_spectator('muons.pt',            2)
c.add_data_spectator('muPairs.mass_Roch')
c.add_data_spectator('muPairs.phi')
c.add_data_spectator('muons.isMediumID',    2)
c.add_data_spectator('jets.phi',            2)
c.add_data_spectator('nJets')

c.add_spectator('muons.pt',                 2)
c.add_spectator('muPairs.mass_Roch')
c.add_spectator('muPairs.phi')
c.add_spectator('muons.isMediumID',         2)
c.add_spectator('jets.phi',                 2)
c.add_spectator('nJets')

c.add_spectator('PU_wgt')
c.add_spectator('GEN_wgt')
c.add_spectator('IsoMu_SF_3')
c.add_spectator('MuID_SF_3')
c.add_spectator('MuIso_SF_3')


c.weigh_by_event(True)

c.add_package("Keras")
c.add_method("model_50_D2_25_D2_25_D2") # Dropout 0.2

# c.add_package("TMVA")
# c.add_method("BDTG_UF_v1")



c.train_methods()

print "Training is done: "
print comment
print "Output saved to:"
print c.outPath

