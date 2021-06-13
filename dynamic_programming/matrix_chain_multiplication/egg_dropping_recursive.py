import sys

def eggDropping(e, f):

    #Base case
    if e==1:
        return f
    if f==0 or f==1:
        return f

    mn = INT_MAX

    for k in range(1, f+1):
        temp = 1 + max(eggDropping(e-1, k-1), eggDropping(e, f-k))
        mn = min(mn, temp)

    return mn

if __name__=="__main__":
    f = 5
    e = 3

    INT_MAX = sys.maxsize

    print(eggDropping(e, f))
