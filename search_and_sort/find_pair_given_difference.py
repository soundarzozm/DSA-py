for _ in range(int(input())):
    
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    flag = 0
    
    dick = {}
    
    for i in range(n):
        dick[arr[i]]=1
        
    for i in arr:
        if (i+d in dick) or (i-d in dick):
            flag =1
            print("1")
            break
    
    if flag==0:
        print("-1")  