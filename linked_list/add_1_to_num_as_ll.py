#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        
        def reverseList(head):
            curr = head
            prev = None
            next1 = head
            while next1!=None:
                next1 = curr.next
                curr.next = prev
                prev = curr
                curr = next1
            head = prev
            return head
        
        head = reverseList(head)
        head1 = head
        carry = 1
        
        while head1 and head1.next:
            head1.data = head1.data + carry
            carry = 0
            
            if head1.data>9:
                head1.data = head1.data%10
                carry = 1
            
            head1 = head1.next
            
        if carry!=0:
            head1.data += carry
        
        head = reverseList(head)
        
        return head
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends