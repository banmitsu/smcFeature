# smcFeature
This is a script to generate smc features for TID2013

(1) smc features: http://www.ntu.edu.sg/home/wslin/codes_smc.rar

Narwaria, M.; Weisi Lin, "SVD-Based Quality Metric for Image and Video Using Machine Learning," in Systems, Man, and Cybernetics, Part B: Cybernetics, IEEE Transactions on , vol.42, no.2, pp.347-364, April 2012
URL: http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6031933&isnumber=6169194

(2) TID 2013 (IQA): http://ponomarenko.info/tid2013.htm

MATLAB> scripts.m

FORMAT of smc_lst.txt:

path/to/reference/image> path/to/distorted/image /path/to/saved/feature \n

Feature download: https://drive.google.com/file/d/0B1rhqS7SXhCcczd4Y1BwckJrdmM/view?usp=sharing

Scripts Directory:

tid2013_smclst.py : output smc_lst.txt (-> scripts.m input)

	- ipython tid2013_scmlst.py ../tid2013/mos_with_names.txt

tid2013indexer.py : output (caffe) iqa_input.lst

	- ipython tid2013indexer.py ../tid2013/mos_with_names.txt /path/to/features/dir

genSet.py         : output train/test_iqa_input.lst

	- ipython genSet.py iqa_input.lst

genSvminput.py    : output svm input, lmdb input

	- ipython genSvminput.py iqa_input.lst /prefix/to/output

	- ipython genSvminput.py train_iqa_input.lst train_

	- ipython genSvminput.py test_iqa_input.lst test_
