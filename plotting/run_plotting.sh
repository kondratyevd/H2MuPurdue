#!/bin/sh

PLOTTING_OUT_PATH=$FRAMEWORK_PATH/plotting/plots/test_latinos_fitreg_uncorr/
# PLOTTING_OUT_PATH=$FRAMEWORK_PATH/plotting/plots/test_latinos_Zpeak_uncorr/ 
mkdir -p $PLOTTING_OUT_PATH
# python $FRAMEWORK_PATH/plotting/scripts/test_hammer.py --out_path $PLOTTING_OUT_PATH
python $FRAMEWORK_PATH/plotting/scripts/test_latinos.py --out_path $PLOTTING_OUT_PATH

# python $FRAMEWORK_PATH/plotting/scripts/test_local.py --out_path $PLOTTING_OUT_PATH