def findLoopHead(head):
     
    if (head == None or head.next == None):
        return None
  
    slow = head
    fast = head
  
    slow = slow.next
    fast = fast.next.next
  
    while (fast and fast.next):
        if (slow == fast):
            break
         
        slow = slow.next
        fast = fast.next.next
  
    if (slow != fast):
        return None
  
    slow = head
     
    while (slow != fast):
        slow = slow.next
        fast = fast.next

    return slow