class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        length = len(nums)

        for i in range(length):
            hashMap[nums[i]] = i

        for i in range(length):
            computedTarget = target - nums[i]
            if computedTarget in hashMap:
                return [i, hashMap[computedTarget]]

        return -1

if __name__ == "__main__":
    solution = Solution()
    nums = []
    target = 0
    print(solution.twoSum(nums, target))
