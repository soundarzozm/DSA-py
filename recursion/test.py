def recursiveFunction(a, n):
    # print("BRUH")
    if a == n+1:
        return
    # print(a)
    recursiveFunction(a+1 ,n)
    print(a)
if __name__ == "__main__":
    n = int(input())
    recursiveFunction(1, n)


