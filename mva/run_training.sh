#!/bin/sh

timestamp=$(date +%Y-%m-%d_%H-%M-%S)
RunID="Run_"$timestamp
echo "RunID = "$RunID
OUTPUT_DIR=$MVA_OUTPUT_PATH$RunID/
echo "Creating output directory "$OUTPUT_DIR
mkdir -p $OUTPUT_DIR
case $1 in
	0)
		echo 'Running option 0'
		python $FRAMEWORK_PATH/mva/scripts/test_dnn_local.py --out_path $OUTPUT_DIR
		echo "Deleting output dir... (test run)"
		rm -rf $OUTPUT_DIR
		;;

	1)
		echo 'Running option 1'
		python $FRAMEWORK_PATH/mva/scripts/test_hammer.py --out_path $OUTPUT_DIR
		echo "Deleting output dir... (test run)"
		rm -rf $OUTPUT_DIR
		;;

	2.0)
		echo 'Running option 2.0: DNN inclusive'
		python $FRAMEWORK_PATH/mva/scripts/dnn_ucsd_inclusive.py --out_path $OUTPUT_DIR
		;;
	2.1)
		echo 'Running option 2.1: DNN 01jet'
		python $FRAMEWORK_PATH/mva/scripts/dnn_ucsd_01jet.py --out_path $OUTPUT_DIR
		;;
	2.2)
		echo 'Running option 2.2: DNN 2jet bveto'
		python $FRAMEWORK_PATH/mva/scripts/dnn_ucsd_2jet_bveto.py --out_path $OUTPUT_DIR
		;;

	3)
		echo 'Running option 3: DNN w/ resolution weights'
		python $FRAMEWORK_PATH/mva/scripts/dnn_resweights.py --out_path $OUTPUT_DIR
		;;

	*)
		echo 'Wrong option ' $1		
		echo "Deleting output dir... (test run)"
		rm -rf $OUTPUT_DIR;;
esac


