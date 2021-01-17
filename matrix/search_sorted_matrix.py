#User function Template for python3
class Solution:
	def matSearch(self, arr, N, M, X):
		for i in range(N):
		    if arr[i][M-1]<X:
		        pass
		    elif arr[i][M-1]==X:
		        return 1
		    else:
		        for j in arr[i]:
		            if j==X:
		                return 1
        return 0	        
		        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))
# } Driver Code Ends