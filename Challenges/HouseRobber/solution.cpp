/**
 * House Robber challenge from leetcode
 * https://leetcode.com/problems/house-robber/
 *
 * Copyright (c) 2015 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2015-05-01
 */

#include <vector>
#include <iostream>

class Solution {
    private:
        std::vector<int> best;
    public:
        int rob(std::vector<int> &nums) {
            best = nums;
            size_t len = nums.size();
            if (len == 0) {
                return 0;
            }
            else if (len > 1) {
                solve(nums, len);
            }
            return best[len - 1]; 
        }
    private:
        void solve(const std::vector<int> &nums, const size_t &len) {
            if (nums[1] < nums[0]) {
                best[1] = best[0];
            }
            for (int i = 2; i < len; ++i) {
                if (nums[i] + best[i - 2] > best[i - 1]) {
                    // we can improve by robbing this house instead of previous
                    best[i] = nums[i] + best[i - 2];
                }
                else {
                    best[i] = best[i - 1];
                }
            }
        }
};

int main() {
    Solution solution;
    std::vector<int> test {5, 2, 7, 9, 3, 1};

    std::cout << solution.rob(test) << std::endl;
    return 0;
}
