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
        # Same logic as Two Sum II and Container with Most Water
        # If left is less, move left, otherwise move right

        # Approach this problem like a real life situation
        # How can you figure out how much water can be stored in a position?
        # By checking the maxLeft and maxRight values
        ans = 0
        l = 0
        r = len(height) - 1

        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1

                # Step - 1: Find the minimum of maxLeft and maxRight. This is our maxWater that can be stored
                # Step - 2: Subtract the current height from this value since we have to count the current height.
                # This is the actual water that can be stored.
                # Step - 3: If this goes negative, we need to take it as 0 since we can't have negative water
                ans += max(0, min(maxLeft, maxRight) - height[l])
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1

                # Same logic as above case
                ans += max(0, min(maxLeft, maxRight) - height[r])
                maxRight = max(maxRight, height[r])

        return ans

if __name__ == "__main__":
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    compute = solution.trap(height)
    print(compute)
