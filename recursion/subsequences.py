def solution(idx, arr, curr):
    # Base Case
    if idx >= len(arr):
        print(curr)
        return None

    # Take
    curr += arr[idx]
    solution(idx+1, arr, curr)

    # Don't Take
    curr = curr[:-1]
    solution(idx+1, arr, curr)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    solution(0, "abcdefghijklmnopqrstuvwxyz", "")