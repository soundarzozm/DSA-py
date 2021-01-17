#User function Template for python3

class Solution:
    def median(self, matrix, r, c):
    	
    	minx = 1001
    	maxx = 0
    	
    	for i in range(r):
    	    if matrix[i][0]<minx:
    	        minx = matrix[i][0]
    	    if matrix[i][c-1]>maxx:
    	        maxx = matrix[i][c-1]
    	
        def countSmall(matrix, minx, maxx):
    	    
            midx = int((minx+maxx)/2)
            count = 0
        
            for i in range(r):
                for j in range(c):
                    if matrix[i][j]<=midx:
                        count+=1
    	    
            if count==(r*c/2):
                return midx, midx
            elif count<(r*c/2):
                return 0, midx
    	    else:
    	        return 1001, midx
    	        
        x, midx = countSmall(matrix, minx, maxx)
        
        while(x==0 or x==1001):
            
            if x==0:
                x, midx = countSmall(matrix, midx, maxx)
            else:
                x, midx = countSmall(matrix, minx, midx)
    	    
    	return x          
        
         
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends