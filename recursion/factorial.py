def parameterized(n, prod):
    # Base Case
    if n <= 1:
        print(prod)
        return None

    # Compute
    prod = prod * n

    # Recursion
    parameterized(n-1, prod)

def functional(n):
    # Base Case
    if n <= 1:
        return 1
    
    # Compute and Recursion
    return n * functional(n-1)

if __name__ == "__main__":
    n = int(input("Enter number to find factorial:\n"))
    # parameterized(n, 1)
    print(functional(n))   