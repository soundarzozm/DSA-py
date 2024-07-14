import time


def fibonacciWithDP(n, dp):
    if n <= 1:
        return dp[n]

    if dp[n-1] == -1:
        dp[n-1] = fibonacciWithDP(n-1, dp)
    if dp[n-2] == -1:
        dp[n-2] = fibonacciWithDP(n-2, dp)

    dp[n] = dp[n-1] + dp[n-2]
    return dp[n]


def fibonacci(n):
    if n < 0:
        return 0

    if n == 0 or n == 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...]

    n = int(input("Enter the iteration of fibonacci required\n"))
    # if (n < 0):
    #     print("Invalid input")
    #     exit()

    # dp = [0, 1] + [-1]*(max(n-1, 0))
    # dp[0] = 0
    # dp[1] = 1
    # start_time = time.process_time()
    # print("With DP:", fibonacciWithDP(n, dp))
    # print((time.process_time() - start_time)*1000, "ms", "\n")

    # start_time = time.process_time()
    # print("With plain recursion:", fibonacci(n))
    # print((time.process_time() - start_time)*1000, "ms", "\n")
    # print("DP Array:", dp)

    print(fibonacci(n))
