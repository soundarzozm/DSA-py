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
    if n == 1:
        return "YES"

    avg = sum(arr) // n
    cur = 0
    for i in range(n):
        if cur < 0 and arr[i] > avg:
            return "NO"
        cur += arr[i] - avg

    if cur == 0:
        return "YES"
    return "NO"

if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        arr = inlt()
        print(solve(n, arr))