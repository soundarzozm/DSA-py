# NOT WORKING

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
def solve(n, arr):
    x = 0
    
    for i in range(n-1):
        s = set()
        for j in range(0, n):
            if abs(arr[j] - arr[i]) < n and abs(arr[j] - arr[i]) > 0:
                s.add(abs(arr[j] - arr[i]))
        
        x = max(x, len(s))

    return x+1

if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        arr = inlt()
        print(solve(n, arr))