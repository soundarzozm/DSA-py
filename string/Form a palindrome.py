#DYNAMIC PROGRAMMING WITH MEMOIZATION

def Min(a, b): 
    return min(a, b) 
  
def findMinInsertionsDP(str1, m): 
  
    table = [[0 for i in range(m)]  
                for i in range(m)] 
    l, h, gap = 0, 0, 0
  
    for gap in range(1, m): 
        l = 0
        for h in range(gap, m): 
            if str1[l] == str1[h]: 
                table[l][h] = table[l + 1][h - 1] 
            else: 
                table[l][h] = (Min(table[l][h - 1],  
                                   table[l + 1][h]) + 1) 
            l += 1
  
    return table[0][m - 1]

for _ in range(int(input())):

    string = input()
    
    print(findMinInsertionsDP(string, len(string)))
