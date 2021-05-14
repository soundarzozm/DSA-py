#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        
        sum1 = k
        dick = {}
        cnt = 0
        
        for i in arr:
            try:
                dick[i] += 1
            except:
                dick[i] = 1
        
        
        for i in range(n):
            try:
                if (sum1%2==0) and (arr[i] == sum1//2):
                    cnt += dick[sum1-arr[i]] - 1
                else:
                    cnt += dick[sum1-arr[i]]    
            except:
                pass
        
        #print(dick)

        return cnt//2

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends