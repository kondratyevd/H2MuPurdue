#!/bin/sh

FRAMEWORK_PATH=/Users/dmitrykondratyev/Documents/HiggsToMuMu/H2MuPurdue/
echo 'Setting the framework path to ' $FRAMEWORK_PATH
MVA_OUTPUT_PATH=/Users/dmitrykondratyev/ML_output/
echo 'Setting the MVA output path to ' $MVA_OUTPUT_PATH

cd $FRAMEWORK_PATH/lib
root -l -q RooDCBShape.cxx++
cd $FRAMEWORK_PATH

export FRAMEWORK_PATH
export MVA_OUTPUT_PATH