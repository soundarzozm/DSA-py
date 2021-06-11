import sys

def MCM(arr, i, j):

    if i>=j:
        return 0

    min_ans = INT_MAX

    for k in range(i, j):
        temp_ans = MCM(arr, i, k) + MCM(arr, k+1, j) + (arr[i-1] * arr[k] * arr[j])
        min_ans = min(min_ans, temp_ans)

    return min_ans 

if __name__=="__main__":
    arr = [40, 20, 30, 10 ,30]
    n = len(arr)

    INT_MAX = sys.maxsize

    print(MCM(arr, 1 , n-1))