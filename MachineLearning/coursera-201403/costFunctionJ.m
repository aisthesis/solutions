function J = costFunctionJ(X, y, theta)

% X is the design matrix (training set)
% y is the class labels

m = size(X, 1);     % number of training examples
predictions = X * theta;
sqrErrors = (predictions - y) .^ 2;
J = 1 / (2 * m) * sum(sqrErrors);
