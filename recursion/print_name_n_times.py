def printName(current, n):
    
    # BASE CASE
    if current == n:
        return

    # COMPUTE FRONT
    print(current)
    
    # RECURSION
    printName(current+1, n)
    
    # COMPUTE BACK
    print(current)

if __name__ == "__main__":
    n = int(input())
    printName(0, n)
