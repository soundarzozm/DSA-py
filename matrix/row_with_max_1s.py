#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
	    
	    flag = False
	    row = 0
	    ind = m
	    
	    for i in range(n):
	        for j in range(m):
	            if arr[i][j]==1:
	                ind = j
	                flag = True
	                row = i
	                break
	        if flag==True:
	            break
	       
	    row2 = row   
	    while (ind>0 and row<n):
	        if arr[row][ind-1]==1:
	            ind = ind - 1
	            row2 = row
	        else:
	            row = row + 1
	            	
	if flag:
            return row2
        
        else:    
            return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends
