# Reversing an array
# TIME - O(n)
# SPACE - O(1)

def reverse(arr, n):
    # Use two pointers
    # l - Left pointer (initially the first index)
    # r - Right pointer (initally the last index)
    l = 0
    r = n-1

    # Iterate through half of the array, swapping the left value with the right value in each pass
    # When you reach the mid point, all the elements will be swapped
    while l < r:
        buffer = arr[l]
        arr[l] = arr[r]
        arr[r] = buffer
        l += 1
        r -= 1

    return arr


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        print(reverse(arr, n))
