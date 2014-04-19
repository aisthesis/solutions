function [result] = myTest()
    n = 5;
    m = 3;
    result = zeros(m, n);
    for i = 1:m
        result(i, 1) = 6;
    endfor
end
