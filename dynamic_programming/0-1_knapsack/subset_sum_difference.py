import numpy as np

def minSubsetDiff(wt, n, W):

    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                t[i][j]=False
            if j==0:
                t[i][j]=True

    for i in range(1, n+1):
        for j in range(1, W+1):

            if wt[i-1]<=j:
                t[i][j] = (t[i-1][j-wt[i-1]]) or (t[i-1][j])

            else:
                t[i][j] = t[i-1][j]

    min1 = 999999
    print(t)
    for ind in range(int(len(t[-1])/2)):
        if t[-1][ind]==True:
            min1 = min(min1, sum - 2*ind)
    return min1


if __name__=="__main__":
    arr = [1, 2, 7]
    sum = sum(arr)
    n = 3

    t = [[None] * (sum+1)] * (n+1)

    t = np.array(t)

    print(minSubsetDiff(arr, n, sum))
