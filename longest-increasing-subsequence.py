'''
https://leetcode.com/problems/longest-increasing-subsequence/
'''


class Solution:
	'''
	Bottom-up dynamic programming solution. We initialize an array of ones to the same length as nums. Each value in this array at index i 
	will represent the length of the longest increasing subsequence ending at that index. We can iterate through the this array,
	and at every index, iterate through all values prior to this index, represented by j. At each of these index pairs, make a comparison between
	the value at each index pair in nums. If nums[i] > nums[j], then this is a potential increasing subsequence, so change the value in our DP 
	array at index i to the maximum between its current value and 1 plus the length of the LIS at index j. Once we've tried for all prior indices,
	we will have the LIS at index i and can move to the next index. Finally, we can just return max of our DP array to get the length of the LIS.

	Time Complexity: O(n^2)
	Space Complexity: O(n)
	'''
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(len(dp)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

class Solution2:
	'''
	Top-down dynamic programming solution (Leetcode fails with TLE). This recursive formulation begins at the start of the array, and the base case is defined as when
	there are no further elements left in the array. Each recursive call will try to find the longest increasing subsequence in a smaller portion of the array, and progress
	towards to the base case, returning 0 when there are no elements left. We have to define two cases, one in which the current element in the array is included in the LIS,
	and one in which the element is excluded. The variable i denotes the current element of the array in which we are considering, and prev denotes the value of the previous
	element in that recursion branches' LIS. First, we recurse on the case where we exclude the current element, and call the function again with the same value of prev,
	and increasing i by one. We assign the value returned by this call to the variable excl. Next, if the element is bigger than prev, and thus a potential candidate for that 
	LIS, then recurse with increasing i by 1, and using the value at the current index as prev. We use the variable incl to store this value, and add 1 to what is returned,
	since we are adding the value at i to the candidate LIS in this recursion branch. Finally, we compare the branch where we included the current index value with the branch where we
	excluded the current index value, and return the maximum of these two. For this implementation, we use a memoization dictionary to store already-calculated function calls with
	i and prev.

	I included this for completeness since the recursive formulation of this problem is quite different/tricky and a good thinking exercise.

	Time Complexity: O(n^2)
	Space Complexity:O(n^2)
	'''
    def __init__(self):
        self.memo = {}
    def lengthOfLIS(self, nums: List[int]) -> int:
    	if len(nums) == 0:
    		return 0
        i = 0
        return self.recurse(nums, i)
    def recurse(self, nums, i, prev=float('-inf')):
        n = len(nums)
        if i == n:
            return 0
        if (i,prev) not in self.memo:
            excl = self.recurse(nums, i+1,  prev)

            incl = 0
            if nums[i] > prev:
                incl = 1 + self.recurse(nums, i+1, nums[i])

            self.memo[(i,prev)] = max(incl, excl)
        return self.memo[(i,prev)]

class Solution3:
	'''
	To understand this solution, first understand the concept of an active increasing subsequence (AIS). As we iterate over the input, an AIS is 
	defined as the increasing sequence of a certain length which ends in the smallest possible integer value of all possible sequences 
	of that length. 

	For example, if we are iterating over an array, and we have seen the values [1,3,2] thus far. In this sequence, there are two increasing subsequences of length 2: [1,3] and [1,2]. 
	As we proceed with the iteration, the subsequence of [1,2] has more potential to find a better LIS, since its end value is lower. This is the AIS of length 2. We also have an 
	AIS of length 1, which is just [1]. If the next value we see is 5, then we now have an AIS of length 3, which is [1,2,5], and we've seen [1,3,2,5] thus far.

	As we iterate through the array, if we know the AIS for all lengths that we've seen up to that point, we can simply make a comparison with the
	new value to the last integer of each AIS. There are a few possible cases. 
	
	1) The current set of all AIS are empty (we are just starting to iterate).
	In this case, simply add the value to our set of AIS as an AIS of length 1.

	2)The value is greater than the last value in the longest AIS.
	In this case, we simply add a new AIS to our set of all AIS, which is 1 longer than the previous longest, with this value appended to it.

	3)The value is less than the last value in the longest AIS.
	In this case, we need to find the AIS of lowest length, with an ending value greater than the value. Replace the ending value of the AIS with this value.

	To illustrate case 3:
	We've seen [1,3,5] so far. Our set of AIS are {[1], [1,3], and [1,3,5]} The next value we see in the iteration is 2. Now, the increasing subsequence of length
	2 with the most potential would be [1,2], rather than the existing [1,3]. As described, we find the AIS with lowest length in our set that has a an ending value
	greater than 2, which is [1,3], and replace it with [1,2].

	There are two important factors which let us turn this into a more efficient algorithm than the DP cases. Firstly, we only care about the last value in each AIS.
	Thus, we don't need to store a set of all full AIS, but simply one array containing the last value of each AIS of each length, which will have 
	length <= the input array we are iterating over. Secondly, this will be a sorted array, meaning that when we want to find the element that we want to replace,
	in case 3, we can use a modified version of binary search, which runs in logn time.

	Thus, to put it all together and summarize:
	We create an empty array s. Each element at s[pos] will be the last value of the active increasing subsequence of length pos+1. Then, we iterate through nums once, and use comparisons
	to check for the three cases mentioned above. We either add the current number to s, or we replace the appropriate element of s, using a modified binary search algorithm
	to find the right index to replace. We also make sure that we are not adding an identical value to the previous value of s, which would not make that active LIS increasing
	any more as it would have two repeated values.

	Once we've iterated through the entire input, the global LIS for the input is simply the longest active LIS, which is just the length of s.

	The binary search ceiling algorithm is just a simple iterative version of binary search. When the loop breaks, the low index will either be the index of the value we 
	want to replace, which should be greater than the number we are replacing it with, or is one to the left of that value. We check these cases and return the index of the 
	correct value to replace.
	
	Time Complexity: O(nlogn)
	Space Complexity: O(n)
	'''
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = [nums[0]]
        for num in nums[1:]:
            if num > s[-1]:
                s.append(num)
            elif len(s) == 1:
                s[0] = num
            else:
                replace_index = self.binary_search_ceiling(s, num)
                if s[replace_index] == num:
                    continue
                elif s[replace_index] == s[replace_index-1]:
                    continue
                else:
                    s[replace_index] = num
        return len(s)
    def binary_search_ceiling(self, arr, item):
        low, high = 0, len(arr)-1
        while low < high:
            mid = low + (high-low) // 2
            if arr[mid] == item:
                return mid
            elif arr[mid] < item:
                low = mid+1
            elif arr[mid] > item:
                high = mid-1
        if arr[low] > item:
            return low
        else:
            return low+1