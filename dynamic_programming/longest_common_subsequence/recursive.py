def longestCommonSubsequence(x, y, m, n):

    #Base Condition
    if m==0 or n==0:
        return 0
    
    #Choice Diagram -> Smaller Input
    if x[m-1] == y[n-1]:
        return (1 + longestCommonSubsequence(x, y, m-1, n-1))
    else:
        return max(longestCommonSubsequence(x, y, m, n-1), longestCommonSubsequence(x, y, m-1, n))

if __name__=="__main__":
    
    x = ""
    m = 0

    y = ""
    n = 0

    print(longestCommonSubsequence(x, y, m, n))
