def parameterized(s, e, arr):
    # Base Case
    if s >= e:
        return arr

    # Compute
    arr[s], arr[e] = arr[e], arr[s]
    
    # Recursion
    return parameterized(s+1, e-1, arr)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(parameterized(0, len(arr)-1, arr))