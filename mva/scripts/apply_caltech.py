import os, sys
sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
import argparse
from classifier import Framework

from samples.ntuples import *

parser = argparse.ArgumentParser(description='')
parser.add_argument('--out_path', action='store', dest='output_path', help='Output path')
args = parser.parse_args()


c = Framework(outPath=args.output_path)
c.label = "apply_caltech"
comment = "apply_caltech"  
                # change this line for each run
c.add_comment(comment)
print comment

treePath = 'tree'

c.set_tree_path(treePath)

c.set_year("caltech")
# c.massWindow = [120,130]


c.trained_model_path =   '$FRAMEWORK_PATH/mva/data/DNN27vars_sig_vbf_bkg_dyvbf_dy105To160_ewk105To160_split_60_40_mod10_190820.h5'
c.standartization_path = '$FRAMEWORK_PATH/mva/data/DNN27vars_sig_vbf_bkg_dyvbf_dy105To160_ewk105To160_split_60_40_mod10_190820.npy'

##################### Input samples #######################


c.add_category(c.ggh_label, True)
c.add_file_to_category(latinos_ggh_2016.name, latinos_ggh_2016.path, latinos_ggh_2016.xSec, c.ggh_label, False)


##########################################################



###  ------   Caltech variables   ------ ###
c.add_variable("njet") # replace with softjet5 later 
c.add_variable("yll") # replace with drll
c.add_variable("yll") # replace with detall
c.add_variable("mjj")
c.add_variable("mjj") # replace with ptjj
c.add_variable("detajj") #replace with etajj
c.add_variable("phiCS") # replace with phijj
c.add_variable('mjj') # replace with mlljj
c.add_variable('detajj') #replace with etalljj
c.add_variable("phiCS") #replace with philljj
c.add_variable("detajj")
c.add_variable("zeppjj")
c.add_variable("drlj") #min dr(mu,j)
c.add_variable("drlj") #replace with maxdrlj
c.add_variable("drlj") #replace with mindrllj
c.add_variable("drlj") #replace with maxdrllj
c.add_variable("yll") #replace with dphill
c.add_variable("CleanJet_pt", 2)
c.add_variable("CleanJet_eta", 2)
c.add_variable("Jet_qgl", 2) # replace with CleanJet_qgl
c.add_variable("cosThetaCS")

c.add_variable("ptll")
c.add_variable("yll") #replace with etall
c.add_variable("mll")

###############################################

# c.add_spectator('hmass')
# c.add_spectator('weight')

# c.weigh_by_event(True)


c.add_package("Keras")
c.apply_methods()

print "Application done: "
print comment
print "Output saved to:"
print c.outPath

