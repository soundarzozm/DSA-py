class Solution:
    # This is one very messed up algorithm using recursion
    # We split the array (by indices) into halves until we are left with only one element per half
    # Then we compare the values of the leaf nodes and modify the array in-place

    def sortArray(self, nums):
        # This is the initial call over the entire array
        left = 0
        right = len(nums) - 1

        self.mergeSort(nums, left, right)

        return nums

    def mergeSort(self, nums, left, right):

        # Base Case
        if left == right:
            return

        mid = (left + right) // 2

        # Call mergeSort on the left half and the right half
        # We expect the algorithm to have sorted both the halves
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)

        # We merge both the halves in-place
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        # This is the merge method which compares values and modifies the array in-place

        tempArray = []

        leftPointer = left
        rightPointer = mid + 1

        while leftPointer <= mid and rightPointer <= right:
            if nums[leftPointer] <= nums[rightPointer]:
                tempArray.append(nums[leftPointer])
                leftPointer += 1
            else:
                tempArray.append(nums[rightPointer])
                rightPointer += 1


        while leftPointer <= mid:
            tempArray.append(nums[leftPointer])
            leftPointer += 1

        while rightPointer <= right:
            tempArray.append(nums[rightPointer])
            rightPointer += 1

        for i in range(left, right + 1):
            nums[i] = tempArray[i - left]


if __name__ == "__main__":
    solution = Solution()
    nums = [9, 8, 7, 6, 5]
    print(solution.sortArray(nums))
