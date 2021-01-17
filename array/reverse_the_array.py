for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    def rev_list(arr, start, end):
        
        if start>=end:
            return
            
        arr[start], arr[end] = arr[end], arr[start]
        
        rev_list(arr, start+1, end-1)
    
    rev_list(arr, 0, n-1)
    
    for x in range(n-1):
        print(arr[x], end=" ")
    print(arr[n-1], end="\n")    