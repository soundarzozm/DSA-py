def knapsack(wt, val, n, W):

    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                t[i][j]=0

    for i in range(1, n+1):
        for j in range(1, W+1):

            if wt[i-1]<=j:
                t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])

            else:
                t[i][j] = t[i-1][j]

    return t[n][W]


if __name__=="__main__":
    wt = []
    val = []
    W = 0
    n = 0

    t = []

    for i in range(n+1):
        for j in range(W+1):
            t[i][j]=-1

    print(knapsack(wt, val, n, W))