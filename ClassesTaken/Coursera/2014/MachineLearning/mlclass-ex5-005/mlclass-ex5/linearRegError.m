## Copyright (C) 2014 Marshall Farrier

## -*- texinfo -*-
## @deftypefn  {Function File} {} linearRegError (@var{X}, @var{y}, @var{theta})
## Return the error of linear regression parameters theta over data set X (features)
## that map to actual values y.
## @end deftypefn

## Author mdf
## Since 2014-04-26

function J = linearRegError(X, y, theta)
    m = length(y);
    J = sum(((X * theta) - y) .^ 2) / (2 * m);
end
