#!/bin/sh

SCRIPT_PATH=$FRAMEWORK_PATH/plotting/scripts/test_latinos.py

case $1 in
	0.0)
		echo 'Running option 0.0: Zpeak, no ZpT reweighting'
		PLOTTING_OUT_PATH=$FRAMEWORK_PATH/plotting/plots/test_latinos_Zpeak_uncorr/ 
		ZPT=false
		MASS_MIN=70
		MASS_MAX=110
		;;

	0.1)
		echo 'Running option 0.1: Zpeak, ZpT reweighting'
		PLOTTING_OUT_PATH=$FRAMEWORK_PATH/plotting/plots/test_latinos_Zpeak_corr/ 
		ZPT=true
		MASS_MIN=70
		MASS_MAX=110
		;;

	1.0)
		echo 'Running option 1.0: fit region, no ZpT reweighting'
		PLOTTING_OUT_PATH=$FRAMEWORK_PATH/plotting/plots/test_latinos_fitreg_uncorr/ 
		ZPT=false
		MASS_MIN=110
		MASS_MAX=150
		;;

	1.1)
		echo 'Running option 1.1: fit region, ZpT reweighting'
		PLOTTING_OUT_PATH=$FRAMEWORK_PATH/plotting/plots/test_latinos_fitreg_corr/ 
		ZPT=true
		MASS_MIN=110
		MASS_MAX=150
		;;
	*)
		echo 'Wrong option ' $1		

esac

mkdir -p $PLOTTING_OUT_PATH

if $ZPT ; then
	python $SCRIPT_PATH --out_path $PLOTTING_OUT_PATH --zpt --mass_min $MASS_MIN --mass_max $MASS_MAX
else
	python $SCRIPT_PATH --out_path $PLOTTING_OUT_PATH --mass_min $MASS_MIN --mass_max $MASS_MAX
fi
