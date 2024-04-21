e = input().split()

q = 0
for i in range(1, 8):
    if e[i] == '1':
        q += 1
        
if e[0] == '1' and q % 2 == 0:
    print('S')
elif e[0] == '1' and q % 2 == 1:
    print('N?') 
elif e[0] == '0' and q % 2 == 1:
    print('S')
else:
    print('N?')