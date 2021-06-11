import sys

def palindromePartition(s, i, j):

    #Base case
    if i>=j or isPalindrome(s[i:j+1]):
        return 0

    mn = INT_MAX

    if t[i][j]!=-1:
        return t[i][j]

    for k in range(i, j):
        if t[i][k]!=-1:
            left = t[i][k]
        else:
            left = palindromePartition(s, i, k)

        if t[k+1][j]!=-1:
            right = t[k+1][j]
        else:
            right = palindromePartition(s, k+1, j)

        temp_ans = 1 + left + right
        mn = min(mn, temp_ans)
        t[i][j] = mn

    return t[i][j]

def isPalindrome(s):
    if s==s[::-1]:
        return True
    return False

if __name__=="__main__":
    s = "ababbbabbababa"
    n = len(s)

    INT_MAX = sys.maxsize

    t = [[-1 for i in range(n+1)] for j in range(n+1)]

    print(palindromePartition(s, 0 , n-1))