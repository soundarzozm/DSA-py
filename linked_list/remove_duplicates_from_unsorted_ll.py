#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        
        main = head
        
        if head.next == None:
            return head
        
        head1 = head.next
        
        main.next = None
        
        dick = {}
        dick[head.data]=1
        
        while head1 and head1.next:
            
            try:
                dick[head1.data]+=1
                head1 = head1.next
            except:
                dick[head1.data]=1
                main.next = head1
                head1 = head1.next
                main = main.next
                main.next = None
        
        if head1.data not in dick.keys():
            main.next = head1

        return head        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha

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
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print(' ')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        a.head = Solution().removeDuplicates(a.head)
        a.printList()
# } Driver Code Ends