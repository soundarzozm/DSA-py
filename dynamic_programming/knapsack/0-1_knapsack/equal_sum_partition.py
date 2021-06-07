import numpy as np

def subsetSum(wt, n, W):

    for i in range(n+1):
        for j in range(W+1):
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

    return t[n][W]


if __name__=="__main__":
    arr = [5, 11, 5, 3]
    arrSum = sum(arr)

    if arrSum%2 != 0:
        print("False")
        exit()

    sum = int(arrSum/2)

    n = 4

    t = [[None] * (sum+1)] * (n+1)

    t = np.array(t)

    print(subsetSum(arr, n, sum))