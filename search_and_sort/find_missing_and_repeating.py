#User function Template for python3

class Solution:
    def findTwoElement(self, arr, n): 
        
        arr.insert(0, -1)
        
        for i in range(1, n+1):
            
            if (arr[abs(arr[i])] > 0):
                arr[abs(arr[i])] = -arr[abs(arr[i])]
            else:
                repeat = abs(arr[i])
                break
                
        for i in range(len(arr)):
            
            if arr[i]>0:
                miss = i
                break
        return [repeat, miss]    
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends