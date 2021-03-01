#User function Template for python3

class Solution:
    def countSquares(self, N):
        if N == 0 or N == 1:
            return 0
        
        x = N**(1/2)

        if int(x)**2==N:
            return int(x)-1
        else:
            return int(x)    
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends