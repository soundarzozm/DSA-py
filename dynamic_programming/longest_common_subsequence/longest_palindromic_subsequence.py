import numpy as np

def LCS(x, y, m, n):

    #Base Case
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j] = 0

    #Choice Diagram
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1]==y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

    return t[m][n]

if __name__=="__main__":

    x = "agbcba"
    y = x[::-1]
    m = len(x)
    n = m

    #Initialization
    t = [[None] * (n+1)] * (m+1)
    t = np.array(t)

    print(LCS(x, y, m, n))
