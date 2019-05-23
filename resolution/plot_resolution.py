import os, sys, errno
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
import ROOT
from fitting.fit_signal import *
from samples.mva_output import dnn_local
from helpers.helpers import *

parser = argparse.ArgumentParser(description='')
parser.add_argument('--out_path', action='store', dest='output_path', help='Output path')
args = parser.parse_args()


var_name = "mass"
w = create_workspace("w", var_name, "Dimuon mass", 100, 110, 150)
frame = w.var(var_name).frame(ROOT.RooFit.Bins(100))


path = dnn_local.path+"/output_test.root"
trees = [["tree_H2Mu_gg", path]]
signal_tree = merge_trees(trees, "signal_tree", debug=True)

print "Total # of events in signal tree: ", signal_tree.GetEntries()

plot_2gaus = fit_signal(w, "2gaus", "test0",  signal_tree, var_name, 100, 110, 150, "1")
plot_3gaus = fit_signal(w, "3gaus", "test1",  signal_tree, var_name, 100, 110, 150, "1")
plot_3gausNuis = fit_signal(w, "3gausNuis", "test2",  signal_tree, var_name, 100, 110, 150, "1")
plot_cb = fit_signal(w, "cb", "test3",  signal_tree, var_name, 100, 110, 150, "1")
plot_dcb = fit_signal(w, "dcb", "test4",  signal_tree, var_name, 100, 110, 150, "1")
plot_cbgaus = fit_signal(w, "cbgaus", "test5",  signal_tree, var_name, 100, 110, 150, "1")
plot_dcbgaus = fit_signal(w, "dcbgaus", "test6",  signal_tree, var_name, 100, 110, 150, "1")


plot_3gaus.dataset.plotOn(frame, ROOT.RooFit.Name('dataset'))

plot_2gaus.fit.plotOn(frame, ROOT.RooFit.Range("full"), ROOT.RooFit.Name(plot_2gaus.name),ROOT.RooFit.LineColor(ROOT.kBlack))
plot_3gaus.fit.plotOn(frame, ROOT.RooFit.Range("full"), ROOT.RooFit.Name(plot_3gaus.name),ROOT.RooFit.LineColor(ROOT.kRed))
plot_3gausNuis.fit.plotOn(frame, ROOT.RooFit.Range("full"), ROOT.RooFit.Name(plot_3gausNuis.name),ROOT.RooFit.LineColor(ROOT.kOrange))
plot_cb.fit.plotOn(frame, ROOT.RooFit.Range("full"), ROOT.RooFit.Name(plot_cb.name),ROOT.RooFit.LineColor(ROOT.kYellow))
plot_dcb.fit.plotOn(frame, ROOT.RooFit.Range("full"), ROOT.RooFit.Name(plot_dcb.name),ROOT.RooFit.LineColor(ROOT.kGreen))
plot_cbgaus.fit.plotOn(frame, ROOT.RooFit.Range("full"), ROOT.RooFit.Name(plot_cbgaus.name),ROOT.RooFit.LineColor(ROOT.kCyan))
plot_dcbgaus.fit.plotOn(frame, ROOT.RooFit.Range("full"), ROOT.RooFit.Name(plot_dcbgaus.name),ROOT.RooFit.LineColor(ROOT.kBlue))

canvas = ROOT.TCanvas("test","test", 800, 800)
canvas.cd()

# frame.addObject(plot_3gaus.chi2_label)
frame.Draw()

# statbox = plot_3gaus.fit.paramOn(frame, ROOT.RooFit.Layout(0.1, 0.4, 0.9))
# statbox.Draw("same")

canvas.SaveAs("%s/test.root"%(args.output_path))
canvas.SaveAs("%s/test.png"%(args.output_path))