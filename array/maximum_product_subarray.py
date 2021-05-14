#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
    def maxProduct(self,arr, n):
        
        maxVal = 1
    	minVal = 1
        
        maxProd = max(arr)

        for i in range(n):
            
            if arr[i]<0:
                temp = maxVal
                maxVal = minVal
                minVal = temp
                
	        maxVal = max(arr[i], maxVal * arr[i])
            minVal = min(arr[i], minVal * arr[i])
            
            maxProd = max(maxProd, maxVal)       

        return maxProd
#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
