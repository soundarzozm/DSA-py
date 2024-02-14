import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

############ ---- Code Here ---- ############
def isEven(a):
    return a%2==0

def solve(a, b):
    if (not isEven(a) and not isEven(b)):
        return "No"

    if isEven(a) and isEven(b):
        return "Yes"
    
    if isEven(a):
        a, b = b, a
    
    # a is odd, b is even
    if b//2 == a:
        return "No"
    return "Yes"

if __name__ == "__main__":
    for _ in range(inp()):
        a, b = inlt()
        print(solve(a, b))