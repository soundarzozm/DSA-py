import numpy as np

def longestCommonSubstring(x, y, m, n):

    #Base Case
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j] = 0

    #Choice Diagram
    result = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1]==y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
                result = max(result, t[i][j])
            else:
                t[i][j] = 0
    return result

if __name__=="__main__":

    x = "abcdef"
    m = len(x)

    y = "abxefgzzzz"
    n = len(y)

    #Initialization
    t = [[None] * (n+1)] * (m+1)
    t = np.array(t)

    print(longestCommonSubstring(x, y, m, n))
