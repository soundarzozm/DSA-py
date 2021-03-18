#User function Template for python3


class Solution:
    def minFlips(self, S):
        
        cnt0 = 0
        cnt1 = 0
        
        for i in range(len(S)):
            x = S[i]
            if i%2==0:
                if x == "0":
                    cnt1 += 1
                else:        
                    cnt0 += 1
            else:
                if x == "0":
                    cnt0 += 1
                else:        
                    cnt1 += 1
                    
        return min(cnt0, cnt1)                


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends