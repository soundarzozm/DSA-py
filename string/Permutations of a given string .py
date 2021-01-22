for _ in range(int(input())):
    
    string = input()
    n = len(string)
    arr = list(string)
    result_arr = []
    
    def toString(List):
        return ''.join(List) 

    def permute(a, l, r):

        if l==r:
            result_arr.append(toString(a))

        else:

            for i in range(l, r+1):
                a[l], a[i] = a[i], a[l]
                permute(a, l+1, r)
                a[l], a[i] = a[i], a[l]

    permute(arr, 0, n-1)

    result_arr.sort()

    for i in result_arr:
        print(i, end=" ")

    print("", end="\n")  