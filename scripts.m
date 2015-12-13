%I = imread('/Users/felisjhou/Downloads/tid2013/reference_images/I01.BMP');
%I_p = imread('/Users/felisjhou/Downloads/tid2013/distorted_images/I01_01_1.BMP');

fileID = fopen('smc_lst.txt','r');
C = textscan(fileID, '%s%s%s');
fclose(fileID);

n = cellfun('length',C);

for i=1:1:n(1)
    I  = imread(C{1,1}{i,1});
    I_p= imread(C{1,2}{i,1});
    I  = rgb2gray(I);
    I_p= rgb2gray(I_p);
    
    [feature, err_flag] = feature_smc1(I, I_p);
    if(err_flag)
        disp(C{1,1}{i,1})
        disp(C{1,2}{i,1})
        disp(C{1,3}{i,1})
    else
        fileID = fopen(C{1,3}{i,1}, 'w');
        fprintf(fileID,'%f\n', feature);
        fclose(fileID);
    end
end
