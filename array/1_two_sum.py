class Solution:
    def twoSum(self, nums, target):

	# Initialize a hashmap since we need to run this algorithm in O(n) time
        hashMap = {}
        length = len(nums)
	
	# Populate the hashmap with all values and their indices in an array
	# For example: nums = [1, 2, 3, 1]
	# {
	# 	1: [0, 3],
	#	2: [1],
	# 	3: [2]
	# }
	for i in range(l):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = []
            hashMap[nums[i]].append(i)
	
        for i in range(l):
        # If target - nums[i] is present in the hashmap, we have our answer. 
	# But what if nums[i] == target - nums[i]? We might be referring to the same element twice.
	    if target-nums[i] in hashMap:
                if nums[i] == target-nums[i]:
		
		    # Here we make sure we are not referring to the same element twice
                    if (len(hashMap[nums[i]]) >= 2):
                        return hashMap[nums[i]][:2]
                    continue
                return [i, hashMap[target-nums[i]][0]]

if __name__ == "__main__":
    solution = Solution()
    nums = []
    target = 0
    print(solution.twoSum(nums, target))
