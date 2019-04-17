import os
import ROOT
from ROOT import gInterpreter, gSystem


fw_path = os.environ['FRAMEWORK_PATH']
gInterpreter.ProcessLine(' #include "%s/lib/EventInfo.h"'%fw_path)
gInterpreter.ProcessLine(' #include "%s/lib/JetInfo.h"'%fw_path)
gInterpreter.ProcessLine(' #include "%s/lib/JetPairInfo.h"'%fw_path)
gInterpreter.ProcessLine(' #include "%s/lib/MetInfo.h"'%fw_path)
gInterpreter.ProcessLine(' #include "%s/lib/MuPairInfo.h"'%fw_path)
gInterpreter.ProcessLine(' #include "%s/lib/MuonInfo.h"'%fw_path)
gInterpreter.ProcessLine(' #include "%s/lib/VertexInfo.h"'%fw_path)

gInterpreter.ProcessLine(' #include "%s/lib/EleInfo.h"'%fw_path)
gInterpreter.ProcessLine(' #include "%s/lib/MhtInfo.h"'%fw_path)
gInterpreter.ProcessLine(' #include "%s/lib/GenParentInfo.h"'%fw_path)
gInterpreter.ProcessLine(' #include "%s/lib/GenMuonInfo.h"'%fw_path)
gInterpreter.ProcessLine(' #include "%s/lib/GenMuPairInfo.h"'%fw_path)

