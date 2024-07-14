class Solution:
    def searchMatrix(self, matrix, target):
        colArray = []

        for row in matrix:
            colArray.append(row[0])

        rowIdx = self.binarySearch(colArray, target)
        ansIdx = self.binarySearch(matrix[rowIdx], target)

        return matrix[rowIdx][ansIdx] == target


    def binarySearch(self, arr, target):
        l = 0
        r = len(arr) - 1
        ans = l

        while l <= r:
            m = (l + r) // 2

            if arr[m] > target:
                r = m - 1
            else:
                ans = m
                l = m + 1

        return ans

if __name__ == "__main__":
    matrix = [[-8,-7,-5,-3,-3,-1,1],[2,2,2,3,3,5,7],[8,9,11,11,13,15,17],[18,18,18,20,20,20,21],[23,24,26,26,26,27,27],[28,29,29,30,32,32,34]]
    target = -5

    case = Solution()

    print(case.binarySearch([-8,-7,-5,-3,-3,-1,1], -5))
    # print(case.searchMatrix(matrix, -5))
