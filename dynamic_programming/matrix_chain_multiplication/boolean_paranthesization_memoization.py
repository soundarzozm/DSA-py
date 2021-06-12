def booleanParanthesization(string, i, j, isTrue):

    #Initialization
    key = str(i) + "_" + str(j) + "_" + str(isTrue)
    if key in t.keys():
        return t[key]
    ans = 0

    #Base Case
    if i>j:
        return 0
    if i==j:
        if isTrue==1:
            if string[i]=="T":
                t[key] = 1
            else:
                t[key] = 0
        else:
            if string[i]=="F":
                t[key] = 1
            else:
                t[key] = 0
        return t[key]

    #Loop
    for k in range(i+1, j, 2):

        leftTrue = booleanParanthesization(string, i, k-1, 1)
        leftFalse = booleanParanthesization(string, i, k-1, 0)
        rightTrue = booleanParanthesization(string, k+1, j, 1)
        rightFalse = booleanParanthesization(string, k+1, j, 0)

        if string[k]=="^":
            if isTrue:
                ans += (leftTrue * rightFalse) + (leftFalse * rightTrue)
            else:
                ans += (leftTrue * rightTrue) + (leftFalse * rightFalse)

        elif string[k]=="&":
            if isTrue:
                ans += (leftTrue * rightTrue)
            else:
                ans += (leftFalse * rightTrue) + (leftTrue * rightFalse) + (leftFalse * rightFalse)

        elif string[k]=="|":
            if isTrue:
                ans += (leftTrue * rightTrue) + (leftFalse * rightTrue) + (leftTrue * rightFalse)
            else:
                ans += (leftFalse * rightFalse)

    t[key] = ans
    return t[key]

if __name__=="__main__":

    string = "T|T&F^T"
    n = len(string)

    t = {}

    print(booleanParanthesization(string, 0 , n-1, 1))