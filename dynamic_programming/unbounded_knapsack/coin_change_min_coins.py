import numpy as np

INT_MAX = 99999

def subsetSum(wt, n, W):

    for i in range(n+1):
        for j in range(sum+1):
            if j==0:
                t[i][j] = 0
            if i==0:
                t[i][j] = INT_MAX - 1
            if i==1 and j!=0:
                if j%wt[0]!=0:
                    t[i][j] = INT_MAX - 1
                else:
                    t[i][j] = int(j/wt[0])

    for i in range(2, n+1):
        for j in range(1, W+1):

            if wt[i-1]<=j:
                t[i][j] = min(t[i][j-wt[i-1]] + 1, t[i-1][j])

            else:
                t[i][j] = t[i-1][j]

    return t[n][W]


if __name__=="__main__":
    coins = [1, 2, 3]
    sum = 5
    n = len(coins)

    t = [[None] * (sum+1)] * (n+1)

    t = np.array(t)

    print(subsetSum(coins, n, sum))