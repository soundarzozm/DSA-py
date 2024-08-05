class Solution:
    def topKFrequentElements(self, nums, k):

        # This array is indexed based on count
        # E.g. arr[6] will have an array of all numbers who appear 6 times in nums
        arr = [[]] * (len(nums) + 1)
        hashMap = {}
        res = []

        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1

        for num in hashMap:
            arr[hashMap[num]] = arr[hashMap[num]] + [num]

        pointer = len(arr) - 1

        while len(res) <= k and pointer >= 0:
            for num in arr[pointer]:
                res.append(num)
            pointer -= 1

        return res[:k]

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 3]
    k = 2
    print(solution.topKFrequentElements(nums, k))
