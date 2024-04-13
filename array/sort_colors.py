# Finding an array of 0s, 1s, and 2s
# Also known as dutch flag algorithm
# This is a single pass algorithm
# TIME - O(n)
# SPACE - O(1)

def sortColors(arr, n):
    # Initialize pointers with respective values
    # l - LEFT (first index)
    # m - MIDDLE (first index)
    # r - RIGHT (last index)
    l = 0
    m = 0
    r = n-1

    while m <= r:
        # If the mth element is 0, we swap lth element with mth
        # Increment l by 1 since the previous element is final
        # Increment m by 1 to check for the next element
        if arr[m] == 0:
            buffer = arr[l]
            arr[l] = arr[m]
            arr[m] = buffer
            l += 1
            m += 1

        # If the mth element is 2, we swap rth element with mth
        # Decrement r by 1 since the next element is final
        # TRICKY: Do not increment m by 1 since we don't know what the newly swapped value is yet
        elif arr[m] == 2:
            buffer = arr[r]
            arr[r] = arr[m]
            arr[m] = buffer
            r -= 1

        # If the mth element is 1, just increment m by 1 to check the next element
        else:
            m += 1

    return arr


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        print(sortColors(arr, n))
