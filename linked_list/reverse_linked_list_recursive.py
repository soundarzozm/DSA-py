#function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

# This function should reverse linked list and return
# head of the modified linked list
def reverseList(head):
    
    prev = None
    next1 = head.next

    def reverse(curr, prev, next1):

        if next1==None:
            curr.next = prev
            return curr

        next1 = curr.next
        curr.next = prev
        prev = curr
        curr = next1
        next1 = curr.next

        """print("curr", curr.data)
        print("prev", prev.data)
        
        if next1:
            print("next", next1.data)"""

        return reverse(curr, prev, next1)    

    head = reverse(head, prev, next1)

    return head

    





#{ 
#  Driver Code Starts
# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = reverseList(lis.head)
        printList(newHead)

# } Driver Code Ends