def reverse(S):
    stack = []
    rev = ""
    for i in S:
        stack.append(i)
    
    while len(stack)>0:
        rev += stack.pop()
    
    return rev

#{ 
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends