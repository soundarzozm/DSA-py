#User function Template for python3
class MaxHeap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [0]*capacity
        self.size = 0

    def getParentIndex(self, index):
        return ((index-1) // 2)

    def getLeftChildIndex(self, index):
        return ((2*index) + 1)

    def getRightChildIndex(self, index):
        return ((2*index) + 2)

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def insert(self, data):
        
        if self.isFull():
            raise("Heap is full")  

        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)

    def heapifyUp(self, index):
        
        if (self.hasParent(index) and self.parent(index) < self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))

    def removeMax(self):

        if (self.size == 0):
            raise("Empty heap")

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.storage[self.size - 1] = 0
        self.size -= 1
        self.heapifyDown(0)
        return data

    def heapifyDown(self, index):

        largest = index

        if (self.hasLeftChild(index) and self.storage[largest] < self.leftChild(index)):
            largest = self.getLeftChildIndex(index)

        if (self.hasRightChild(index) and self.storage[largest] < self.rightChild(index)):
            largest = self.getRightChildIndex(index)

        if (largest != index):
            self.swap(index, largest)
            self.heapifyDown(largest)

class Solution:

	def kLargest(self,arr, n, k):
	    
	    heap = MaxHeap(n)
	    
	    for i in arr:
	        heap.insert(i)
	        
	    res = []
	    
	    for i in range(k):
	        res.append(heap.removeMax())
	        
	    return res
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends