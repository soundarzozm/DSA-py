class Solution:
    def evalRPN(self, tokens):
        stack = []
        operators = ("+", "-", "*", "/")

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()

                if token == "/":
                    stack.append(int(op1 / op2))
                elif token == "*":
                    stack.append(op1 * op2)
                elif token == "+":
                    stack.append(op1 + op2)
                else:
                    stack.append(op1 - op2)
        
        return stack[-1]

if __name__ == "__main__":
    solution = Solution()
    tokens = ["2","1","+","3","*"]
    print(solution.evalRPN(tokens))
