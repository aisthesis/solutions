function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

# For the exercise use this array for both C and sigma test cases
values = [0.01 0.03 0.1 0.3 1 3 10 30]';

# Set up test cases for each
C_vec = values;
sigma_vec = values;
C_vec_len = length(C_vec);
sigma_vec_len = length(sigma_vec);

# Set up matrix of validation errors
valErrors = zeros(C_vec_len, sigma_vec_len);

# Set up predictions matrix
predictions = zeros(size(y));

for i = 1:C_vec_len
    for j = 1:sigma_vec_len
        fprintf("Training model with C = %f and sigma = %f\n", C_vec(i), sigma_vec(j));
        if exist('OCTAVE_VERSION')
            fflush(stdout);
        end
        model= svmTrain(X, y, C_vec(i), @(x1, x2) gaussianKernel(x1, x2, sigma_vec(j)));
        predictions = svmPredict(model, Xval);
        valErrors(i, j) = mean(double(predictions ~= yval));
        fprintf("Error on cross-validation set: %f\n", valErrors(i, j));
        if exist('OCTAVE_VERSION')
            fflush(stdout);
        end
    endfor
endfor

# Get minimum error and determine location in error matrix
[~, index] = min(valErrors(:));
row = mod(index - 1, C_vec_len) + 1;
col = idivide(index - 1, C_vec_len) + 1;

# Get values for C and sigma
C = C_vec(row);
sigma = sigma_vec(col);

# Report results
fprintf("Minimum error on cross-validation set: %f\n", valErrors(row, col));
fprintf("C: %f\n", C);
fprintf("sigma: %f\n", sigma);
if exist('OCTAVE_VERSION')
    fflush(stdout);
end

% =========================================================================

end
