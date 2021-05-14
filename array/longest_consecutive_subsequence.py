
 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        
        dick = {}

        for i in arr:
            dick[i]=1

        cnt = 0
        maxCnt = 0

        for i in range(1, max(arr)+1):
            try:
                if dick[i]==1:
                    cnt+=1
            except:
                maxCnt = max(cnt, maxCnt)
                cnt = 0
        
        maxCnt = max(cnt, maxCnt)
        
        return maxCnt

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends