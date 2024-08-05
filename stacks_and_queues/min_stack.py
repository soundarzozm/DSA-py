# So the concept is to create two stacks
# Stack - Usual stack to store the values
# MinStack - To store the "minimum value till then" such that every position contains the minimum value till that position in the main stack

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        
        # We are checking if stack is empty or not
        # stack and minStack will have the same length always since we are pushing and popping together
        # If stack is empty, just add the value since it's the first value
        # Otherwise, check the minimum till that value and add that (which is already in current-1 position)
        # EZ
        if self.minStack:
            val = min(val, self.minStack[-1])

        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

if __name__ == "__main__":
    myStack = MinStack()

    myStack.push(1)
    myStack.push(5)
    myStack.push(2)

    myStack.pop()

    print(myStack.top())
    print(myStack.getMin())
