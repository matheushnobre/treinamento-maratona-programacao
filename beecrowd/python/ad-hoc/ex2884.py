n, m = map(int, input().split())
l, *x = map(int, input().split())

acesos = {}
for i in range(m):
    if i+1 in x:
        acesos[i+1] = True
    else:
        acesos[i+1] = False

interruptores = {}
for i in range(n):
    k, *y = map(int, input().split())
    interruptores[i+1] = y
    
a = 0
i = 1
t = 0
while True:
    par = True
    for valor in acesos.values():
        if valor == True:
            par = False
    if par: break
    
    a += 1
    for lamp in interruptores[i]:
        acesos[lamp] = False if acesos[lamp] == True else True
    
    i += 1
    if i > n: 
        i = 1
        t += 1
        if t == 2:
            a = -1
            break
    
print(a)