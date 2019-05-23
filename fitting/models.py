import os
import ROOT
Import = getattr(ROOT.RooWorkspace, 'import')

class FitFunction(object):
    def __init__(self, name, function, ndof):
        self.name = name
        self.ndof = ndof
        self.function = function


def fit_func_2gaus(w, label, model_name, var_name):
    w.factory("%s_mix1 [0.5, 0.0, 1.0]"%label)
    mix1 = w.var("%s_mix1"%label)
    w.factory("Gaussian::%s_gaus1(%s, %s_mean1[125., 120., 130.], %s_width1[1.0, 0.5, 5.0])"%(label, var_name, label, label))
    w.factory("Gaussian::%s_gaus2(%s, %s_mean2[125., 120., 130.], %s_width2[5.0, 2.0, 10.])"%(label, var_name, label, label))
    gaus1 = w.pdf('%s_gaus1'%(label))
    gaus2 = w.pdf('%s_gaus2'%(label))
    smodel = ROOT.RooAddPdf(model_name, model_name, ROOT.RooArgList(gaus1, gaus2) , ROOT.RooArgList(mix1), ROOT.kTRUE)
    param_list = ["%s_mean1"%label, "%s_mean2"%label, "%s_width1"%label, "%s_width2"%label, "%s_mix1"%label]
    Import(w, smodel)
    return w, param_list

def fit_func_3gaus(w, label, model_name, var_name):
    w.factory("%s_mix1 [0.5, 0.0, 1.0]"%label)
    w.factory("%s_mix2 [0., 0.0, 1.0]"%label)
    mix1 = w.var("%s_mix1"%label)
    mix2 = w.var("%s_mix2"%label)
    w.factory("Gaussian::%s_gaus1(%s, %s_mean1[125., 120., 130.], %s_width1[1.0, 0.5, 5.0])"%(label, var_name, label, label))
    w.factory("Gaussian::%s_gaus2(%s, %s_mean2[125., 120., 130.], %s_width2[5.0, 2.0, 10.])"%(label, var_name, label, label))
    w.factory("Gaussian::%s_gaus3(%s, %s_mean3[125., 120., 130.], %s_width3[5.0, 1.0, 10.])"%(label, var_name, label, label))
    gaus1 = w.pdf('%s_gaus1'%(label))
    gaus2 = w.pdf('%s_gaus2'%(label))
    gaus3 = w.pdf('%s_gaus3'%(label))
    smodel = ROOT.RooAddPdf(model_name, model_name, ROOT.RooArgList(gaus1, gaus2, gaus3) , ROOT.RooArgList(mix1, mix2), ROOT.kTRUE)
    param_list = ["%s_mean1"%label, "%s_mean2"%label, "%s_mean3"%label, "%s_width1"%label, "%s_width2"%label, "%s_width3"%label, "%s_mix1"%label, "%s_mix2"%label]
    Import(w, smodel)
    return w, param_list


def fit_func_3gausNuis(w, label, model_name, var_name):

    w.factory("%s_mix1 [0.5, 0.0, 1.0]"%label)
    w.factory("%s_mix2 [0., 0.0, 1.0]"%label)

    w.factory("mu_res_beta [0, 0, 0]")
    w.factory("mu_scale_beta [0, 0, 0]")

    w.factory("mu_res_unc [0.1, 0.1, 0.1]")
    w.factory("mu_scale_unc [0.0005, 0.0005, 0.0005]")

    w.var("mu_res_unc").setConstant(True)
    w.var("mu_scale_unc").setConstant(True)

    mix1 = w.var("%s_mix1"%label)
    mix2 = w.var("%s_mix2"%label)

    w.factory("EXPR::%s_mean1_times_nuis('%s_mean1*(1 + mu_scale_unc*mu_scale_beta)',{%s_mean1[125.0, 120., 130.],mu_scale_unc,mu_scale_beta})"%(label,label,label))
    w.factory("EXPR::%s_mean2_times_nuis('%s_mean2*(1 + mu_scale_unc*mu_scale_beta)',{%s_mean2[125.0, 120., 130.],mu_scale_unc,mu_scale_beta})"%(label,label,label))
    w.factory("EXPR::%s_mean3_times_nuis('%s_mean3*(1 + mu_scale_unc*mu_scale_beta)',{%s_mean3[125.0, 120., 130.],mu_scale_unc,mu_scale_beta})"%(label,label,label))

    w.factory("expr::%s_deltaM21('%s_mean2-%s_mean1',{%s_mean2, %s_mean1})"%(label,label,label,label,label))
    w.factory("expr::%s_deltaM31('%s_mean3-%s_mean1',{%s_mean3, %s_mean1})"%(label,label,label,label,label))

    w.factory("EXPR::%s_mean2_final('%s_mean2_times_nuis + mu_res_unc*mu_res_beta*%s_deltaM21',{%s_mean2_times_nuis, mu_res_unc, mu_res_beta, %s_deltaM21})"%(label,label,label,label,label))
    w.factory("EXPR::%s_mean3_final('%s_mean3_times_nuis + mu_res_unc*mu_res_beta*%s_deltaM31',{%s_mean3_times_nuis, mu_res_unc, mu_res_beta, %s_deltaM31})"%(label,label,label,label,label))

    w.factory("EXPR::%s_width1_times_nuis('%s_width1*(1 + mu_res_unc*mu_res_beta)',{%s_width1[1.0, 0.5, 5.0],mu_res_unc, mu_res_beta})"%(label,label,label))
    w.factory("EXPR::%s_width2_times_nuis('%s_width2*(1 + mu_res_unc*mu_res_beta)',{%s_width2[5.0, 2.0, 10.],mu_res_unc, mu_res_beta})"%(label,label,label))
    w.factory("EXPR::%s_width3_times_nuis('%s_width3*(1 + mu_res_unc*mu_res_beta)',{%s_width3[5.0, 1.0, 10.],mu_res_unc, mu_res_beta})"%(label,label,label))

    w.factory("Gaussian::%s_gaus1(%s, %s_mean1_times_nuis, %s_width1_times_nuis)"%(label, var_name, label, label))
    w.factory("Gaussian::%s_gaus2(%s, %s_mean2_final, %s_width2_times_nuis)"%(label, var_name, label, label))
    w.factory("Gaussian::%s_gaus3(%s, %s_mean3_final, %s_width3_times_nuis)"%(label, var_name, label, label))


    gaus1 = w.pdf('%s_gaus1'%(label))
    gaus2 = w.pdf('%s_gaus2'%(label))
    gaus3 = w.pdf('%s_gaus3'%(label))

    smodel = ROOT.RooAddPdf(model_name, model_name, ROOT.RooArgList(gaus1, gaus2, gaus3) , ROOT.RooArgList(mix1, mix2), ROOT.kTRUE)

    param_list = ["%s_mean1"%label, "%s_mean2"%label, "%s_mean3"%label, "%s_width1"%label, "%s_width2"%label, "%s_width3"%label, "%s_mix1"%label, "%s_mix2"%label]
    Import(w, smodel)
    return w, param_list


def fit_func_cb(w, label, model_name, var_name):
    w.factory("RooCBShape::%s(%s, %s_mean[125,120,130], %s_sigma[2,0,5], %s_alpha[2,0,25], %s_n[1.5,0,25])"%(model_name, var_name, label,label,label,label))
    param_list = ["%s_mean"%label, "%s_sigma"%label, "%s_alpha"%label, "%s_n"%label]
    return w, param_list

def fit_func_dcb(w, label, model_name, var_name):
    fw_path = os.environ['FRAMEWORK_PATH']
    ROOT.gSystem.Load("%s/lib/RooDCBShape_cxx.so"%fw_path)
    w.factory("RooDCBShape::%s(%s, %s_mean[125,120,130], %s_sigma[2,0,5], %s_alphaL[2,0,25] , %s_alphaR[2,0,25], %s_nL[1.5,0,25], %s_nR[1.5,0,25])"%(model_name, var_name, label,label,label,label,label,label))
    param_list = ["%s_mean"%label, "%s_sigma"%label, "%s_alphaL"%label, "%s_alphaR"%label, "%s_nL"%label, "%s_nR"%label]
    return w, param_list

def fit_func_cbgaus(w, label, model_name, var_name):
    w.factory("RooCBShape::%s_cb(%s, %s_mean[125,120,130], %s_sigma[2,0,5], %s_alpha[2,0,25], %s_n[1.5,0,25])"%(label, var_name, label,label,label,label))
    w.factory("Gaussian::%s_gaus(%s, %s_mean_gaus[125., 120., 130.], %s_width_gaus[2.0, 0, 20])"%(label,var_name, label, label))
    mix = ROOT.RooRealVar("%s_mix"%label,  "%s_mix"%label, 0.5,0.,1.)
    cb = w.pdf('%s_cb'%label)
    gaus = w.pdf('%s_gaus'%label)
    smodel = ROOT.RooAddPdf(model_name, model_name, cb, gaus, mix)
    Import(w, smodel)
    param_list = ["%s_mean"%label, "%s_sigma"%label, "%s_alpha"%label, "%s_n"%label, "%s_mean_gaus"%label, "%s_width_gaus"%label, "%s_mix"%label]
    return w, param_list
   
def fit_func_dcbgaus(w, label, model_name, var_name):
    fw_path = os.environ['FRAMEWORK_PATH']
    ROOT.gSystem.Load("%s/lib/RooDCBShape_cxx.so"%fw_path)
    w.factory("RooDCBShape::%s_dcb(%s, %s_mean[125,120,130], %s_sigma[2,0,5], %s_alphaL[2,0,25] , %s_alphaR[2,0,25], %s_nL[1.5,0,25], %s_nR[1.5,0,25])"%(label, var_name, label,label,label,label,label,label))
    w.factory("Gaussian::%s_gaus(%s, %s_mean_gaus[125., 120., 130.], %s_width_gaus[2.0, 0, 20])"%(label,var_name, label, label))
    mix = ROOT.RooRealVar("%s_mix"%label,  "%s_mix"%label, 0.5,0.,1.)
    dcb = w.pdf('%s_dcb'%label)
    gaus = w.pdf('%s_gaus'%label)
    smodel = ROOT.RooAddPdf(model_name, model_name, dcb, gaus, mix)
    Import(w, smodel)
    param_list = ["%s_mean"%label, "%s_sigma"%label, "%s_alphaL"%label, "%s_alphaR"%label, "%s_nL"%label, "%s_nR"%label, "%s_mean_gaus"%label, "%s_width_gaus"%label, "%s_mix"%label]
    return w, param_list


_2gaus = FitFunction('2gaus', fit_func_2gaus, 5)
_3gaus = FitFunction('3gaus', fit_func_3gaus, 8)
_3gausNuis = FitFunction('3gausNuis', fit_func_3gausNuis, 8)
_cb = FitFunction('cb', fit_func_cb, 4)
_dcb = FitFunction('dcb', fit_func_dcb, 6)
_cbgaus = FitFunction('cbgaus', fit_func_cbgaus, 7)
_dcbgaus = FitFunction('dcbgaus', fit_func_dcbgaus, 9)

fit_functions = {
	'2gaus': _2gaus,
    '3gaus': _3gaus,
    '3gausNuis': _3gausNuis,
    'cb': _cb,    
    'dcb': _dcb,
    'cbgaus': _cbgaus,
    'dcbgaus': _dcbgaus,    
}