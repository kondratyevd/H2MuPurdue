import os, sys, errno
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
from array import array
import lib.includes

import ROOT
from ROOT import gSystem
from config.variables import variables


ROOT.gStyle.SetOptStat(0)

        
class NTuplePlotter(object):
    def __init__(self):
        print "#"*70
        self.out_dir = "plots/"
        self.tree_path = 'dimuons/tree'
        self.has_metadata = True
        self.metadata_path = 'dimuons/metadata'
        self.selection = '1'
        self.jet_selection = '1'
        self.wgt_sf = "1"

        self.var_list =[]

        self.has_data = False
        self.data_samples = []
        self.data_hist_dict = {}
        self.data_title = ''
        self.lumi = 0
        
        self.has_mc = False
        self.source_list = []
        self.signal_list = []

        self.scale_mc_to_data = False
        self.log_y = False

        self.style = self.Style()
        
################################################# Input ##################################################

    def add_data_file(self, title, path, lumi):
        self.has_data = True
        self.lumi = self.lumi + lumi
        self.data_title = "Data"
        self.data_samples.append([title,path])
        print "Data imported from "+path

    def add_data_dir(self, title, path, lumi):
        self.has_data = True
        self.lumi = self.lumi + lumi
        self.data_title = "Data"
        if "*" not in path:
            self.data_samples.append([title,path+"/*root"])
        print "Data imported from "+path

    def add_source(self, name, color):
        src = self.Source(self, name, color, False)
        self.source_list.append(src)
        return src

    def add_signal(self, name, color):
        src = self.Source(self, name, color, True)
        self.signal_list.append(src)
        return src

    def add_variable(self, name, nObj):
        if name not in [v.name for v in variables]:
            sys.exit("\n\nERROR: Variable %s not found in the list.\n"%(name))
        else:
            for var in variables:
                if var.name == name:                                    
                    print "Adding input variable %s  [%i]"%(name, nObj)
                    var.itemsAdded = nObj
                    # self.nVar = self.nVar + nObj
                    self.var_list.append(var) 
        # var = self.Variable(name, title, nBins, xmin, xmax, units, '', 1, False)
        # self.var_list.append(var)
        # print "Variable %s added.."%name

    def add_multidim_var(self, name, leaf, N, title, nBins, xmin, xmax, units ):
        var = self.Variable(name, title, nBins, xmin, xmax, units, leaf, N, True)
        self.var_list.append(var)
        print "Variable %s added.."%name

    def add_selection(self, selection):
        self.selection = selection
        print "Selection: %s"%selection

    def add_jet_selection(self, jet_selection):
        self.jet_selection = jet_selection
        print "Jet selection: %s"%jet_selection

    def add_wgt_sf(self, wgt_sf):
        self.wgt_sf = wgt_sf
        print "Weights and SF: %s"%wgt_sf

############################################## Configuration ###############################################

    def set_out_dir(self, path):
        self.out_dir = path
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        try:
            os.makedirs(path+"root/")
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise    

    def set_lumi(self, lumi):
        self.lumi = lumi

    def setLogY(self):
        self.log_y = True

############################################### Compilation ################################################

    def compile_data(self):    #get histograms for data
        print "\n"+"#"*35
        print "#    Compiling data"
        print "#"*35

        for var in self.var_list:  
            if var.isMultiDim:
                for j in range(var.itemsAdded):
                    var_name_multi = "%s[%i]"%(var.name, j)
                    self.data_hist_dict[var_name_multi] = ROOT.TH1D("Data_hist_"+var_name_multi, self.data_title, var.nBins, var.min, var.max)
                    self.data_hist_dict[var_name_multi].Sumw2()
            else:  
                self.data_hist_dict[var.name] = ROOT.TH1D("Data_hist_"+var.name, self.data_title, var.nBins, var.min, var.max)
                self.data_hist_dict[var.name].Sumw2()

        self.data_title = "Data %i /pb"%self.lumi
        print "Total lumi: %i /pb\n"%self.lumi 

        for smp in self.data_samples:
            if self.has_metadata:
                metadata = ROOT.TChain(self.metadata_path)
                metadata.Add(smp[1])
                nEvt = self.get_nEvts(metadata, "Data", weighted = False)

            for var in self.var_list:
                if var.isMultiDim:
                    for j in range(var.itemsAdded):
                        var_name_multi = "%s[%i]"%(var.name, j)
                        tree = ROOT.TChain(self.tree_path)
                        tree.Add(smp[1])
                        hist_name = "Data_"+var_name_multi+"_"+smp[0]
                        new_hist = ROOT.TH1D(hist_name, self.data_title, var.nBins, var.min, var.max)
                        new_hist.Sumw2()

                        selection = self.selection                           

                        if "mass_Roch" in var_name_multi:
                            selection = "(%s)&(muPairs.mass_Roch<120 || muPairs.mass_Roch>130)"%self.selection
        
                        tree.Draw(var_name_multi+">>"+hist_name, selection)

                        self.data_hist_dict[var_name_multi].Add(new_hist, 1)    # fill histograms
                        print "            Variable: %15s        Integral = %f"%(var_name_multi, new_hist.GetSumOfWeights())
                else:
                    tree = ROOT.TChain(self.tree_path)
                    tree.Add(smp[1])
                    hist_name = "Data_"+var.name+"_"+smp[0]
                    new_hist = ROOT.TH1D(hist_name, self.data_title, var.nBins, var.min, var.max)
                    new_hist.Sumw2()

                    selection = self.selection 

                    if "mass_Roch" in var.name:
                        selection = "(%s)&(muPairs.mass_Roch<120 || muPairs.mass_Roch>130)"%self.selection
                    if "mll" in var.name:
                        selection = "(%s)&(mll<120 || mll>130)"%self.selection
    
                    tree.Draw(var.name+">>"+hist_name, selection)
                    self.data_hist_dict[var.name].Add(new_hist, 1)    # fill histograms
                    print "            Variable: %15s        Integral = %f"%(var.name, new_hist.GetSumOfWeights())

    def compile_mc(self):    # get histograms for MC
        for src in self.source_list + self.signal_list:
            src.compile()    # see definition of class 'Source'
            del src


    def selection_is_ok(self, tree):
        muon1_pt = tree.FindBranch("muons.pt").FindLeaf("pt").GetValue(0)
        muon2_pt = tree.FindBranch("muons.pt").FindLeaf("pt").GetValue(1)
        muon1_hlt2 = tree.FindBranch("muons.isHltMatched").FindLeaf("isHltMatched").GetValue(2)
        muon1_hlt3 = tree.FindBranch("muons.isHltMatched").FindLeaf("isHltMatched").GetValue(3)
        muon2_hlt2 = tree.FindBranch("muons.isHltMatched").FindLeaf("isHltMatched").GetValue(8)
        muon2_hlt3 = tree.FindBranch("muons.isHltMatched").FindLeaf("isHltMatched").GetValue(9)
        muon1_ID = tree.FindBranch("muons.isMediumID").FindLeaf("isMediumID").GetValue(0)
        muon2_ID = tree.FindBranch("muons.isMediumID").FindLeaf("isMediumID").GetValue(1)
        muPair_mass = tree.FindBranch("muPairs.mass_Roch").FindLeaf("mass_Roch").GetValue()
        nJets = tree.FindBranch("nJets").FindLeaf("nJets").GetValue()
        nJetPairs = tree.FindBranch("nJetPairs").FindLeaf("nJetPairs").GetValue()
        flag = ((muPair_mass>12)&
                (muon1_ID>0)&
                (muon2_ID>0)&
                (muon1_pt>20)&
                (muon2_pt>20)&
                (
                    ( muon1_pt > 30 & (muon1_hlt2>0 or muon1_hlt3>0) ) 
                or
                    ( muon2_pt > 30 & (muon2_hlt2>0 or muon2_hlt3>0) )
                ))

        return flag 


# #  After TChain.Add() we have histograms 'sumEventWeights' and 'originalNumEvents' 
# #  which store number of original events or weights for each added tuple.
# #  Instead, we need the sum of events or weights of all tuples in the chain.

    def get_nEvts(self, metadata, name, weighted):    

        ROOT.gROOT.SetBatch(1)    
        if weighted:
            label = 'sumEventWeights'
        else:
            label = 'originalNumEvents' 

        dummy = ROOT.TCanvas("dummmy","dummy",100,100)
        metadata.Draw(label+">>evts_"+name)
        hist = ROOT.gDirectory.Get("evts_"+name)
        nEvts = hist.GetMean()*hist.GetEntries()    #    mean * entries = (sum / entries) * entries = sum
        dummy.Close()
        return nEvts

################################################# Plotting ##################################################

    def plot_stack(self):

        if self.has_data:
            self.compile_data()

        else:
            print "No data found, setting lumi to 40000 /pb"
            self.lumi = 40000

        if self.has_mc:
            self.compile_mc()
        else:
            print "No MC found."

        for var in self.var_list:      
            if var.isMultiDim:
                for j in range(var.itemsAdded):
                    self.make_stack_plots(var, "%s[%i]"%(var.name, j))
            else:
                self.make_stack_plots(var, var.name)


    def make_stack_plots(self, var, name):

        #---------------- Initialize  ----------------#
    
        legend = ROOT.TLegend(.63,.6,.86,.89)
        legend.SetFillStyle(1001)
        legend.SetBorderSize(0)
    
        legend_s = ROOT.TLegend(.5,.75,.63,.89)
        legend_s.SetFillStyle(1001)
        legend_s.SetBorderSize(0)
    
        if self.has_mc:
            ratio = None
            mcErr = None
            hist_list = []
            mc_total_hist = ROOT.TH1D("master_"+name, name, var.nBins, var.min, var.max)
            mc_total_hist.Sumw2()
            stack = ROOT.THStack()
    
            #---------------- Fill additional histograms  ----------------#
    
            if self.has_data and self.scale_mc_to_data:         # scale MC integral to data
                for src in self.signal_list:
                    hist_list.append(src.hist_dict[name])
                    mc_total_hist.Add(src.hist_dict[name],1)
                    legend.AddEntry(src.hist_dict[name], src.name, "l")
                for src in self.source_list:
                    hist_list.append(src.hist_dict[name])
                    mc_total_hist.Add(src.hist_dict[name],1)
                    legend.AddEntry(src.hist_dict[name], src.name, "f")
                for src in self.source_list:
                    src.hist_dict[name].Scale(self.data_hist_dict[name].Integral()/mc_total_hist.Integral()) # scale to data
                    stack.Add(src.hist_dict[name])
                mc_total_hist.Scale(self.data_hist_dict[name].Integral()/mc_total_hist.Integral())
                ratio, mcErr = self.draw_ratio(self.data_hist_dict[name],mc_total_hist, var)
    
            else:                                        # not scaling to data: real MC normalization
                for src in self.signal_list:
                    hist_list.append(src.hist_dict[name])
                    mc_total_hist.Add(src.hist_dict[name],1)
                    legend_s.AddEntry(src.hist_dict[name], src.name, "l")
                for src in self.source_list:        
                    hist_list.append(src.hist_dict[name])
                    mc_total_hist.Add(src.hist_dict[name],1)
                    legend.AddEntry(src.hist_dict[name], src.name, "f")
                    stack.Add(src.hist_dict[name])
                if self.has_data:
                    ratio, mcErr = self.draw_ratio(self.data_hist_dict[name],mc_total_hist, var)
    
        #--------------------------- Draw  ---------------------------#            
    
        canvas = ROOT.TCanvas("canvas", "canvas", 800, 880)
        canvas.cd()
    
        if self.has_data and self.has_mc:                                # make pads for plot and ratio
            pad1 = ROOT.TPad("pad1","",0,0.25,1,1.0)
            pad2 = ROOT.TPad("pad2","",0,0.05,1,0.25)
            pad1.Draw()
            pad1.cd()
            self.style.apply(stackPad = pad1)
            legend.AddEntry(self.data_hist_dict[name], self.data_title, "pe")
    
        if self.has_mc:                                                # plot MC stack
            legend.AddEntry(mc_total_hist, "MC stat. err.", "f")
            stack.Draw("hist")
            for src in self.signal_list:
                src.hist_dict[name].Draw("samehist")
            mc_total_hist.Draw("samee2")
            self.style.apply(mcStack = stack, mcTotalHist = mc_total_hist, hist_list = hist_list, log_y = self.log_y)
        
        if self.has_data:                                            # plot data points
            self.data_hist_dict[name].Draw("samepe")
            self.style.apply(dataHist = self.data_hist_dict[name])        
    
        if self.log_y:
            ROOT.gPad.SetLogy()
    
        if self.has_data and self.has_mc:                                # plot ratio    
            canvas.cd()
            pad2.Draw()
            pad2.cd()
            self.style.apply(ratioPad = pad2)
            ratio.Draw("ape1")
            mcErr.Draw('samee2')    
            self.style.apply(ratioHist = ratio, ratioErrHist = mcErr, var = var)
            pad2.SetTicks()
            pad2.Update()
            pad1.cd()
    
            print "\n"+"#"*35
            print '# %s:'%name
            print "#    Data / MC = %f"%(self.data_hist_dict[name].Integral() / mc_total_hist.Integral())
            print '#'
            print "#"*35
    
        legend.Draw()
        legend_s.Draw()
        canvas.Print(self.out_dir+name+".png")
        canvas.SaveAs(self.out_dir+"root/"+name+".root")
        canvas.Close()


    def draw_ratio(self,numHist,denHist, var):

        x  = array('d')
        y  = array('d')
        ex = array('d')
        ey = array('d')
        y_mcErr = array('d')
        ey_mcErr = array('d')

        binWidth = (var.max - var.min) / float(var.nBins)

        for i in range(var.nBins):

            numVal = numHist.GetBinContent(i+1)+0.0000001
            numErr = numHist.GetBinError(i+1)
            denVal = denHist.GetBinContent(i+1)+0.0000001
            denErr = denHist.GetBinError(i+1)

            xVal = var.min+(i+0.5)*binWidth
            ratioVal = numVal/denVal
            ratioErr = numErr/denVal

            x.append(xVal)
            y.append(ratioVal)
            ex.append(binWidth/2)
            ey.append(ratioErr)

            y_mcErr.append(1)
            ey_mcErr.append(denErr/denVal)

        ROOT.gStyle.SetGridStyle(1)
        ratioPlot = ROOT.TGraphErrors(var.nBins, x, y, ex, ey)
        mcErr = ROOT.TGraphErrors(var.nBins, x, y_mcErr, ex, ey_mcErr)

        return ratioPlot, mcErr

    def plot_shapes(self):

        self.compile_mc(False)

        for var in self.var_list:

            #---------------- Initialize  ----------------#
            
            legend = ROOT.TLegend(.63,.6,.86,.89)
            legend.SetFillStyle(1001)
            legend.SetBorderSize(0)

            #--------------------------- Draw  ---------------------------#            

            canvas = ROOT.TCanvas("canvas", "canvas", 800, 880)
            canvas.cd()

            mx = 0

            for src in self.signal_list+self.source_list:              
                src.hist_dict[var.name].Scale(1/src.hist_dict[var.name].Integral())
                new_mx = src.hist_dict[var.name].GetBinContent(src.hist_dict[var.name].GetMaximumBin())
                if new_mx > mx:
                    mx = new_mx

            for src in self.signal_list+self.source_list:
                
                src.hist_dict[var.name].SetLineColor(src.hist_dict[var.name].GetFillColor())
                src.hist_dict[var.name].SetLineWidth(2)
                src.hist_dict[var.name].SetFillStyle(3003)
                src.hist_dict[var.name].SetTitle('')
                src.hist_dict[var.name].SetMaximum(mx*1.1)
                src.hist_dict[var.name].GetXaxis().SetTitle(var.title)
                src.hist_dict[var.name].Draw("samehist")
                legend.AddEntry(src.hist_dict[var.name], src.name, "l")
            legend.Draw()

            try:
                os.makedirs(self.out_dir+"/shapes/")
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

            canvas.Print(self.out_dir+"/shapes/"+var.name+".png")
            canvas.SaveAs(self.out_dir+"root/"+var.name+".root")
            canvas.Close()


################################################# Classes ##################################################

    class Source(object):

        def __init__(self, framework, name, color, isSignal):
            self.framework = framework
            self.name = name
            self.color = color
            self.sample_list = []
            self.hist = None
            self.hist_dict = {}
            self.sumOfWeights = 0
            self.isSignal = isSignal

        def get_file(self, name, path, xSec):
            self.sample_list.append(self.SampleMC(self.framework, self, name, path, xSec))
            print "%s added as %s.."%(name, self.name)
            self.framework.has_mc = True

        def get_dir(self, name, path, xSec):
            self.sample_list.append(self.SampleMC(self.framework, self, name, path+"/*root", xSec))
            print "%s added as %s.."%(name, self.name)
            self.framework.has_mc = True

        def compile(self):

            print '\n'+"#"*35
            print "# Source: "+self.name
            print "#"*35
            print "        "+"-"*70

            for var in self.framework.var_list:
                if var.isMultiDim:
                    for j in range(var.itemsAdded):
                        var_name_multi = "%s[%i]"%(var.name, j)
                        self.hist_dict[var_name_multi] = ROOT.TH1D(self.name+"_"+var_name_multi, self.name+" #%i"%j, var.nBins, var.min, var.max)
                        self.hist_dict[var_name_multi].Sumw2() 
                else:    
                    self.hist_dict[var.name] = ROOT.TH1D(self.name+"_"+var.name, self.name, var.nBins, var.min, var.max)
                    self.hist_dict[var.name].Sumw2()

            for smp in self.sample_list:
                smp.get_histos(self.framework.wgt_sf, self.hist_dict)

        class SampleMC(object):

            def __init__(self, framework, source, name, path, xSec):
                self.framework = framework
                self.source = source
                self.name = name
                self.path = path
                self.xSec = xSec
                self.weight = 1
                self.nEvt = 1
                self.nOriginalWeighted = 1
                self.lumi_wgt = 1
                tree = ROOT.TChain()
    
            def get_histos(self, weights, hist_dict): # get MC histograms
                ROOT.gROOT.SetBatch(ROOT.kTRUE)

                tree = ROOT.TChain(self.framework.tree_path)
                tree.Add(self.path)
                if self.framework.has_metadata:
                    metadata = ROOT.TChain(self.framework.metadata_path)
                    metadata.Add(self.path)

                    self.nOriginalWeighted = self.framework.get_nEvts(metadata, self.name, weighted = True)
                    self.lumi_wgt = self.xSec*self.framework.lumi/self.nOriginalWeighted

                    print "        Compiling sample: %15s    Sum of weights: %10i"%(self.name, self.nOriginalWeighted)
                    print "        Lumi weight: %f"%self.lumi_wgt
                    print "        "+"-"*35
                else:
                    print "        Compiling sample: %15s"%(self.name)
                    print "        "+"-"*35

                for var in self.framework.var_list:
                    if var.isMultiDim:
                        for j in range(var.itemsAdded):
                            var_name_multi = "%s[%i]"%(var.name, j)

                            if "mass_res" in var_name_multi:
                                self.new_hist = self.framework.ebe_calib(tree, self.name+"_"+var_name_multi, self.name, var_name_multi, var.nBins, var.min, var.max, self.framework.selection, weights)
                                self.new_hist.Sumw2()
                                hist_dict[var_name_multi].Add(self.new_hist, self.lumi_wgt)
                                self.framework.style.apply(mcHist = hist_dict[var_name_multi], color = self.source.color, isSignal = self.source.isSignal)
                            else:
                                dummy = ROOT.TCanvas("dummmy_%s_%s"%(self.name, var_name_multi),"dummy_%s_%s"%(self.name, var_name_multi),100,100)
                                dummy.cd()
                                dummy.SetBatch(ROOT.kTRUE)
                                hist_name = self.name+"_"+var_name_multi
                                
                                self.new_hist = ROOT.TH1D(hist_name, self.name, var.nBins, var.min, var.max)
                                self.new_hist.Sumw2()
                
                                tree.Draw(var_name_multi+">>"+hist_name, "(%s)*(%s)"%(self.framework.selection, weights))
                
                                hist_dict[var_name_multi].Add(self.new_hist, self.lumi_wgt)
                                self.framework.style.apply(mcHist = hist_dict[var_name_multi], color = self.source.color, isSignal = self.source.isSignal)
                                dummy.Close()

                            print self.new_hist.GetSumOfWeights()
                            print "            Variable: %15s        Integral = %f"%(var_name_multi, self.new_hist.GetSumOfWeights()*self.lumi_wgt)

                    else:
                        if "mass_res" in var.name:
                            self.new_hist = self.framework.ebe_calib(tree, self.name+"_"+var.name, self.name, var.name, var.nBins, var.min, var.max, self.framework.selection, weights)
                            self.new_hist.Sumw2()
                            hist_dict[var_name_multi].Add(self.new_hist, self.lumi_wgt)
                            self.framework.style.apply(mcHist = hist_dict[var_name_multi], color = self.source.color, isSignal = self.source.isSignal)
                        else:
                            dummy = ROOT.TCanvas("dummmy_%s_%s"%(self.name, var.name),"dummy_%s_%s"%(self.name, var.name),100,100)
                            dummy.cd()
                            dummy.SetBatch(ROOT.kTRUE)
                            hist_name = self.name+"_"+var.name
                            
                            self.new_hist = ROOT.TH1D(hist_name, self.name, var.nBins, var.min, var.max)
                            self.new_hist.Sumw2()

                            tree.Draw(var.name+">>"+hist_name, "(%s)*(%s)"%(self.framework.selection, weights))

                            hist_dict[var.name].Add(self.new_hist, self.lumi_wgt)
                            self.framework.style.apply(mcHist = hist_dict[var.name], color = self.source.color, isSignal = self.source.isSignal)
                            dummy.Close()
                        print self.new_hist.GetSumOfWeights()
                        print "            Variable: %15s        Integral = %f"%(var.name, self.new_hist.GetSumOfWeights()*self.lumi_wgt)
                print "        "+"-"*70
                tree.Reset()
                tree.Delete()
                del tree

                    

################################################# Style ##################################################

    class Style(object):
        def __init__(self):
            pass
    
        def apply(self, mcHist = None, color = None, stackPad = None, mcStack = None, dataHist = None, mcTotalHist = None, ratioPad = None, ratioHist = None, ratioErrHist = None, hist_list = None, isSignal = False, var = None, log_y = False):
            if mcHist and color:
                self.style_mc_hist(mcHist, color, isSignal)
            if stackPad:
                self.style_stack_pad(stackPad)
            if mcStack and hist_list:
                self.style_mc_stack(mcStack, hist_list, log_y)
            if mcTotalHist:
                self.style_mc_total_hist(mcTotalHist)
            if dataHist:
                self.style_data_hist(dataHist)
            if ratioHist and var:
                self.style_ratio_hist(ratioHist, var)
            if ratioErrHist and var:
                self.style_ratio_err_hist(ratioErrHist, var)
            if ratioPad:
                self.style_ratio_pad(ratioPad)
    
        def style_mc_hist(self, hist, color, isSignal):
            if isSignal:
                hist.SetLineColor(color)
                hist.SetLineWidth(3)
            else:
                hist.SetFillColor(color)
                hist.SetFillStyle(1001)
                hist.SetLineColor(ROOT.kBlack)
                hist.SetLineWidth(2)

        def style_stack_pad(self, pad):
            pad.SetBottomMargin(0.03)
            pad.SetTicks()

        def style_mc_stack(self,stack, hist_list, log_y):
            stack.GetYaxis().SetTitle("Events / bin")
            stack.GetYaxis().SetTitleOffset(1.2)
            stack.GetXaxis().SetNdivisions(0)
            ymin = 0.01 if log_y else 0
            ymax_factor = 1000 if log_y else 1.1
            mx = max(hist_list, key=lambda hist: hist.GetBinContent(hist.GetMaximumBin()))
            stack.SetMinimum(ymin)
            stack.SetMaximum(mx.GetBinContent(mx.GetMaximumBin())*ymax_factor)    

        def style_mc_total_hist(self, hist):
            hist.SetFillStyle(3001)
            hist.SetFillColor(ROOT.kBlack)
            hist.SetMarkerSize(0)    

        def style_data_hist(self, hist):
            hist.SetMarkerStyle(20)
            hist.SetMarkerSize(0.9)
            hist.SetLineColor(ROOT.kBlack)

        def style_ratio_hist(self,hist,var):
            hist.GetYaxis().SetTitle("Data/MC")
            hist.GetXaxis().SetTitle(var.name+var.comma+var.units)
            hist.GetYaxis().SetTitleOffset(0.3)
            hist.SetMarkerStyle(20)
            hist.SetMarkerSize(.9)
            hist.SetMarkerColor(ROOT.kBlack)
            hist.GetXaxis().SetLabelSize(0.12)
            hist.GetXaxis().SetTitleSize(0.12)
            hist.GetYaxis().SetLabelSize(0.12)
            hist.GetYaxis().SetTitleSize(0.12)
            hist.GetYaxis().SetNdivisions(5)
            hist.GetXaxis().SetRangeUser(var.min, var.max)
            hist.SetMinimum(0.5)
            hist.SetMaximum(1.5)
            hist.SetTitle('')
    
        def style_ratio_err_hist(self,hist,var):
            hist.SetFillStyle(3001)
            hist.SetFillColor(ROOT.kBlack)
            hist.SetMarkerSize(0)

        def style_ratio_pad(self,pad):
            pad.SetGridx()
            pad.SetGridy()
            pad.SetTopMargin(0)
            pad.SetBottomMargin(0.25)
            pad.Update()

    def ebe_calib(self, tree, new_hist_name, smp_name, var_name, nBins, xmin, xmax, selection, weights):

        pt_bins = {
                   "pt_bin1": "(muons.pt[0]>30)&(muons.pt[0]<50)",
                   "pt_bin2": "(muons.pt[0]>50)"
                   }

        B1 = "(abs(muons.eta[0])<0.9)"
        B2 = "(abs(muons.eta[1])<0.9)"
        O1 = "(abs(muons.eta[0])>0.9)&(abs(muons.eta[0])<1.9)"
        O2 = "(abs(muons.eta[1])>0.9)&(abs(muons.eta[1])<1.9)"
        E1 = "(abs(muons.eta[0])>1.9)"
        E2 = "(abs(muons.eta[1])>1.9)"

        BB = "%s&%s"%(B1, B2)
        BO = "%s&%s"%(B1, O2)
        BE = "%s&%s"%(B1, E2)

        OB = "%s&%s"%(O1, B2)
        OO = "%s&%s"%(O1, O2)
        OE = "%s&%s"%(O1, E2)

        EB = "%s&%s"%(E1, B2)
        EO = "%s&%s"%(E1, O2)
        EE = "%s&%s"%(E1, E2)

        eta_bins = { "BB": BB,
                     "BO": BO,
                     "BE": BE,
                     "OB": OB,
                     "OO": OO,
                     "OE": OE,
                     "EB": EB,
                     "EO": EO,
                     "EE": EE
                     }

        # These factors are calculated from fit of Z-peak in 2017 data and DY
        factors = {'pt_bin2_EB': 1.0013319478357219,
                 'pt_bin1_OO': 1.0023693878056639,
                 'pt_bin1_BO': 1.0218129532550582,
                 'pt_bin2_EE': 0.9765938713567794,
                 'pt_bin1_BB': 1.0323464800005375,
                 'pt_bin2_EO': 1.0018350428217986,
                 'pt_bin1_BE': 1.0082951486706067,
                 'pt_bin1_EO': 0.9978525407560304,
                 'pt_bin1_OE': 0.9965500080239412,
                 'pt_bin2_BE': 1.0003701332423942,
                 'pt_bin2_OO': 1.0137635235189486,
                 'pt_bin2_BB': 1.034563610596542,
                 'pt_bin2_BO': 0.9934484561232999,
                 'pt_bin2_OE': 0.9922489708563557,
                 'pt_bin1_EE': 0.9969964864616038,
                 'pt_bin1_OB': 1.0265579651723569,
                 'pt_bin1_EB': 0.9892302833112607,
                 'pt_bin2_OB': 0.9931856900102433}

        result = "0"

        calib_hists = {}

        new_hist = ROOT.TH1D(new_hist_name, smp_name, nBins, xmin, xmax)

        for eta_bin_key, eta_bin_cut in eta_bins.iteritems():
            for pt_bin_key, pt_bin_cut in pt_bins.iteritems():
                name = "%s_%s"%(pt_bin_key, eta_bin_key)
                cut = "(%s)&(%s)"%(pt_bin_cut, eta_bin_cut)
                hist_name = "hist_"+name
                calib_hists[name] = ROOT.TH1D(hist_name, hist_name, nBins, xmin, xmax)
                calib_hists[name].Sumw2()
                tree.Draw("(%s)*%f>>%s"%(var_name,factors[name],hist_name), "(%s)*(%s)*(%s)"%(selection, weights, cut))
                new_hist.Add(calib_hists[name])

        return new_hist

