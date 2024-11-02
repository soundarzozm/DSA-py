class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        length = len(nums)

	for i in range(l):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = []
            hashMap[nums[i]].append(i)

        for i in range(l):
            if target-nums[i] in hashMap:
                if nums[i] == target-nums[i]:
                    if (len(hashMap[nums[i]]) >= 2):
                        return hashMap[nums[i]][:2]
                    continue
                return [i, hashMap[target-nums[i]][0]]

if __name__ == "__main__":
    solution = Solution()
    nums = []
    target = 0
    print(solution.twoSum(nums, target))
