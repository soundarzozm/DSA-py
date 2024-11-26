class MinStack:
# What is a min stack? What is a monotonically decreasing stack? They're the same
# The elements in these data structures are in decreasing order only.
# So, the top element will logically be the smallest

    def __init__(self):
        # We are going to use a standard stack
        # But instead of adding elements directly, we add a tuple (element, min. element till now)
        self.stack = []

    def push(self, val):
        if self.stack:
            self.stack.append((val, min(val, self.stack[-1][1])))
        else:
            self.stack.append((val, val))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
