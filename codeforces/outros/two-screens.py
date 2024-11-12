t = int(input())
for _ in range(t):
    a = input()
    b = input()
    
    equals = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]: equals += 1
        else: break
    
    saida = len(a) + len(b) - 2*equals
    if equals != 0: saida += equals + 1
    print(saida)