for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    locsum = arr[0]
    glosum = arr[0]
    
    for i in range(1, n):
        
        locsum = max(arr[i], locsum + arr[i])
        
        if locsum > glosum:
            glosum = locsum
            
        #if sum goes below 0
        if locsum < 0:
            locsum = 0
    
    print(glosum)  
