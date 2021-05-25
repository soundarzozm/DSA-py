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
        #self.heapifyUpIterative()
        self.heapifyUpRecursive(self.size - 1)

    def heapifyUpIterative(self):

        index = self.size - 1

        while (self.hasParent(index) and self.parent(index) < self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def heapifyUpRecursive(self, index):
        
        if (self.hasParent(index) and self.parent(index) < self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUpRecursive(self.getParentIndex(index))

    def removeMax(self):

        if (self.size == 0):
            raise("Empty heap")

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.storage[self.size - 1] = 0
        self.size -= 1
        #self.heapifyDownIterative()
        self.heapifyDownRecursive(0)
        return data

    def heapifyDownIterative(self):

        index = 0

        while (self.hasLeftChild(index)):
            largerChildIndex = self.getLeftChildIndex(index)

            if (self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                largerChildIndex = self.getRightChildIndex(index)

            if (self.storage[index] < self.storage[largerChildIndex]):
                break
            else:
                self.swap(index, largerChildIndex)
            index = largerChildIndex

    def heapifyDownRecursive(self, index):

        largest = index

        if (self.hasLeftChild(index) and self.storage[largest] < self.leftChild(index)):
            largest = self.getLeftChildIndex(index)

        if (self.hasRightChild(index) and self.storage[largest] < self.rightChild(index)):
            largest = self.getRightChildIndex(index)

        if (largest != index):
            self.swap(index, largest)
            self.heapifyDownRecursive(largest)

if __name__ == "__main__":

    heap = MaxHeap(10)

    print(heap.storage)

    heap.insert(5)
    heap.insert(2)
    heap.insert(7)
    heap.insert(1)
    heap.insert(0)

    print(heap.storage)
    print(heap.removeMax())
    print(heap.storage)
    print(heap.removeMax())
    print(heap.storage)
    print(heap.removeMax())
    print(heap.storage)
    