n = float(input())
s = n/1.60934
i = ''

cont=-10000
for c in str(s):
    i += c
    cont+=1
    if c == '.':
        cont=0
    if cont==2: break
    
print(i, end='')