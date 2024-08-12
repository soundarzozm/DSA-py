class Solution:
    def twoSum(self, numbers, target):

        # Initialize left and right pointers
        l = 0
        r = len(numbers) - 1

        while l < r:

            # Calculate the current sum (for the current l and r values)
            s = numbers[l] + numbers[r]
            
            # If the sum == target, this is the answer.
            # Return the indices
            if s == target:
                return [l+1, r+1]
            
            # If the sum is less than the target, we need to increase the sum
            # Moving the left pointer to the right will increase the sum since the array is sorted
            elif s < target:
                l += 1

            # Similarly, decreasing the right pointer will decrease the sum
            else:
                r -= 1
        

if __name__ == "__main__":
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(numbers, target))