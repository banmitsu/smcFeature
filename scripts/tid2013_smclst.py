#! /usr/bin/env python
#! FelisJ release. 2013-09-13

import numpy as np
import os, sys

global DATA_label
DATA_label = {}


indexfile = sys.argv[1]
# change!
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


def _create_smc_list_():
	file = open("smc_lst.txt", "w+")
	for item in DATA_label:
		ref = item.split('_')[0]
		feat= item.split('.')[0]
		ref_img = "/tid2013/reference_images/"+ref+".BMP"
		dit_img = "/tid2013/distorted_images/"+item
		dir_feat= "/tid2013/features/"+feat+".smc"
		file.write(ref_img+' '+dit_img+' '+dir_feat+'\n')

if __name__ == '__main__':
	with open(indexfile) as f:
		lst = np.genfromtxt(f, dtype=[('score', float), ('filename', np.str_, 1024)], delimiter=' ')
	for item in lst:
		DATA_label[item['filename']] = item['score']
	_create_caffe_list_()
	_create_smc_list_()

