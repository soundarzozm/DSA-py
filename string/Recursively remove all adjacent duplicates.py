def rm_dup(string):

    i = 1
    out_str = ""
    
    if len(string)<2:
        return string
    else:    
        while(i < (len(string)-1)):
            if string[i] == string[i+1] or string[i]==string[i-1]:
                i+=1
            else:
                out_str+=string[i]
                i+=1
            
        if string[-1] != string[-2]:
            out_str+=string[-1]
            
        if string[0] != string[1]:
            out_str = string[0] + out_str
    
    return(out_str) 

for _ in range(int(input())):
    
    string = input()
    
    x = rm_dup(string)
    while(x != rm_dup(x)):
        x = rm_dup(x)
        
    print(x) 