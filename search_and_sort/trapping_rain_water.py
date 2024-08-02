class Solution:
    def trap(self, height):
        # O(n) Space
        # maxLeft = [0] * len(height)
        # maxRight = [0] * len(height)
        # minArray = [0] * len(height)
        # ansArray = [0] * len(height)

        # # Prefix Array
        # maxCount = 0
        # for i in range(len(height)):
        #     maxLeft[i] = maxCount
        #     maxCount = max(maxCount, height[i])

        # # Suffix Array
        # maxCount = 0
        # for i in range(len(height)-1, -1, -1):
        #     maxRight[i] = maxCount
        #     maxCount = max(maxCount, height[i])

        # for i in range(len(minArray)):
        #     minArray[i] = min(maxLeft[i], maxRight[i])

        # for i in range(len(minArray)):
        #     ansArray[i] = max(minArray[i] - height[i], 0)

        # return sum(ansArray)

        # O(1) Space
        ans = 0
        l = 0
        r = len(height) - 1

        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                ans += max(0, min(maxLeft, maxRight) - height[l])
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                ans += max(0, min(maxLeft, maxRight) - height[r])
                maxRight = max(maxRight, height[r])

        return ans

if __name__ == "__main__":
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    compute = solution.trap(height)
    print(compute)
