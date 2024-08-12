class Solution:
    def maxArea(self, heights):
        # We follow the same logic as two sum II
        ans = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            
            # This is the only extra step
            # We compute the maximum area till now
            ans = max(ans, min(heights[l], heights[r]) * (r - l))

            # Move the lower pointer
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return ans

if __name__ == "__main__":
    solution = Solution()
    heights = []
    print(solution.maxArea(heights))