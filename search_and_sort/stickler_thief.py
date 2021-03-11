#User function Template for python3

def FindMaxSum(arr, n):
    '''
    :param a:  given list of values
    :param n: size of a
    :return: Integer
    '''
    
    excl = 0
    incl_old = arr[0]
    
    if n==1 or n==2:
        return max(arr)
    
    for i in range(1, n):
        
        incl = excl + arr[i]
        excl = max(excl, incl_old)

        incl_old = incl
        
    return max(incl, excl)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        print(FindMaxSum(a,n))
# } Driver Code Ends