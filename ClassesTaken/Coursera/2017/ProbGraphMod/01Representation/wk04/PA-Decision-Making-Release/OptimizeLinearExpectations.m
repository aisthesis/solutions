% Copyright (C) Daphne Koller, Stanford University, 2012

function [MEU OptimalDecisionRule] = OptimizeLinearExpectations( I )
  % Inputs: An influence diagram I with a single decision node and one or more utility nodes.
  %         I.RandomFactors = list of factors for each random variable.  These are CPDs, with
  %              the child variable = D.var(1)
  %         I.DecisionFactors = factor for the decision node.
  %         I.UtilityFactors = list of factors representing conditional utilities.
  % Return value: the maximum expected utility of I and an optimal decision rule 
  % (represented again as a factor) that yields that expected utility.
  % You may assume that there is a unique optimal decision.
  %
  % This is similar to OptimizeMEU except that we will have to account for
  % multiple utility factors.  We will do this by calculating the expected
  % utility factors and combining them, then optimizing with respect to that
  % combined expected utility factor.  
  % MEU = [];
  % OptimalDecisionRule = [];
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %
  % YOUR CODE HERE
  %
  % A decision rule for D assigns, for each joint assignment to D's parents, 
  % probability 1 to the best option from the EUF for that joint assignment 
  % to D's parents, and 0 otherwise.  Note that when D has no parents, it is
  % a degenerate case we can handle separately for convenience.
  %
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  
    EUF = struct('var', [], 'card', [], 'val', []);

    for i = 1:length(I.UtilityFactors)
        tmpI = I;
        tmpI.UtilityFactors = I.UtilityFactors(i);
        tmpEUF = CalculateExpectedUtilityFactor(tmpI);
        EUF = FactorSum(EUF, tmpEUF);
    endfor

    OptimalDecisionRule = struct('var', [], 'card', [], 'val', []);
    OptimalDecisionRule.var = EUF.var;
    OptimalDecisionRule.card = EUF.card;
    OptimalDecisionRule.val = zeros(prod(OptimalDecisionRule.card), 1);

    if length(EUF.var) < 2,
        [MEU myIndex] = max(EUF.val);
        OptimalDecisionRule.val(myIndex) = 1;
    else
        MEU = 0.0;
        fullAssignment = IndexToAssignment([1:prod(OptimalDecisionRule.card)],OptimalDecisionRule.card);
        for i = 1:prod(OptimalDecisionRule.card(2:end))
            subAssignment = IndexToAssignment(i,OptimalDecisionRule.card(2:end));
            myIndex = [];
            for j = 1:size(fullAssignment,1)
                if all(fullAssignment(j,2:size(fullAssignment,2))==subAssignment)
                    myIndex = [myIndex;j];
                endif
            endfor
            Assignment = IndexToAssignment(myIndex,OptimalDecisionRule.card);
            myValue = GetValueOfAssignment(EUF,Assignment);
            [myMax mySubIndex] = max(myValue);
            OptimalDecisionRule.val(myIndex) = 0;
            OptimalDecisionRule.val(myIndex(mySubIndex)) = 1;
            MEU = MEU + EUF.val(myIndex(mySubIndex));
        endfor
    endif

endfunction
