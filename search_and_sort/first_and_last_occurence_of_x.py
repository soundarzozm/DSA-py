for _ in range(int(input())):
    
    n, x = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    flag = 0
    start = -1
    
    for i in range(n):
        
        if arr[i]==x and flag==0:
            start = i
            flag = 1
            
        if arr[i]!=x and flag==1:
            end = i-1
            break
    
    if start==-1:
        print(-1)
    else:    
        print(str(start)+" "+str(end))    