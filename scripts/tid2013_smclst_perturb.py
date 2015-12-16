#! /usr/bin/env ptython
#! FelisJ release. 2013-09-14

import numpy as np
import os, sys
from random import shuffle

global DATA_label
DATA_label = {}

try:
	indexlst = sys.argv[1]
except:
	print "tid2013_smclst_perturb.py ../smc_lst.txt"

if __name__ == '__main__':
	with open(indexlst) as f:
		lst = np.genfromtxt(f, dtype=[('score', np.str_, 8), ('origin', np.str_, 1024), ('distorted', np.str_, 1024), ('feat', np.str_, 1024)], delimiter=' ')
	try:
		fileto_train = open('../tid2013/train_lst.txt', 'w+')
		fileto_test  = open('../tid2013/test_lst.txt',  'w+')
	except:
		print "Open files fail."

	total_num = len(lst)
	test_num  = total_num/4
	train_num = total_num - test_num
	print "generate test/train set:", test_num, " - ", train_num
	shuffle(lst)
	train_set = lst[:train_num]
	test_set  = lst[train_num:]
	for item in train_set:
		fileto_train.write(item['feat']+' '+item['score']+'\n')
	for item in test_set:
		fileto_test.write(item['feat']+' '+item['score']+'\n')
	fileto_train.close()
	fileto_test.close()
	


