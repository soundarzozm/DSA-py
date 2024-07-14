def maxProfit(arr):
    buyPrice = arr[0]
    days = len(arr)

    maxDifference = 0

    for i in range(1, days):
        if (arr[i] - buyPrice) > 0:
            maxDifference = max(maxDifference, arr[i] - buyPrice)
        else:
            buyPrice = arr[i]

    return maxDifference


if __name__ == "__main__":
    arr = list(map(int, input().split(",")))
    print(maxProfit(arr))
