from models import *
import ROOT
Import = getattr(ROOT.RooWorkspace, 'import')

class SigFitOutput(object):
    def __init__(self, name, hist, dataset, fit, rate, chi2, chi2_label, frame):
        self.name = name
        self.rate = rate
        self.chi2 = chi2
        self.chi2_label = chi2_label        
        self.hist = hist
        self.dataset = dataset
        self.fit = fit
        self.frame = frame
        


def create_workspace(name, var_name, var_title, nBins,xmin, xmax):
    var = ROOT.RooRealVar(var_name,var_title,xmin,xmax)     
    var.setBins(nBins)
    var.setRange("full", xmin, xmax)
    w = ROOT.RooWorkspace(name, False)
    Import(w, var)
    return w

def fit_signal(w, fit_func_name, label, tree, var_name, nBins, xmin, xmax, cut):
    # trees = [["tree1name", "/path/to/file1.root"], ["tree2name", "/path/to/file2.root"], ..]
    lumi = 1
    var = w.var(var_name)
    var.setBins(5000)
    max_abs_eta_var = ROOT.RooRealVar("max_abs_eta_mu","Max abs(eta) of muons", 0, 2.4) 
    mu1_eta = ROOT.RooRealVar("mu1_eta","mu1_eta", -2.4, 2.4) 
    mu2_eta = ROOT.RooRealVar("mu2_eta","mu2_eta", -2.4, 2.4)

    ggh_pred_var = ROOT.RooRealVar("ggH_prediction", "ggH_prediction", 0, 1)
    vbf_pred_var = ROOT.RooRealVar("VBF_prediction", "VBF_prediction", 0, 1)
    dy_pred_var = ROOT.RooRealVar("DY_prediction", "DY_prediction", 0, 1)
    tt_pred_var = ROOT.RooRealVar("ttbar_prediction", "ttbar_prediction", 0, 1) 

    arg_set = ROOT.RooArgSet(var, max_abs_eta_var, mu1_eta, mu2_eta, ggh_pred_var, vbf_pred_var, dy_pred_var, tt_pred_var)
       
    signal_hist_name = "signal_%s"%label
    signal_hist = ROOT.TH1D(signal_hist_name, signal_hist_name, nBins, xmin, xmax)

    dummy = ROOT.TCanvas("dummy", "dummy", 800, 800)
    dummy.cd()
    tree.Draw("%s>>%s"%(var_name, signal_hist_name), "(%s)*weight_over_lumi*%s"%(cut, lumi))
    dummy.Close()
    signal_rate = signal_hist.Integral()

    model_name = '%s_%s'%(label, fit_func_name)
    ds_name = "ds_%s"%label

    fit_func = fit_functions[fit_func_name]
    w, param_list = fit_func.function(w, label, model_name, var_name)
    smodel = w.pdf(model_name)

    ds = ROOT.RooDataSet(ds_name, ds_name, tree, arg_set, cut)
    res = smodel.fitTo(ds, ROOT.RooFit.Range("full"),ROOT.RooFit.Save(), ROOT.RooFit.Verbose(False))
    res.Print()


    for par in param_list:
        par_var = w.var(par)
        par_var.setConstant(True)


    frame = var.frame(ROOT.RooFit.Bins(nBins))
    ds.plotOn(frame, ROOT.RooFit.Name(ds_name))
    smodel.plotOn(frame, ROOT.RooFit.Range("full"), ROOT.RooFit.Name(model_name),ROOT.RooFit.LineColor(ROOT.kRed))
    
    chi2 = frame.chiSquare(model_name, ds_name, fit_func.ndof) 

    chi2_label = ROOT.TPaveLabel(0.7,0.83,0.9,0.9, "#chi^{2}/dof = %.4f"%chi2,"brNDC")
    chi2_label.SetFillColor(0)
    chi2_label.SetTextSize(0.4)

    return SigFitOutput(model_name, signal_hist, ds, smodel, signal_rate, chi2, chi2_label, frame)






