/*
https://leetcode.com/problems/missing-number/
*/

class Solution {
public:
	/*
	The XOR operator is commutative and associative, meaning the order we do it in doesn't matter. If we XOR an integer
	with some other integer, then XOR it again with that same integer, we get the original integer, as the two XOR operations
	will cancel out. Thus, we need to start with 0, iterate through each number in the array, and XOR it with both the number in that index
	of the array, and the index itself +1. Eventually, we will have XOR'd our starting number with every number twice, except the missing number,
	meaning all other XORs will have cancelled out, and all that's left is 0 ^ missing_num, which is just missing_num.

	Time Complexity: O(n)
	Space Complexity: O(n) 
	*/
    int missingNumber(vector<int>& nums) {
        int res = 0;
        for (int i=0; i < nums.size(); i++) {
        	if (nums[i] != 0) {
        		res ^= nums[i];
        	}
        	res ^= (i+1);
        }
        return res;
    }
};