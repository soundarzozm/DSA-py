def solve(root, result):

    #Base cases
    if root == None:
        return 0

    #Hypothesis
    left = solve(root.left, result)
    right = solve(root.right, result)

    #Induction
    temp_pass = 1 + max(left, right)
    temp_through = 1 + left + right
    ans = max(temp_pass, temp_through)
    result = max(ans, result)

    return temp_pass

if __name__ == "__main__":

    result = 0

    solve(root, result)
    return result
