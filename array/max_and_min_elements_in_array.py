# Finding the maximum and minimum element in the array
# TIME - O(n)
# SPACE - O(1)
import sys

# Store INT_MAX and INT_MIN values
max_size = sys.maxsize
min_size = -sys.maxsize - 1


def findMaxAndMin(arr, n):
    # Initialize the maxElement and minElement variables with INT_MIN and INT_MAX respectively
    minElement = max_size
    maxElement = min_size

    # Iterate through the array and with each pass, compare the element with minElement and maxElement and replace wherever required
    for i in arr:
        if i > maxElement:
            maxElement = i
        if i < minElement:
            minElement = i

    return maxElement, minElement


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        print(findMaxAndMin(arr, n))
