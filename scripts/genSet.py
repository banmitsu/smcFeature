#! /usr/bin/env ptython
#! FelisJ release. 2013-09-14

import numpy as np
import os, sys
from random import shuffle

global DATA_label
DATA_label = {}

# indexlst="caffe_iqa_input.lst"
indexlst = sys.argv[1]

def _create_caffe_list_():
	file = open("caffe_iqa_input.lst", "w+")
	for item in DATA_label:
		label = _label_MOS_(item)
		label = _label_DISTORTION_(item)
		file.write(suffix_dir+item+' '+label+'\n')
	file.close()

if __name__ == '__main__':
	with open(indexlst) as f:
		lst = np.genfromtxt(f, dtype=[('filename', np.str_, 1024), ('score', np.str_, 8)], delimiter=' ')
	try:
		fileto_train = open('train_'+indexlst, 'w+')
		fileto_test  = open('test_'+indexlst, 'w+')
	except:
		print "Open file fail."
	total_num = len(lst)
	test_num  = total_num/4
	train_num = total_num - test_num
	print "generate train/test set:", test_num, " - ", train_num
	shuffle(lst)
	train_set = lst[:train_num]
	test_set  = lst[train_num:]
	for item in train_set:
		fileto_train.write(item['filename']+' '+item['score']+'\n')
	for item in test_set:
		fileto_test.write(item['filename']+' '+item['score']+'\n')
	fileto_train.close()
	fileto_test.close()
	


