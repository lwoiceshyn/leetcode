class Solution:
    '''
    Bottom-up dynamic programming solution. Similar to House Robber I, we want to iterate through the houses, keeping track of a maximum value, following
    the recursive formula: f(n) = max(f(n-1), nums[n]+f(n-2)). In this case, where we have a circular constraint on the first and last house in the array,
    we need to do two passes. One which includes the first house, but excludes the last one, and one which excludes the first house, and includes the last one.
    Then we can just compare the maximum sums from these two passes and the maximum between them is the global maximum sum that we can obtain. Since our recursion
    only cares about the previous two values, we can achieve constant space complexity by storing four temp values (two for each iteration) and just update these.
    Also, we only have to really do one iteration, and just access different indices of nums depending on whether we are referring to the first situation, where
    we include the first house, or the second situation.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    ''' 
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 4:
            return max(nums)
        dp1 = [nums[0], max(nums[0], nums[1])]
        dp2 = [nums[1], max(nums[1], nums[2])]
        for i in range(2, len(nums)-1):
            dp1 = [dp1[1], max(dp1[1],nums[i]+dp1[0])]
            dp2 = [dp2[1], max(dp2[1], nums[i+1]+dp2[0])]
        return max(dp1[1], dp2[1])
