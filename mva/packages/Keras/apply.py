#!/usr/bin/env python
import os, sys
sys.path.append( os.path.dirname(os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) ))

from kerasApplicator import KerasApplicator

def apply(framework, package):
	with KerasApplicator(framework, package) as t:
		t.convert_to_pandas()
		t.apply_models()	

