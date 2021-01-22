for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    
    arr.sort()
    
    mins = arr[n-1] - arr[0]
    
    i=0
    for j in range(0+m-1, n):
        mins = min(mins, arr[j] - arr[i])
        i+=1
        
    print(mins)    