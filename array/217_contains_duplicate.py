class Solution:
    def hasDuplicate(self, nums):
        # So the approach is to create a set
        # Set can have only unique elements
        # If an element already exists in the set, it has been repeated so return True

        # Initialize set
        uniqueValues = set()

        # Run loop in nums
        for num in nums:

            # Check if the element already exists in the set
            # If it does, return True
            # Otherwise, add it to the set and move to the next iteration
            if num in uniqueValues:
                return True
            uniqueValues.add(num)

        # We will reach here only if the above return statement doesn't get executed
        # That means there have not been any repeated elements till now
        # So we return False
        return False

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 3]
    print(solution.hasDuplicate(nums))
