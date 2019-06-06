import os, sys
sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
import argparse
from classifier import Framework

from samples.ntuples import *

parser = argparse.ArgumentParser(description='')
parser.add_argument('--out_path', action='store', dest='output_path', help='Output path')
args = parser.parse_args()


c = Framework(outPath=args.output_path)
c.label = "dnn_resweights"
comment = "DNN UCSD resweights"  
                # change this line for each run
c.add_comment(comment)
print comment

treePath = 'tree'

c.set_tree_path(treePath)

c.set_year("ucsd_inclusive")
c.massWindow = [120,130]
c.multiclass = False


##################### Input samples #######################


c.add_category('signal', True)
c.add_file_to_category(ucsd_ggh_2016.name, ucsd_ggh_2016.path, ucsd_ggh_2016.xSec, 'signal', False)
# c.add_file_to_category(ucsd_ggh_2017.name, ucsd_ggh_2017.path, ucsd_ggh_2017.xSec, 'signal', False)
# c.add_file_to_category(ucsd_ggh_2018.name, ucsd_ggh_2018.path, ucsd_ggh_2018.xSec, 'signal', False)
# c.add_file_to_category(ucsd_vbf_2016.name, ucsd_vbf_2016.path, ucsd_vbf_2016.xSec, 'signal', False)
# c.add_file_to_category(ucsd_vbf_2017.name, ucsd_vbf_2017.path, ucsd_vbf_2017.xSec, 'signal', False)
# c.add_file_to_category(ucsd_vbf_2018.name, ucsd_vbf_2018.path, ucsd_vbf_2018.xSec, 'signal', False)

c.add_category('background', False)
c.add_file_to_category(ucsd_dy_2016.name, ucsd_dy_2016.path, ucsd_dy_2016.xSec, 'background', False)
# c.add_file_to_category(ucsd_dy_2017.name, ucsd_dy_2017.path, ucsd_dy_2017.xSec, 'background', False)
# c.add_file_to_category(ucsd_dy_2018.name, ucsd_dy_2018.path, ucsd_dy_2018.xSec, 'background', False)
# c.add_file_to_category(ucsd_top_2016.name, ucsd_top_2016.path, ucsd_top_2016.xSec, 'background', False)
# c.add_file_to_category(ucsd_top_2017.name, ucsd_top_2017.path, ucsd_top_2017.xSec, 'background', False)
# c.add_file_to_category(ucsd_top_2018.name, ucsd_top_2018.path, ucsd_top_2018.xSec, 'background', False)


##########################################################



###  ------   Raffaele's variables   ------ ###
c.add_variable("hmmpt") 
c.add_variable("hmmrap")
c.add_variable("hmmthetacs") 
c.add_variable("hmmphics")
c.add_variable("met")
c.add_variable("m1ptOverMass")
c.add_variable("m2ptOverMass")
c.add_variable('m1eta')
c.add_variable('m2eta')
c.add_variable("njets")
c.add_variable("nbjets")
c.add_variable("zepen")
c.add_variable("j1pt")
c.add_variable("j2pt")
c.add_variable("j1eta")
c.add_variable("mjj")
c.add_variable("detajj")
c.add_variable("dphijj")
###############################################

c.add_spectator('hmass')
c.add_spectator('hmerr')
c.add_spectator('weight')

c.weigh_by_event(True)

c.add_package("Keras")
c.add_method("model_sigloss") # Dropout 0.2

c.train_methods()

print "Training is done: "
print comment
print "Output saved to:"
print c.outPath

