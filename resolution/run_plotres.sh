#!/bin/sh

PLOTRES_OUT_PATH=$FRAMEWORK_PATH/resolution/plots/test/ 
mkdir -p $PLOTRES_OUT_PATH
python $FRAMEWORK_PATH/resolution/plot_resolution.py --out_path $PLOTRES_OUT_PATH