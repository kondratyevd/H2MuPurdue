#!/bin/sh

FRAMEWORK_PATH=/home/dkondra/H2MuPurdue/
echo 'Setting the framework path to ' $FRAMEWORK_PATH
MVA_OUTPUT_PATH=/tmp/dkondra/ML_output/
echo 'Setting the MVA output path to ' $MVA_OUTPUT_PATH

. /cvmfs/cms.cern.ch/cmsset_default.sh
cd /cvmfs/cms.cern.ch/slc7_amd64_gcc630/cms/cmssw/CMSSW_10_2_0/src/
cmsenv
cd $FRAMEWORK_PATH

export FRAMEWORK_PATH
export MVA_OUTPUT_PATH