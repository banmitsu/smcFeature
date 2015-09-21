#! /usr/bin/env python
#! 2015
import numpy as np
import os, sys
import lmdb
import caffe.io
from caffe.proto import caffe_pb2
import matplotlib.pyplot as plt

LMDB_PATH = sys.argv[1]
env = lmdb.open(LMDB_PATH, readonly=True, lock=False)

OUTPUT_PATH = sys.argv[2]

datum = caffe_pb2.Datum()

num_datum = 60000
visualize = False

X = []

with env.begin() as txn:
	cur = txn.cursor()
	for i in xrange(num_datum):
		if not cur.next():
			#cur.first()
			break
		key, value = cur.item()
		datum.ParseFromString(value)	
		# img_data = np.array(bytearray(datum.data)).reshape(datum.channels, datum.height, datum.width)
		if datum.width == 1 & datum.height == 1 & datum.channels == 1:
			data = np.array(datum.float_data)
		else:
			data = np.array(datum.float_data).reshape(datum.channels, datum.height, datum.width)
		#if visualize:
		#	plt.imshow(img_data.transpose([1,2,0]))
		#	plt.show()
		X.append(data)
		print key, data
		# break

np.savetxt(OUTPUT_PATH, X, newline='\n', fmt="%1.6f")

