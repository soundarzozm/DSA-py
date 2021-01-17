#User function Template for python3

def sort012(arr,n):
    
    p0 = 0
    p1 = 0
    p2 = n-1
    
    for i in range(n):
        
        if arr[p1]==0:
            arr[p0], arr[p1] = arr[p1], arr[p0]
            p0+=1
            p1+=1
        elif arr[p1]==1:
            p1+=1
        else:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p2-=1
    
    return arr        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends