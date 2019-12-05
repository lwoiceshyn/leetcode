'''
https://leetcode.com/problems/jump-game-ii/
'''


class Solution:
    '''
    Maintain a sliding window that represents the indices we can reach in a certain number of steps. We start with the range we can reach from
    the first index, which would be 1 step. Then, each iteration of a while loop, while our end pointer is less than the end index of the array,
    we increase our step count by 1, then go through each index in our interval. If the current index + its jump distance can reach the end, then
    return the step count. Otherwise, update a max_end variable which tracks the end pointer for the next interval, by finding the max index we can
    reach from 1 jump from the current interval. Then, at the end of each loop iteration, set the left interval to 1 + the old right interval, and 
    the right interval to the max index we could reach from the last interval.

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        start, end, step, n = 0, nums[0], 1, len(nums)
        max_end = 0
        while end < n-1:
            step += 1
            for i in range(start,end+1):
                if i + nums[i] >= n-1:
                    return step
                else:
                    max_end = max(max_end, i+nums[i])
            start, end = end+1, max_end
        return step



class Solution2:
    '''
    Bottom-up dynamic programming solution. DP array represents the minimum number of jumps to reach tile i. 
    '''
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * (len(nums))
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], 1+dp[j])
        return dp[-1]
