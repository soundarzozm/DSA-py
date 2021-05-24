#User function Template for python3
class Solution:
    def smallestNumber (self, S, D):
        
        num = [1]
        num += ([0]*(D-1))
        
        i = D-1
        ans = ""
        
        try:
            while sum(num)!=S or i<0:
            
            
                if sum(num)<S:
                    num[i] = 9

                elif sum(num)>S:    
                    num[i+1] = num[i+1] - (sum(num) - S)
                    break
            
                i -= 1
        except:
            return -1
        
        #print(num)
        
        for i in num:
            ans += str(i)
        
        return ans    
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends