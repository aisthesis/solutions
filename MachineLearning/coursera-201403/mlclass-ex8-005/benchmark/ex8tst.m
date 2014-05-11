## Copyright (C) 2014 Marshall Farrier
## 
## Modified from coursera machine learning class for purposes
## of benchmarking.
##
## Author Marshall Farrier
## Since 2014-05-11
%% Machine Learning Online Class
%  Exercise 8 | Anomaly Detection and Collaborative Filtering
%
%  Instructions
%  ------------
%
%  This file contains code that helps you get started on the
%  exercise. You will need to complete the following functions:
%
%     estimateGaussian.m
%     selectThreshold.m
%
%  For this exercise, you will not need to change any code in this file,
%  or any other files other than those mentioned above.
%

%% Initialization
clear ; close all; 

%% ================== Part 4: Multidimensional Outliers ===================
%  We will now use the code from the previous part and apply it to a 
%  harder problem in which more features describe each datapoint and only 
%  some features indicate whether a point is an outlier.
%

%  Loads the second dataset. You should now have the
%  variables X, Xval, yval in your environment
load('ex8data2.mat');

%  Apply the same steps to the larger dataset
[mu sigma2] = estimateGaussian(X);

% Get the initial time
t0 = clock();

%% ======================== Changes begin here ======================== 
%  Training set 
ptst = multivariateGaussianTst(X, mu, sigma2);

%  Cross-validation set
ptstval = multivariateGaussianTst(Xval, mu, sigma2);

%  Find the best threshold
[tau F1] = selectThresholdTst(yval, ptstval);

% Compute time required for program to complete
elapsed_time = etime(clock(), t0);

fprintf('Best tau found using cross-validation: %e\n', tau);
fprintf('Best F1 on Cross Validation Set:  %f\n', F1);
fprintf('# Outliers found: %d\n', sum(ptst > tau));
fprintf("Elapsed time: %f seconds\n", elapsed_time);
