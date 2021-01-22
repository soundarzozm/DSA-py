#User function Template for python3

class Solution:      
    
    def merge(self, arr1, arr2, n, m): 
        
        def nextGap(gap):
            if (gap == 1):
                return 0            
            return (gap // 2) + (gap % 2)
        
        gap = n + m   
        gap = nextGap(gap)
        
        while gap > 0:
 
            i = 0
            
            while i + gap < n:
                if (arr1[i] > arr1[i + gap]):
                    arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
                i += 1
 
            j = gap - n if gap > n else 0
            
            while i < n and j < m:
                if (arr1[i] > arr2[j]):
                    arr1[i], arr2[j] = arr2[j], arr1[i]
                i += 1
                j += 1
 
            if (j < m):
                j = 0
                while j + gap < m:
                    if (arr2[j] > arr2[j + gap]):
                        arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j] 
                    j += 1
 
            gap = nextGap(gap)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, m=map(int, (input().strip().split()))
        arr1=list(map(int , input().strip().split()))
        arr2=list(map(int , input().strip().split()))
        ob = Solution()
        ans=ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends