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
vbf.get_file(latinos_vbf_2016.name, latinos_vbf_2016.path+"part0*", 1)

ggh = p.add_signal("ggH", ROOT.kRed)
ggh.get_file(latinos_ggh_2016.name, latinos_ggh_2016.path+"part0*", 1)

vh = p.add_signal("VH", ROOT.kGreen)
vh.get_file(latinos_wplush_2016.name, latinos_wplush_2016.path+"part0*", 1)
vh.get_file(latinos_wminush_2016.name, latinos_wminush_2016.path+"part0*", 1)
vh.get_file(latinos_zh_2016.name, latinos_zh_2016.path+"part0*", 1)

tth = p.add_signal("ttH", ROOT.kBlue)
tth.get_file(latinos_tth_2016.name, latinos_tth_2016.path+"part0*", 1)

ttst = p.add_source("t#bar{t} + Single top", ROOT.kYellow)
ttst.get_file(latinos_ttto2l2nu_2016.name, latinos_ttto2l2nu_2016.path+"part0*", 1)
ttst.get_file(latinos_tttosemileptonic_2016.name, latinos_tttosemileptonic_2016.path+"part0*", 1)
ttst.get_file(latinos_st_tw_antitop_2016.name, latinos_st_tw_antitop_2016.path+"part0*", 1)
ttst.get_file(latinos_st_tw_top_2016.name, latinos_st_tw_top_2016.path+"part0*", 1)
ttst.get_file(latinos_st_s_2016.name, latinos_st_s_2016.path+"part0*", 1)
ttst.get_file(latinos_st_t_antitop_2016.name, latinos_st_t_antitop_2016.path+"part0*", 1)
ttst.get_file(latinos_st_t_top_2016.name, latinos_st_t_top_2016.path+"part0*", 1)

dy = p.add_source("Drell-Yan", ROOT.kOrange-3)
dy.get_file(latinos_dy_2016.name, latinos_dy_2016.path+"part0*", 1)

# p.add_data_dir(latinos_data_2016.name, latinos_data_2016.path+"*part0*", latinos_data_2016.lumi)   
p.add_data_dir(latinos_data_2016.name, latinos_data_2016.path+"*part0*", 1)   
  
p.add_variable("mll", 1)
# p.add_variable("Muon_eta", 2)

p.set_out_dir(args.output_path)
selection = "(Muon_pt[0]>30)&(Muon_pt[1]>20)"
# selection = "(mll>110)&(mll<150)&(Muon_pt[0]>30)&(Muon_pt[1]>20)"

p.add_selection(selection)

# p.add_wgt_sf("XSWeight*SFweight2l*GenLepMatch2l")
p.add_wgt_sf("XSWeight*SFweight2l*GenLepMatch2l*METFilter_MC")
p.setLogY() 


p.plot_stack()
#================================================
