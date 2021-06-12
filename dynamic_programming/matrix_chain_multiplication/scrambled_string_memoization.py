def scrambledString(a, b):
    
    #Initialization
    key = a + "_" + b
    if key in t.keys():
        return t[key]

    n = len(a)
    flag = False
    flag1 = False
    flag2 = False
    
    #Base condition
    if a==b:
        return True
    if len(a)<=1 or len(b)<=1:
        return False

    #Loop
    for i in range(1, n):
        if (scrambledString(a[:i], b[n-i:]) & scrambledString(a[i:], b[:n-i])):
            flag1 = True
        if (scrambledString(a[:i], b[:i]) & scrambledString(a[i:], b[i:])):
            flag2 = True
        if flag1 or flag2:
            flag = True
            break

    t[key] = flag
    return t[key]

if __name__=="__main__":

    a = "great"
    b = "rgeat"

    if len(a)!=len(b):
        print(False)
        exit()

    if a=="" and b=="":
        print(True)
        exit()

    t = {}

    print(scrambledString(a, b))