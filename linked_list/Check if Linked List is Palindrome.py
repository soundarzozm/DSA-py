#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
def isPalindrome(head):
    
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
        
    length = 0
    
    first = head
    ptr = head
    
    while(ptr):
        length += 1
        ptr = ptr.next
    
    second = head
    
    if length%2 != 0:
        for _ in range(int(length/2)+1):
            second = second.next
    else:
        for _ in range(int(length/2)):
            second = second.next
    
    second = reverseList(second)
    
    while (second):
        if second.data != first.data:
            return 0
        first = first.next
        second = second.next
    return 1        



#{ 
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra Jha

import atexit
import io
import sys

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
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends