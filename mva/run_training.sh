#!/bin/sh

timestamp=$(date +%Y-%m-%d_%H-%M-%S)
RunID="Run_"$timestamp
echo "RunID = "$RunID
OUTPUT_DIR=$MVA_OUTPUT_PATH$RunID/
echo "Creating output directory "$OUTPUT_DIR
mkdir $OUTPUT_DIR
case $1 in
	0)
		echo 'Running option 0'
		python $FRAMEWORK_PATH/mva/scripts/test_dnn_local.py --out_path $OUTPUT_DIR
		;;

	0)
		echo 'Running option 1'
		python $FRAMEWORK_PATH/mva/scripts/test_hammer.py --out_path $OUTPUT_DIR
		;;

	*)
		echo 'Wrong option ' $1;;		

esac

echo "Deleting output dir... (test run)"
rm -rf $OUTPUT_DIR

