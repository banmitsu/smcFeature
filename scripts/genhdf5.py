#! /usr/bin/env python
#! FelisJ release. 2013-09-15

import numpy as np
import os, sys
from subprocess import call
import lmdb
import h5py
from caffe.io import array_to_datum

global DATA_label
DATA_label = {}


def _feature_(feature):
    arr = [float(dim) for dim in feature]
    return arr

def _create_hdf5_(f,  X, Y):
    with h5py.File(hdf5_filename, "w") as f:
    	dset = f.create_dataset("data", data=X)
	dset = f.create_dataset("label", data=Y)

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
		_out = []
		hdf5_filename = args['prefix']+"hdf5_input"
		call(["rm", hdf5_filename])
	except:
		print "output file failed."
		pass

	with open(args['inputlist']) as f:
		lst = np.genfromtxt(f, dtype=[('filename', np.str_, 1024), ('label', np.str_, 10)], delimiter=' ')
	print "TOTAL Featurs: ", len(lst)
	for item in lst:
		#print item['filename'], item['label']
		txt = np.genfromtxt(item['filename'], dtype=[('feature', np.str_, 1024)], delimiter='\n')
		# raw feature
		feature = txt['feature'].T.tolist()
		# label
		label   = str(item['label'])

		# print feature
		# print label

		_out.append( (float(label), _feature_(feature)) )
		# hdf5
		#break
	
	num_of_dims = len(feature)
	Y = np.array([y for y, _ in _out])
   	X = np.array([x for _, x in _out])
    	X = X.reshape( (len(Y), 1, 1, num_of_dims) )
	Y = Y.reshape( (len(Y)), 1 )
    	_create_hdf5_(hdf5_filename, X, Y)

	f = h5py.File(hdf5_filename, 'r')
	# print f.keys()
	
