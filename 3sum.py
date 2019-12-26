'''
https://leetcode.com/problems/3sum/
'''

class Solution:
	'''
	Uses the two-pointer technique to find all unique triplets in quadratic time. First, the array is sorted, which takes O(nlogn) time. 
	Then, the two-pointer techniqueis applied. The if statement after the first while statement ensures we do not redundantly re-check for 
	identical values. Then, we compare triplets, and if greater than 0, decrease our right pointer, and if less than 0, increase our left 
	pointer. If our triplet sum is equal to zero, then we add it to our outputs list. The two final while statements are necessary to ensure 
	we do not include any repeated triplets. They each increment/decrement their respective pointer until a unique value is reached. Even if 
	both are shifted, it doesn't skip any potential triplets since shifting only one to a new unique value guarantees that the sum won't be 
	zero, since the other two values in the triplet are the same as before, where the sum was zero.

	Time Complexity: O(n^2), since the sorting is O(nlogn), and the two-poiner technique runs in O(n^2)
	Space Complexity: O(1)
	'''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputs = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i-1]: 
                j, k = i+1, len(nums)-1
                while j < k:
                    if nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        outputs.append([nums[i], nums[j], nums[k]])
                        j, k = j+1, k-1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
            i+=1
        return outputs

class Solution2:
	'''
	(Not accepted by Leetcode)
	My first attempt at a solution using a hashing method. First, we iterate through all unique pairs of indices and find the value 
	that would complete their triplet. This value is used as a dictionary key, and the two indices that complete the triplet are stored 
	as a corresponding value. These are stored in a list of nested tuples to ensure that the dictionary values are not overwritten when
	an identical match value is used.

	Then, we go linearly through each value in the array, and see if that value completes a triplet by checking if it is a key in the dictionary. 
	If so, we take the list of index pairs that match this value and iterate through them. We use a list of sets to check if this triplet is unique, 
	and if so, add it to our outputs.

	Time Complexity: O(n^2)
	Space Complexity: O(n)
	'''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
	    required = {}
	    outputs = []
	    unique_sets = []
	    for i in range(0, len(nums)-1):
	        for j in range(i+1, len(nums)):
	            missing = 0 - nums[i] - nums[j]
	            key = missing
	            value = (i,j)
	            if key not in required:
	                required[key] = [value]
	            else:
	                required[key].append(value)
	    for i in range(len(nums)):
	        if nums[i] in required:
	            match_index_list = required[nums[i]]
	            for match_indices in match_index_list:
	                if i not in match_indices:
	                    if set([nums[i], nums[match_indices[0]], nums[match_indices[1]]]) not in unique_sets:
	                        outputs.append([nums[i], nums[match_indices[0]], nums[match_indices[1]]])
	                        unique_sets.append(set([nums[i], nums[match_indices[0]], nums[match_indices[1]]]))
	    return outputs


class Solution3:
	'''
	(Not accepted by Leetcode)
	A more elegant version of the above hashing solution, that doesn't require a dictionary. For each index i, instantiate an empty set, and iterate through all remaining indices 
	that form a unique index pair that hasn't been visited yet. Calculate the value needed to complete the triplet at this unique pair. If that value is already in our set, ensure that the triplet
	is unique (using a list of sets), and if so, add it to our output list. If not, add the value at our second index to the set.

	Time Complexity: O(n^2)
	Space Complexity: O(n)
	'''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
	    outputs = []
	    unique_sets = []
	    for i in range(0, len(nums)-1):
	        matches = set()
	        for j in range(i+1, len(nums)):
	            match = -(nums[i] + nums[j])
	            if match in matches:
	                if set([nums[i], nums[j], match]) not in unique_sets:
	                    outputs.append([nums[i], nums[j], match])
	                    unique_sets.append(set([nums[i], nums[j], match]))
	            else:
	                matches.add(nums[j])
	    return outputs

