#array's question regarding stock price solved in O(n) instead of O(n^2)

for _ in range(int(input())):
    
    result = []
    n = int(input())
    arr = list(map(int, input().split()))
    start = end = 0

    for i in range(1, n-1):
        if arr[i] <= arr[start]:
            start = end = i
        else:
            end = i
            if arr[i+1] < arr[end]:
                result.append(start)
                result.append(end)
                start = i+1
            else:
                pass
    
    if arr[n-1] > arr[end]:
        result.append(start)
        result.append(n-1)
        
    if len(result)==0:
        print("No Profit")
        
    else:    
           
        for i in range(0, len(result)-2, 2):
            print("(", end="")
            print(result[i], end=" ")
            print(result[i+1], end=") ")
            
        print("(", end="")
        print(result[len(result)-2], end=" ")
        print(result[len(result)-1], end=")\n")
