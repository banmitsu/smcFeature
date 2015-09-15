#! /usr/bin/env python
#! FelisJ release. 2013-09-13

import numpy as np
import os, sys

global DATA_label
DATA_label = {}

try:
	indexfile = sys.argv[1]
except:
	print "tid2013_smclst.py ../tid2013/mos_with_names.txt"

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
	_create_smc_list_()

