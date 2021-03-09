#User function Template for python3

def search(arr, l_out, h_out, key):
    
    pivot = h_out
    
    for i in range(h_out):
        if arr[i+1]<arr[i]:
            pivot = i
            break
    
    if key == arr[pivot]:
        return pivot
    
    a1 = arr[:pivot]
    a2 = arr[pivot:]
    
    ans1 = binSearch(a1, key)
    ans2 = binSearch(a2, key)
    
    if ans1==ans2:
        return -1
    
    if ans2==-1:
        return ans1
    else:
        return ans2 + len(a1)

        
    
def binSearch(a, x):

    l_in = 0
    h_in = len(a) - 1
 
    while l_in <= h_in:
 
        m_in = (h_in + l_in) // 2
 
        if a[m_in] < x:
            l_in = m_in + 1
 
        elif a[m_in] > x:
            h_in = m_in - 1
 
        else:
            return m_in
 
    return -1 
            
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        
        print(search(A, 0, n - 1, k))
# } Driver Code Ends