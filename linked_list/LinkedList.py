class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self, node):
        self.head = node

    def addNode(self, node):
        pointer = self.head

        while pointer.next:
            pointer = pointer.next

        pointer.next = node

    def printList(self):
        pointer = self.head

        while pointer:
            if pointer.next:
                print(pointer.val, "--> ", end="")
            else:
                print(pointer.val)
            pointer = pointer.next

if __name__ == "__main__":
    firstNode = ListNode(1)
    myLinkedList = LinkedList(firstNode)
    myLinkedList.printList()

    myLinkedList.addNode(ListNode(2))
    myLinkedList.addNode(ListNode(3))

    myLinkedList.printList()
