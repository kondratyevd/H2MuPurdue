import os,sys
sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )

import ROOT
 
import argparse
from plotter import NTuplePlotter
from samples.ntuples import *

parser = argparse.ArgumentParser(description='')
parser.add_argument('--out_path', action='store', dest='output_path', help='Output path')
parser.add_argument('--zpt', action='store_true', dest='zpt', help='Z pT reweighting')
parser.add_argument('--mass_min', action='store', dest='mass_min', help='Mass min')
parser.add_argument('--mass_max', action='store', dest='mass_max', help='Mass max')

args = parser.parse_args()
p = NTuplePlotter()
p.reweight_zpt = args.zpt
print args.zpt
p.tree_path = "Events"
p.has_metadata = False

# files_to_run = "*part0*"
files_to_run = ""

ggh = p.add_signal("ggH", ROOT.kRed)
ggh.get_file(latinos_ggh_2016.name, latinos_ggh_2016.path+files_to_run, 1)

vbf = p.add_signal("VBF", ROOT.kViolet)
vbf.get_file(latinos_vbf_2016.name, latinos_vbf_2016.path+files_to_run, 1)

vh = p.add_signal("VH", ROOT.kGreen)
vh.get_file(latinos_wplush_2016.name, latinos_wplush_2016.path+files_to_run, 1)
vh.get_file(latinos_wminush_2016.name, latinos_wminush_2016.path+files_to_run, 1)
vh.get_file(latinos_zh_2016.name, latinos_zh_2016.path+files_to_run, 1)

tth = p.add_signal("ttH", ROOT.kBlue)
tth.get_file(latinos_tth_2016.name, latinos_tth_2016.path+files_to_run, 1)

vvv = p.add_source("VVV", ROOT.kOrange+3)
vvv.get_file(latinos_zzz_2016.name, latinos_zzz_2016.path+files_to_run, 1)
vvv.get_file(latinos_wzz_2016.name, latinos_wzz_2016.path+files_to_run, 1)
vvv.get_file(latinos_wwz_2016.name, latinos_wwz_2016.path+files_to_run, 1)
vvv.get_file(latinos_www_2016.name, latinos_www_2016.path+files_to_run, 1)

vv = p.add_source("VV", ROOT.kTeal-5)
vv.get_file(latinos_wwto2l2nu_2016.name, latinos_wwto2l2nu_2016.path+files_to_run, 1)
vv.get_file(latinos_wzto2l2q_2016.name, latinos_wzto2l2q_2016.path+files_to_run, 1)
vv.get_file(latinos_wzto3lnu_2016.name, latinos_wzto3lnu_2016.path+files_to_run, 1)
vv.get_file(latinos_zzto2l2nu_2016.name, latinos_zzto2l2nu_2016.path+files_to_run, 1)
vv.get_file(latinos_zzto2l2q_2016.name, latinos_zzto2l2q_2016.path+files_to_run, 1)
vv.get_file(latinos_zzto4l_2016.name, latinos_zzto4l_2016.path+files_to_run, 1)

ttst = p.add_source("t#bar{t} + Single top", ROOT.kYellow)
ttst.get_file(latinos_ttto2l2nu_2016.name, latinos_ttto2l2nu_2016.path+files_to_run, 1)
ttst.get_file(latinos_tttosemileptonic_2016.name, latinos_tttosemileptonic_2016.path+files_to_run, 1)
ttst.get_file(latinos_st_tw_antitop_2016.name, latinos_st_tw_antitop_2016.path+files_to_run, 1)
ttst.get_file(latinos_st_tw_top_2016.name, latinos_st_tw_top_2016.path+files_to_run, 1)
ttst.get_file(latinos_st_s_2016.name, latinos_st_s_2016.path+files_to_run, 1)
ttst.get_file(latinos_st_t_antitop_2016.name, latinos_st_t_antitop_2016.path+files_to_run, 1)
ttst.get_file(latinos_st_t_top_2016.name, latinos_st_t_top_2016.path+files_to_run, 1)

dy = p.add_source("Drell-Yan", ROOT.kOrange-3)
dy.get_file(latinos_dy_2016.name, latinos_dy_2016.path+files_to_run, 1)

p.add_data_dir(latinos_data_2016.name, latinos_data_2016.path+files_to_run, latinos_data_2016.lumi)   
  
# p.add_variable("mll")
# p.add_variable("mllErr")
# p.add_variable("yll")
# p.add_variable("cosThetaCS")
# p.add_variable("phiCS")
p.add_variable("ptll")
# p.add_variable("Muon_pt", 2)
# p.add_variable("Muon_eta", 2)
# p.add_variable("CleanJet_pt", 2)
# p.add_variable("CleanJet_eta", 2)
# p.add_variable("detajj")
# p.add_variable("mjj")
# p.add_variable("zeppjj")
# p.add_variable("nJet")
# p.add_variable("MET_pt")


p.set_out_dir(args.output_path)


supercut = '   Lepton_pt[0]>26 \
            && Lepton_pt[1]>20 \
            && (nLepton>=2 && (Alt$(Lepton_pt[2],0)<10) || Alt$(Lepton_pdgId[2],13)==13) \
            && abs(Lepton_eta[0])<2.4 && abs(Lepton_eta[1])<2.4 \
            && (Lepton_pdgId[0]*Lepton_pdgId[1]==(-13*13)) \
            '
bveto = '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta)<2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.6321) == 0)'
jets = '((!CleanJet_pt[0] || CleanJet_pt[0]>30) && (!CleanJet_pt[1] || CleanJet_pt[1]>30) )'

selection = '(mll>%s)&(mll<%s)&(%s)&(%s)&(%s)'%(args.mass_min, args.mass_max, supercut, bveto, jets) # Z peak


p.add_selection(selection)

p.add_wgt_sf("XSWeight*SFweight2l*GenLepMatch2l*METFilter_MC*%f"%(latinos_data_2016.lumi/1000.))
p.setLogY() 


p.plot_stack()
#================================================
