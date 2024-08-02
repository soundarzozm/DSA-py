class Solution:
    def threeSum(self, nums):
        # Sort the array to use 2sum II's approach
        # This will take O(nlogn) time
        ans = []
        nums.sort()

        # i is the first pointer and it will run only till last -2 terms since they will be l and r
        for i in range(len(nums) - 2):

            # We have to skip whenever ith term is repeating
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:

                # This is the current sum
                # The question asks us pairs when this is 0
                s = nums[i] + nums[l] + nums[r]

                # The greater than 0 and less than 0 conditions are straightforward
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1

                # This is a tricky case
                else:
                    ans.append([num, nums[l], nums[r]])

                    # Here we are doing l+=1
                    # We can also do r-=1, it doesn't matter
                    # Since l is now not the old number, r will have to change accordingly since sum is no more 0
                    # Only thing we have to make sure is that l is not the same
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    compute = solution.threeSum(nums)

    # nums = [2, 7, 11, 15]
    # target = 9
    # compute = solution.twoSum(nums, target)
    print(compute)

