#User function Template for python3

def spirallyTraverse(matrix, r, c): 
    
    row0 = 0
    col0 = 0
    row1 = len(matrix)
    col1 = len(matrix[0])
    result = []
    
    def spiral_traverse(matrix, row0, row1, col0, col1):
        
        if (row0>=row1 or col0>=col1):
            return result
        
        for i in range(row0, col1):
            result.append(matrix[row0][i])
        
        for i in range(row0+1, row1):
            result.append(matrix[i][col1-1])
            
        if row0 != row1-1:
            for i in range(col1-2, col0-1, -1):
                result.append(matrix[row1-1][i])
                
        if col0 != col1-1:
            for i in range(row1-2, row0, -1):
                result.append(matrix[i][col0])
        
        spiral_traverse(matrix, row0+1, row1-1, col0+1, col1-1)
    
    spiral_traverse(matrix, row0, row1, col0, col1)    
    
    return result
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        ans = spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends