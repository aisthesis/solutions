% clean.m
% Clean Yule data by subtracting
% 100 from all values.
% Then save as yule-cleaned.mat
%
% Author: Marshall Farrier
% Since: 2014-06-11

function clean() 

load('yule.dat');
yuleCleaned = yule - 100;
save('-mat-binary', 'yule-cleaned.mat', 'yuleCleaned');

end
