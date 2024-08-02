class Solution:
    def maxArea(self, heights):
        ans = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            ans = max(ans, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ans

if __name__ == "__main__":
    solution = Solution()
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    compute = solution.maxArea(heights)
    print(compute)
