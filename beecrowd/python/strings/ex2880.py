c = input()
p = input()

s = 0
pas = 0

for i in range(len(c) - len(p) + 1):
    j = 0
    k = pas
    pos = True
    
    while j < len(p):
        if c[k] == p[j]: 
            pos = False
            break
        j += 1
        k += 1
        
    if pos:
        s += 1
    pas += 1
    
print(s)