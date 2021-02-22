#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        first = arr[0]
        last = arr[-1]
        small = first + k
        big = last
        if last-k>0:
            big = last - k
        arr[0] = small
        arr[-1] = big    
        ans = big - small
        print(arr)

        for i in range(1, n-1):
            new_big = arr[i] + k
            new_small = arr[i] - k

            if new_small<0:
                arr[i] = new_big
                pass

            if new_small>=small and new_big<=big:
                arr[i] = new_small
            elif new_small>small and new_big>big:
                arr[i] = new_small
            elif new_small<small and new_big<big:
                arr[i] = new_big
            else:
                if abs(new_small - small) > abs(new_big - big):
                    arr[i] = new_big
                else:
                    arr[i] = new_small
        print(arr)
        arr.sort()
        print(arr)
        ans = arr[-1] - arr[0]
        return ans            



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends