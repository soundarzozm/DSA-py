class Solution:
    def largestRectangleArea(self, heights):
        # Use a monotonic increasing stack
        length = len(heights)
        stack = []
        maxArea = 0

        for i in range(length):
            # If stack is not empty, we are going to compare the height with the
            # topmost element of the stack (the maximum height till now)
            if stack:

                # If the current height is greater than the greatest element in the
                # stack, just add [current index, current height] to the stack
                if heights[i] >= stack[-1][1]:
                    stack.append([i, heights[i]])

                # This is where the trick is
                # Keep popping out elements from the stack until you get an element
                # with height lesser than current height
                # With every pop, compute the maxArea
                # Once done, add [index of last top element, current height] to the stack
                else:
                    while stack and heights[i] < stack[-1][1]:
                        curr = stack.pop()
                        maxArea = max(maxArea, (i - curr[0]) * curr[1])
                    stack.append([curr[0], heights[i]])

            # If stack is empty, just add [current index, current height] to the stack
            else:
                stack.append([i, heights[i]])

        while stack:
            curr = stack.pop()
            maxArea = max(maxArea, (length - curr[0]) * curr[1])

        return maxArea

if __name__ == "__main__":
    solution = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    compute = solution.largestRectangleArea(heights)

    print(compute)
