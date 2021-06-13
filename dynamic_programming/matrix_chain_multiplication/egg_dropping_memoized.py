import sys

def eggDropping(e, f):

    #Initialization
    if t[e][f]!=-1:
        return t[e][f]
    mn = INT_MAX

    #Base case
    if e==1:
        return f
    if f==0 or f==1:
        return f

    #Loop
    for k in range(1, f+1):

        if t[e-1][k-1]!=-1:
            egg_break = t[e-1][k-1]
        else:
            egg_break = eggDropping(e-1, k-1)

        if t[e][f-k]!=-1:
            egg_not_break = t[e][f-k]
        else:
            egg_not_break = eggDropping(e, f-k)

        temp = 1 + max(egg_break, egg_not_break)
        mn = min(mn, temp)
    t[e][f] = mn
    return t[e][f]

if __name__=="__main__":
    f = 4
    e = 2

    INT_MAX = sys.maxsize
    t = [[-1 for i in range(f+1)] for j in range(e+1)]

    print(eggDropping(e, f))
