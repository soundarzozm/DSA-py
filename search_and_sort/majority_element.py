
class Solution:
    def majorityElement(self, A, N):
        
        A.sort()
        
        if len(A)==1:
            return A[0]
        
        last = A[0]
        cnt = 1
        lim = N//2
        flag = 0
        
        for i in range(1, N):
            if A[i] == last:
                cnt+=1
            else:
                last = A[i]
                cnt = 1
            if cnt>lim:
                flag = 1
                break
        
        if flag == 0:
            return -1
        return last
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends