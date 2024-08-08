class Solution:
    # Define mapping to reduce code
    parenthesesInverse = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

    def isValid(self, string):
        stack = []

        for s in string:
            
            # If it's an opening bracket, we add it to the stack
            if s == "(" or s == "[" or s == "{":
                stack.append(s)
                continue
            
            # The code below will be executed only when the current bracket is a closing bracket
            # If the stack is empty, we cannot have a closing bracket. Hence, we return False
            if not stack:
                return False
            
            # We pop out the topmost element and check if the current bracket is matching it and return False otherwise
            top = stack.pop()
            if self.parenthesesInverse[top] != s:
                return False
        
        # The string has been processed completely here. If the stack has anything left, that means they're invalid
        if stack:
            return False
        
        return True

if __name__ == "__main__":
    solution = Solution()
    string = "()[]{}("
    print(solution.isValid(string))
