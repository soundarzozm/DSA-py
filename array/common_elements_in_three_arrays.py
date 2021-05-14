#User function Template for python3

class Solution:
    def commonElements (self, arr1, arr2, arr3, n1, n2, n3):
        
        result = []
        
        p1 = 0
        p2 = 0
        p3 = 0
        
        while (p1<n1 and p2<n2 and p3<n3):
            
            if arr1[p1] < arr2[p2]:
                p1+=1
            elif arr1[p1] > arr2[p2]:
                p2+=1
            elif arr1[p1] > arr3[p3]:
                p3+=1
            elif arr1[p1]<arr3[p3]:
                p1+=1
                p2+=1
            else:
                if arr1[p1] not in result:
                    result.append(arr1[p1])
                p1+=1
                p2+=1
                p3+=1
        
        return result


#{ 
#  Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends