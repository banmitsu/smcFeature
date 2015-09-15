#! /usr/bin/env python
#! FelisJ release. 2013-09-13

import numpy as np
import os, sys

global DATA_label
DATA_label = {}

# indexfile="mos_with_names.txt"
indexfile = sys.argv[1]
# suffix_dir="/home/fj/felis/tid2013/distorted_images/"
suffix_dir = sys.argv[2]

def _label_MOS_(item):
	return np.str_(DATA_label[item])

def _label_DISTORTION_(item):
	return item.split('_')[1]

def _create_caffe_list_():
	file = open("caffe_iqa_input.lst", "w+")
	for item in DATA_label:
		label = _label_MOS_(item)
		label = _label_DISTORTION_(item)
		file.write(suffix_dir+item+' '+label+'\n')
	file.close()

if __name__ == '__main__':
	with open(indexfile) as f:
		lst = np.genfromtxt(f, dtype=[('score', float), ('filename', np.str_, 1024)], delimiter=' ')
	for item in lst:
		DATA_label[item['filename']] = item['score']
	_create_caffe_list_()


