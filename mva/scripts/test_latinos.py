import os, sys
sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
import argparse
from classifier import Framework

from samples.ntuples import *

parser = argparse.ArgumentParser(description='')
parser.add_argument('--out_path', action='store', dest='output_path', help='Output path')
args = parser.parse_args()


c = Framework(outPath=args.output_path)
c.label = "latinos"
comment = "latinos test"  
                # change this line for each run
c.add_comment(comment)
print comment

treePath = 'Events'

c.set_tree_path(treePath)

c.set_year("latinos")
c.massWindow = [120,130]
c.multiclass = True
c.dy_label = "DY"
c.top_label = "ttbar"
c.ggh_label = "ggH"
c.vbf_label = "VBF"


##################### Input samples #######################

# for Keras
# c.add_category(c.ggh_label, True)
# c.add_file_to_category(latinos_ggh_2016.name, latinos_ggh_2016.path, latinos_ggh_2016.xSec, c.ggh_label, False)

# c.add_category(c.vbf_label, True)
# c.add_file_to_category(latinos_vbf_2016.name, latinos_vbf_2016.path, latinos_vbf_2016.xSec, c.vbf_label, False)

# c.add_category(c.dy_label, False)
# c.add_file_to_category(latinos_dy_2016.name, latinos_dy_2016.path, latinos_dy_2016.xSec, c.dy_label, False)

# c.add_category(c.vbf_label, False)
# c.add_file_to_category(latinos_ttto2l2nu_2016.name, latinos_ttto2l2nu_2016.path, latinos_ttto2l2nu_2016.xSec, c.top_label, False)

# for TMVA
c.add_signal_file(latinos_ggh_2016.name, latinos_ggh_2016.path, latinos_ggh_2016.xSec, False)
c.add_signal_file(latinos_vbf_2016.name, latinos_vbf_2016.path, latinos_vbf_2016.xSec, False)
c.add_background_file(latinos_dy_2016.name, latinos_dy_2016.path, latinos_dy_2016.xSec, False)
c.add_background_file(latinos_ttto2l2nu_2016.name, latinos_ttto2l2nu_2016.path, latinos_ttto2l2nu_2016.xSec, False)
##########################################################



###  ------   Raffaele's variables   ------ ###
c.add_variable("ptll") 
c.add_variable("yll")
c.add_variable("cosThetaCS") 
c.add_variable("phiCS")
c.add_variable("MET_pt")
c.add_variable("pt1omll")
c.add_variable("pt2omll")
c.add_variable('Muon_eta', 2)
# c.add_variable("drmj")
c.add_variable("nJet")
# c.add_variable("nbjets")
c.add_variable("zeppjj")
c.add_variable("Jet_pt", 2)
c.add_variable("mjj")
c.add_variable("detajj")
# c.add_variable("dphijj")
###############################################

c.add_spectator('mll')
c.add_spectator('XSWeight')
c.add_spectator('SFweight')
c.add_spectator('GenLepMatch')
c.add_spectator('METFilter_MC')

c.weigh_by_event(True)

c.add_package("TMVA")
c.add_method("BDTG_UCSD") # Dropout 0.2

# c.add_package("Keras")
# c.add_method("model_50_D2_25_D2_25_D2") # Dropout 0.2

c.train_methods()

print "Training is done: "
print comment
print "Output saved to:"
print c.outPath

