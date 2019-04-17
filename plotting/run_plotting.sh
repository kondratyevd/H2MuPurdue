#!/bin/sh

PLOTTING_OUT_PATH=$FRAMEWORK_PATH/plotting/plots/test/ 
mkdir $PLOTTING_OUT_PATH
python $FRAMEWORK_PATH/plotting/scripts/test_hammer.py --out_path $PLOTTING_OUT_PATH
# python $FRAMEWORK_PATH/plotting/scripts/test_local.py --out_path $PLOTTING_OUT_PATH