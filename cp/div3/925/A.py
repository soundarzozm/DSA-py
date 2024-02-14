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
def solve(n):
    l1, l2, l3 = 1, 1, 1

    if n <= 27:
        l1 = 1
        l2 = 1
        l3 = n-2

    if n > 27:
        l3 = 26
        l2 = max(1, n-27)
        l1 = 1

    if n > 52:
        l2 = 26
        l1 = n-52
    
    if n > 77:
        l1 = 26

    return chr(l1+96)+chr(l2+96)+chr(l3+96)

if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        print(solve(n))