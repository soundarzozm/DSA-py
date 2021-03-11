#User function Template for python3

class Solution:
    def inSequence(self, start, term, diff):
        
        if term==start:
            return 1
            
        if diff == 0:
            return 0
        
        x = (term - start)/diff
        
        if x - int(x)>0:
            return 0
            
        if x!=abs(x):
            return 0
            
        return 1    
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B, C = [int(x) for x in input().split()]
        
        ob = Solution();
        print(ob.inSequence(A, B, C))
# } Driver Code Ends