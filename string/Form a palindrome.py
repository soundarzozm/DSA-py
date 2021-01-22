#DYNAMIC PROGRAMMING WITH MEMOIZATION

def Min(a, b): 
    return min(a, b) 
  
def findMinInsertionsDP(str1, n): 
  
    table = [[0 for i in range(n)]  
                for i in range(n)] 
    l, h, gap = 0, 0, 0
  
    for gap in range(1, n): 
        l = 0
        for h in range(gap, n): 
            if str1[l] == str1[h]: 
                table[l][h] = table[l + 1][h - 1] 
            else: 
                table[l][h] = (Min(table[l][h - 1],  
                                   table[l + 1][h]) + 1) 
            l += 1
  
    return table[0][n - 1]

for _ in range(int(input())):

    string = input()
    
    print(findMinInsertionsDP(string, len(string)))