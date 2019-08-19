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

p.tree_path = "Events"
p.has_metadata = False

vbf = p.add_signal("VBF", ROOT.kViolet)
vbf.get_file(latinos_vbf_2016.name, latinos_vbf_2016.path+"part0*", latinos_vbf_2016.xSec)

ggh = p.add_signal("ggH", ROOT.kRed)
ggh.get_file(latinos_ggh_2016.name, latinos_ggh_2016.path+"part0*", latinos_ggh_2016.xSec)

ttst = p.add_source("t#bar{t} + Single top", ROOT.kYellow)
ttst.get_file(latinos_top_2016.name, latinos_top_2016.path+"part0*", latinos_top_2016.xSec)

dy = p.add_source("Drell-Yan", ROOT.kOrange-3)
dy.get_file(latinos_dy_2016.name, latinos_dy_2016.path+"part0*", latinos_dy_2016.xSec)

p.add_data_dir(latinos_data_2016.name, latinos_data_2016.path+"*part0*", latinos_data_2016.lumi)   
  
p.add_variable("mll", 1)
# p.add_variable("Muon_eta", 2)

p.set_out_dir(args.output_path)
selection = "1"
# selection = "(mll>110)&(mll<150)&(Muon_pt[0]>30)&(Muon_pt[1]>20)"

p.add_selection(selection)

p.add_wgt_sf("1")
# p.add_wgt_sf("XSWeight*SFweight2l*GenLepMatch2l*METFilter_MC")
p.setLogY() 


p.plot_stack()
#================================================
