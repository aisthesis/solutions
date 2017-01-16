%ComputeJointDistribution Computes the joint distribution defined by a set
% of given factors
%
%   Joint = ComputeJointDistribution(F) computes the joint distribution
%   defined by a set of given factors
%
%   Joint is a factor that encapsulates the joint distribution given by F
%   F is a vector of factors (struct array) containing the factors 
%     defining the distribution
%

function Joint = ComputeJointDistribution(F)

  % Check for empty factor list
  if (numel(F) == 0)
      warning('Error: empty factor list');
      Joint = struct('var', [], 'card', [], 'val', []);      
      return;
  end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% YOUR CODE HERE:
% Compute the joint distribution defined by F
% You may assume that you are given legal CPDs so no input checking is required.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
% adding 0 guarantees a deep copy of each array
% http://stackoverflow.com/questions/35818295/octave-force-deepcopy
Joint = struct('var', F(1).var + 0, 'card', F(1).card + 0, 'val', F(1).val + 0);
for i = 2:length(F)
    Joint = FactorProduct(Joint, F(i));
endfor;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end

