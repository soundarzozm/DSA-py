def knapsack(wt, val, n, W):

    if (n==0 or W==0):
        return 0

    if t[n][W] != -1:
        return t[n][W]

    if wt[n-1]<=W:
        t[n][W] = max(val[n-1]+knapsack(wt, val, n-1, W-wt[n-1]), knapsack(wt, val, n-1, W))
        return t[n][W]

    elif wt[n-1] > W:
        t[n][W]=knapsack(wt, val, n-1, W)
        return t[n][W]


if __name__=="__main__":
    wt = []
    val = []
    W = 0
    n = 0

    t = [[None] * (W+1)] * (n+1)


    print(knapsack(wt, val, n, W))