import numpy as np

def unboundedKnapsack(wt, val, n, W):

    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                t[i][j]=0

    for i in range(1, n+1):
        for j in range(1, W+1):

            if wt[i-1]<=j:
                t[i][j] = max(val[i-1] + t[i][j-wt[i-1]], t[i-1][j])

            else:
                t[i][j] = t[i-1][j]

    return t[n][W]


if __name__=="__main__":
    lt = [1, 2, 3, 4, 5]
    price = [3, 7, 2, 8, 9]
    N = 8
    n = len(price)

    t = [[None] * (N+1)] * (n+1)

    t = np.array(t)

    print(unboundedKnapsack(lt, price, n, N))