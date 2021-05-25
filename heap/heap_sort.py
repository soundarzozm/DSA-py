#User function Template for python3
class MinHeap:

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
        self.heapifyUpRecursive(self.size - 1)

    def heapifyUpRecursive(self, index):
        
        if (self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUpRecursive(self.getParentIndex(index))

    def removeMin(self):

        if (self.size == 0):
            raise("Empty heap")

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.storage[self.size - 1] = 0
        self.size -= 1
        self.heapifyDownRecursive(0)
        return data

    def heapifyDownRecursive(self, index):

        smallest = index

        if (self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index)):
            smallest = self.getLeftChildIndex(index)

        if (self.hasRightChild(index) and self.storage[smallest] > self.rightChild(index)):
            smallest = self.getRightChildIndex(index)

        if (smallest != index):
            self.swap(index, smallest)
            self.heapifyDownRecursive(smallest)


class Solution:
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        
        heap = MinHeap(n)
        
        for i in arr:
            heap.insert(i)
        
        for i in range(n):
            arr[i] = heap.removeMin()
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends