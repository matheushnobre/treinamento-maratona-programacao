n = int(input())
c = int(input())

saida = True
for i in range(n-1):
    b = int(input())
    if b > c:
        saida = False

if saida:
    print('S')
else:
    print('N')