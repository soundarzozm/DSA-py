import sys

def palindromePartition(s, i, j):

    #Base case
    if i>=j or isPalindrome(s[i:j+1]):
        return 0

    mn = INT_MAX

    #Loop
    for k in range(i, j):
        temp_ans = 1 + palindromePartition(s, i, k) + palindromePartition(s, k+1, j)
        mn = min(mn, temp_ans)

    return mn

def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False

if __name__=="__main__":
    string = "ababbbabbababa"
    n = len(string)

    INT_MAX = sys.maxsize

    print(palindromePartition(string, 0, n-1))