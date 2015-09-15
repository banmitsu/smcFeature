The file feature_smc1.m is for feature extraction. It takes the reference and distorted images as input and gives the 256 dimensional feature vector as the output.

models_smc_revised.mat contains the 4 models developed by using TID, LIVE, CSIQ and watermark image databases.

The folder "svm" consists of the support vector machine toolkit which has been downloaded from http://www.csie.ntu.edu.tw/\verb~cjlin/libsvm

Please follow the instructions for its installtion from their website.


********************************************************************************
An example usage is given below.

Suppose tr_l_a57 is the vector containing the subjective scores from the A57 database and tr_a57 consists of the corresponding image feature vectors.


load models_smc_final.mat

[pr_live,a1]=svmpredict(tr_l_a57,tr_a57',model_live_smc);

[pr_csiq,a1]=svmpredict(tr_l_a57,tr_a57',model_csiq_smc);

[pr_tid,a1]=svmpredict(tr_l_a57,tr_a57',model_tid_smc);

[pr_watermark,a1]=svmpredict(tr_l_a57,tr_a57',model_watermark_smc);

Then pr_live,pr_csiq,pr_tid and pr_watermark contain the predicted scores from the respective models.
*********************************************************************************