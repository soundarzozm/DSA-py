class Solution:
    def topKFrequentElements(self, nums, k):

        # Bucket array is indexed based on count
        # E.g. bucket[6] will have an array of all numbers which appear 6 times in nums
        bucket = [[]] * (len(nums) + 1)
        hashMap = {}
        res = []
		
		# Populate hashmap with {num: count} logic
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1

		# Populate bucket sort
		# E.g. since 1 appears thrice, bucket[3] will have 1 appended to it
        for num in hashMap:
            bucket[hashMap[num]] = bucket[hashMap[num]] + [num]

        pointer = len(bucket) - 1
		
		# Traverse bucket in reverse and populate result
        while len(res) <= k and pointer >= 0:
            for num in bucket[pointer]:
                res.append(num)
            pointer -= 1

        return res[:k]

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 3]
    k = 2
    print(solution.topKFrequentElements(nums, k))
