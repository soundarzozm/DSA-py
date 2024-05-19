def sortBySign(arr):
    n = 0
    p = 0

    while p < len(arr):
        if arr[p] < 0:
            buffer = arr[p]
            arr[p] = arr[n]
            arr[n] = buffer
            n += 1
        else:
            p += 1
    
    return arr


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        print(sortBySign(arr))