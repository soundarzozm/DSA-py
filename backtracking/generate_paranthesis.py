class Solution:
    def generateParanthesis(self, n):
        openCount = 0
        closeCount = 0
        stack = []
        ans = []

        def backtrack(openCount, closeCount):

            # Base Case - it is solved
            if openCount == closeCount == n:
                ans.append("".join(stack))
                return

            # Solve for all choices
            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closeCount)
                stack.pop()

            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()

        backtrack(0, 0)
        return ans

if __name__ == "__main__":
    solution = Solution()
    n = 4
    compute = solution.generateParanthesis(n)
    print(compute)
