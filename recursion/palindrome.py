def parameterized(s, e, string):
    # Base Case
    if s >= e:
        return True

    # # Compute and Recursion
    # return string[s] == string[e] and parameterized(s+1, e-1, string)

    # Compute
    if string[s] != string[e]:
        return False
    
    # Recursion
    return parameterized(s+1, e-1, string)

if __name__ == "__main__":
    string = input()
    print(parameterized(0, len(string)-1, string))