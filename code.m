clear all
close all
clc
tic


logo = (imread('logo5.png'));                                               %read logo
jpegFiles = dir('*.jpg');                                                   %find jpg files in the directory
numfiles = length(jpegFiles);
%mydata = cell(1,length(jpegFiles));


for K = 1 : numfiles
    a = imread(jpegFiles(K).name);                                          %read the image
    a((size(a,1)-size(logo,1)+1):end,1:size(logo,2),1) = logo(:,:,3);       %add logo
    filename = sprintf('nature%02d.png', K);
    imwrite(a,filename);
end


t=toc;
fprintf('average time taken to process image is = %5d \n',t/length(K))
