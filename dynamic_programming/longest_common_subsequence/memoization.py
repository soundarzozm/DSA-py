import numpy as np

def LCS(x, y, m, n):

    #Base Case
    if n==0 or m==0:
        return 0

    #Check if in DP Matrix
    if t[m][n]!=-1:
        return t[m][n]

    #Choice Diagram
    if x[m-1]==y[n-1]:
        t[m][n] = 1 + LCS(x, y, m-1, n-1)
    else:
        t[m][n] = max(LCS(x, y, m, n-1), LCS(x, y, m-1, n))

    return t[m][n]

if __name__=="__main__":

    x = ""
    m = 0

    y = ""
    n = 0

    t = [[-1] * (n+1)] * (m+1)
    t = np.array(t)

    print(LCS(x, y, m, n))
