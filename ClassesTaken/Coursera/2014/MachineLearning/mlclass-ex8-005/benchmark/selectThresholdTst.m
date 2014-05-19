function [bestTau bestF1] = selectThresholdTst(yval, ptstval) 
%SELECTTHRESHOLD Find the best threshold (tau) to use for selecting
%outliers
%   [bestEpsilon bestF1] = SELECTTHRESHOLD(yval, ptstval) finds the best
%   threshold to use for selecting outliers based on the results from a
%   validation set (ptstval) and the ground truth (yval).
%

bestEpsilon = 0;
bestF1 = 0;
F1 = 0;
truePositives = 0;
falsePositives = 0;
falseNegatives = 0;
prec = 0;
rec = 0;
predictions = zeros(size(ptstval));

stepsize = (max(ptstval) - min(ptstval)) / 1000;
for tau = min(ptstval):stepsize:max(ptstval)
    
    % ====================== YOUR CODE HERE ======================
    % Instructions: Compute the F1 score of choosing tau as the
    %               threshold and place the value in F1. The code at the
    %               end of the loop will compare the F1 score for this
    %               choice of tau and set it to be the best tau if
    %               it is better than the current choice of tau.
    %               
    % Note: You can use predictions = (ptstval < tau) to get a binary vector
    %       of 0's and 1's of the outlier predictions

    predictions = (ptstval > tau);
    truePositives = sum(predictions & yval);
    falsePositives = sum(predictions & !yval);
    falseNegatives = sum(!predictions & yval);
    if (truePositives == 0)
        continue
    endif
    prec = truePositives / (truePositives + falsePositives);
    rec = truePositives / (truePositives + falseNegatives);
    F1 = 2 * prec * rec / (prec + rec);

    % =============================================================

    if F1 > bestF1
       bestF1 = F1;
       bestTau = tau;
    end
end

end
