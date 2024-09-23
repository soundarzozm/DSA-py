class Solution:
    def binarySearch(self, arr, target):
        leftPointer = 0
        rightPointer = len(arr) - 1

        while leftPointer <= rightPointer:

            middlePointer = (leftPointer + rightPointer) // 2

            if arr[middlePointer] == target:
                return middlePointer

            elif arr[middlePointer] < target:
                leftPointer = middlePointer + 1

            else:
                rightPointer = middlePointer - 1

        return -1

if __name__ == "__main__":
    solution = Solution()
    arr = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(solution.binarySearch(arr, target))
