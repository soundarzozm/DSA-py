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

    #Initialization
    s = ""
    i = m
    j = n

    #Build the string
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            s += x[i-1]
            i-=1
            j-=1
        else:
            if t[i][j-1]>t[i-1][j]:
                j-=1
            else:
                i-=1

    return s[::-1]

if __name__=="__main__":

    x = "abcdef"
    m = len(x)

    y = "abxef"
    n = len(y)

    #Initialization
    t = [[None] * (n+1)] * (m+1)
    t = np.array(t)

    print(LCS(x, y, m, n))
