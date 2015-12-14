%% WRITING TO HDF5

prefix = 'train';
filename = strcat(prefix,'.h5');
listname = strcat(prefix,'_list.txt');

% to simulate data being read from disk / generated etc.
root = '/Users/felisjhou/Downloads/';

fileID = fopen( strcat(strcat(strcat(root,'tid2013/'),prefix),'_mos_pair.txt'), 'r');
C = textscan(fileID, '%f%s%s');
fclose(fileID);

n = cellfun('length',C);
num_start_samples=1;
num_total_samples=n(1);
data_disk=zeros(32,32,2,num_total_samples); 
label_disk=zeros(1,num_total_samples); 

%%
for i=1:1:n(1)
    score = C{1,1}(i);
    I  = imread( strcat(root, C{1,2}{i,1}) );
    I_p= imread( strcat(root, C{1,3}{i,1}) );
    I  = rgb2gray(I);
    I_p= rgb2gray(I_p);
    
    [paired_img, err_flag] = pair_image(I, I_p);
    if(err_flag)
        disp(C{1,1}(i))
        disp(C{1,2}(i))
    else
        data_disk(:,:,:,i)=paired_img; 
        label_disk(1,i)=score;
    end
end


%%

chunksz=10;
created_flag=false;
totalct=0;
for batchno=1:num_total_samples/chunksz
  fprintf('batch no. %d\n', batchno);
  last_read=(batchno-1)*chunksz;

  % to simulate maximum data to be held in memory before dumping to hdf5 file 
  batchdata=data_disk(:,:,:,last_read+1:last_read+chunksz); 
  batchlabs=label_disk(:,last_read+1:last_read+chunksz);

  % store to hdf5
  startloc=struct('dat',[1,1,1,totalct+1], 'lab', [1,totalct+1]);
  curr_dat_sz=store2hdf5(filename, batchdata, batchlabs, ~created_flag, startloc, chunksz); 
  created_flag=true;% flag set so that file is created only once
  totalct=curr_dat_sz(end);% updated dataset size (#samples)
end

% display structure of the stored HDF5 file
h5disp(filename);
% READING FROM HDF5

% CREATE list.txt containing filename, to be used as source for HDF5_DATA_LAYER
FILE=fopen(listname, 'w');
fprintf(FILE, '%s', filename);
fclose(FILE);
fprintf('HDF5 filename listed in %s \n', listname);


%% Read data and labels for samples #1000 to 1999
data_rd=h5read(filename, '/data', [1 1 1 1000], [32, 32, 2, 1000]);
label_rd=h5read(filename, '/label', [1 1000], [1, 1000]);
fprintf('Testing ...\n');
try 
  assert(isequal(data_rd, single(data_disk(:,:,:,1000:1999))), 'Data do not match');
  assert(isequal(label_rd, single(label_disk(:,1000:1999))), 'Labels do not match');

  fprintf('Success!\n');
catch err
  fprintf('Test failed ...\n');
  getReport(err)
end

%delete(filename);

% NOTE: In net definition prototxt, use list.txt as input to HDF5_DATA as: 
% layer {
%   name: "data"
%   type: "HDF5Data"
%   top: "data"
%   top: "labelvec"
%   hdf5_data_param {
%     source: "/path/to/list.txt"
%     batch_size: 64
%   }
% }
