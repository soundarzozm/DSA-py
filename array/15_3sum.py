class Solution:
    def threeSum(self, nums):
        ans = []

        # We have to sort the array to use the two sum II logic
        nums.sort()

        # Iterate to end - 2 because last two numbers will be processed automatically
        for i in range(len(nums) - 2):

            # We check if the next ith number is the same or not
            # We don't want to add repeated answers
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            # Initialize left and right pointers
            # Left will be the leftmost after i which is i+1
            # Right will be last index
            l = i + 1
            r = len(nums) - 1

            # Perform the two sum II logic
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s == 0:
                    ans.append([nums[i], nums[l], nums[r]])

                    # Can either do l+=1 or r-=1
                    # We just want to proceed ahead
                    l += 1

                    # Again check for repeated numbers
                    while l<r and nums[l-1] == nums[l]:
                        l += 1

                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums))