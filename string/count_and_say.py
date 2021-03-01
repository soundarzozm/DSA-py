def countAndSay(n):

    if n==1:
        return "1"   

    if n==2:
        return "11"

    res = "11"
    
    m = 2

    while m<n:
        res = giv_res(res)
        m+=1

    return res    

def giv_res(s):
    cnt = 1
    res = ""
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            cnt+=1
        else:
            res = res + str(cnt) + s[i-1]
            cnt = 1
    return res + str(cnt) + s[i]              

if __name__ == "__main__":
    print(countAndSay(4))