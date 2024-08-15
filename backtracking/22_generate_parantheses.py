class Solution:
    def generateParanthesis(self, n):

        # openCount contains the number of opening brackets in stack
        # closeCount contains the number of closing brackets in stack
        openCount = 0
        closeCount = 0
        stack = []
        ans = []

        def backtrack(openCount, closeCount):

            # Base Case - it is solved
            # All the opening and closing brackets are used
            if openCount == closeCount == n:
                ans.append("".join(stack))
                return

            # Solve for all choices
            # First we check if it is possible to add opening bracket
            if openCount < n:
                # We add opening bracket to the stack
                stack.append("(")
                # Then we call backtrack function again which will try to add more brackets (opening first, then closed)
                backtrack(openCount + 1, closeCount)
                # This is important. We remove the opening bracket we just added and try adding closing bracket below (if possible)
                stack.pop()

            # We cannot add more closing brackets than existing opening brackets
            if closeCount < openCount:
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()

        backtrack(openCount, closeCount)
        return ans

if __name__ == "__main__":
    solution = Solution()
    n = 4
    compute = solution.generateParanthesis(n)
    print(compute)
