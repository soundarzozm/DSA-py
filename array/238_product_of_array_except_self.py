class Solution:
    def productExceptSelf(self, nums):

        # So the logic is that prefixArray will have the products of all elements to the left of the current element
        # and suffix array will have the products of all elements to the right of the current element
        # So for every element in i-th index, prefixArray[i] contains product of all elements from left till i
        # and suffixArray[i] contains product of all elements from right till i
        # So prefixArray[i] x suffixArray[i] = answer[i]
        prefixArray = []
        suffixArray = []
        ans = []

        # Populate prefixArray
        first = 1
        for num in nums:
            prefixArray.append(first)
            first = num * first

        # Populate prefixArray
        first = 1        
        for i in range(len(nums) - 1, -1, -1):
            suffixArray.append(first)
            first = nums[i] * first
        
        # Reverse suffixArray since the loop ran in reverse
        suffixArray = suffixArray[::-1]
        
        # Compute answer
        for i in range(len(nums)):
            ans.append(prefixArray[i] * suffixArray[i])

        return ans
	
    def productExceptSelfConstantMemory(self, nums):
		# Same logic as above, but it is given that the space taken by the output array does not count
        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix = prefix * nums[i]
		
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * suffix
            suffix = suffix * nums[i]

        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4]
    print(solution.productExceptSelf(nums))
    print(solution.productExceptSelfConstantMemory(nums))
