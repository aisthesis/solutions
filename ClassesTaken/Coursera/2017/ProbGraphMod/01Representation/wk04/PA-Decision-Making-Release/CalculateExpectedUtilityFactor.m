% Copyright (C) Daphne Koller, Stanford University, 2012

function EUF = CalculateExpectedUtilityFactor( I )

  % Inputs: An influence diagram I with a single decision node and a single utility node.
  %         I.RandomFactors = list of factors for each random variable.  These are CPDs, with
  %              the child variable = D.var(1)
  %         I.DecisionFactors = factor for the decision node.
  %         I.UtilityFactors = list of factors representing conditional utilities.
  % Return value: A factor over the scope of the decision rule D from I that
  % gives the conditional utility given each assignment for D.var
  %
  % Note - We assume I has a single decision node and utility node.
  % EUF = [];
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %
  % YOUR CODE HERE...
  %
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  

    EUF = struct('var', [], 'card', [], 'val', []);

    F = [ I.RandomFactors I.UtilityFactors ];
    X = I.RandomFactors;
    D = I.DecisionFactors(1);
    U = I.UtilityFactors(1);

    allVars = unique([ F(:).var ]);
    toKeep = D.var;
    toEliminate = setdiff(allVars, toKeep);
    factors = VariableElimination(F, toEliminate);

    parentsD = factors(1);
    for i = 2:length(factors),
        parentsD = FactorProduct(parentsD, factors(i));
    endfor;

    EUF = parentsD;

end  
