#! /usr/bin/env python
#! FelisJ release. 2013-09-13

import numpy as np
import os, sys

global DATA_label
DATA_label = {}


def _label_MOS_(item):
	return np.str_(int(round(DATA_label[item])))

def _label_DISTORTION_(item):
	return item.split('_')[1]

def _label_switch_(label_type, item):
	if label_type == 'MOS':
		label = _label_MOS_(item)
	if label_type == 'DIS':
		label = _label_DISTORTION_(item)
	return label

def _create_caffe_list_(suffix_dir):
	file = open("caffe_iqa_input.lst", "w+")
	for item in DATA_label:
		label = _label_switch_('MOS', item)
		feature= item.split('.')[0]+'.smc'
		file.write(suffix_dir+feature+' '+label+'\n')
	file.close()

if __name__ == '__main__':
	arg_names = ['command', 'indexfile', 'suffix_dir']
	args = dict(zip(arg_names, sys.argv))
	if len(args) < 3:
		print "Error command:..."
		print "python tid2013indexer.py ../tid2013/mos_with_names.txt /path/to/features/"
		sys.exit()
	print "Indexfile: ", args['indexfile'], "Suffix_dir: ", args['suffix_dir']
	#sys.exit()

	with open(args['indexfile']) as f:
		lst = np.genfromtxt(f, dtype=[('score', float), ('filename', np.str_, 1024)], delimiter=' ')
	for item in lst:
		DATA_label[item['filename']] = item['score']

	_create_caffe_list_(args['suffix_dir'])


