#! /usr/bin/env python
#! FelisJ release. 2013-09-15

import numpy as np
import os, sys
import lmdb
from caffe.io import array_to_datum

global DATA_label
DATA_label = {}


def _svm_feature_(feature):
    tmpS = ''
    i = 0
    # convert to svm format
    for i in range(0, len(feature)):
        tmpS += str(i+1) + ':' + str(feature[i]) + ' '
    return tmpS

def _lmdb_feature_(feature):
    arr = [float(dim) for dim in feature]
    return arr

def _create_lmdb_(lmdb_filename, X, Y):
    num = np.prod(X.shape)
    itemsize = np.dtype(X.dtype).itemsize
    # set a reasonable upper limit for database size
    map_size = 10240 * 1024 + num * itemsize * 2
    print 'save {} instances...'.format(num)
    env = lmdb.open(lmdb_filename, map_size=map_size)
    for i, (x, y) in enumerate(zip(X, Y)):
        datum = array_to_datum(x, y)
        str_id = '{:08}'.format(i)
        with env.begin(write=True) as txn:
            txn.put(str_id, datum.SerializeToString())


if __name__ == '__main__':
	arg_names = ['command', 'inputlist', 'prefix']
	args = dict(zip(arg_names, sys.argv))
	if len(args) < 2:
		print "Error command:..."
		print "python genSvminput.py /path/to/feature/list /prefix/to/output/file"
		sys.exit()
	if len(args) < 3:
		args['prefix'] = ''
	print "Inputlist: ", args['inputlist'], "Prefix_output: ", args['prefix']
	#sys.exit()
	
	try:
		lmdb_out = []
		lmdb_filename = args['prefix']+"lmdb_input"
		svm_filename  = args['prefix']+"svm_input"
		svm_handle = open(svm_filename,"w+")
	except:
		print "output file failed."
		pass

	with open(args['inputlist']) as f:
		lst = np.genfromtxt(f, dtype=[('filename', np.str_, 1024), ('label', np.str_, 10)], delimiter=' ')
	print "TOTAL Featurs: ", len(lst)
	for item in lst:
		print item['filename'], item['label']
		txt = np.genfromtxt(item['filename'], dtype=[('feature', np.str_, 1024)], delimiter='\n')
		# raw feature
		feature = txt['feature'].T.tolist()
		# label
		label   = str(item['label'])

		# svm
		svm_feature = _svm_feature_(feature)
		svm_handle.write(label+' '+svm_feature+'\n')
		# lmdb
		lmdb_out.append( (int(label), _lmdb_feature_(feature)) )
		# break
	
	num_of_dims = len(feature)
	Y = np.array([y for y, _ in lmdb_out])
   	X = np.array([x for _, x in lmdb_out])
    	X = X.reshape( (len(Y), 1, 1, num_of_dims) )
    	_create_lmdb_(lmdb_filename, X, Y)
    
