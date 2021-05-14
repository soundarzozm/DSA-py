for _ in range(int(input())):

    n = int(input())
    k = int(input())
    arr = list(map(int, input().split()))

    print([i for i in set(arr) if arr.count(i) > len(arr)//k][0])