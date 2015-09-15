#! /usr/bin/env python
#! FelisJ release. 2015-09-09
import numpy as np
import os, sys

nameto_lst = sys.argv[1]

with open(nameto_lst) as f:
    lst = np.genfromtxt(f, dtype=[('name', np.str_, 1024), ('label', int)], delimiter=' ')

label_max   = np.max(lst['label'])
label_min =  np.min(lst['label'])

num_label = len(lst['label'])

print "Total data: ", num_label

for i in range(label_min, label_max+1):
    count = len([item for item in lst['label'] if item == i])
    print "Class-", i, " : ", count, "/", float(count)/float(num_label)


