#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def addLists(first, second):
    
    def reverseList(head):
    
        prev = None
        current = head

        while(current is not None):
        
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        
        head = prev

        return head
        
    first = reverseList(first)
    second = reverseList(second)
    
    result = LinkedList()
    
    carry = 0
    
    while ((first!=None or second!=None) or carry != 0):
        
        if first==None and second!=None:
            bruh = second.data + carry
            second = second.next
        elif first!=None and second==None:
            bruh = first.data + carry
            first = first.next
        elif first!=None and second!=None:
            bruh = first.data + second.data + carry
            first = first.next
            second = second.next
        else:
            bruh = carry
        
        if bruh > 9:
            carry = 1
            bruh = bruh%10
        else:
            carry = 0
            
        result.insert(bruh)
        
    return reverseList(result.head)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = addLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends