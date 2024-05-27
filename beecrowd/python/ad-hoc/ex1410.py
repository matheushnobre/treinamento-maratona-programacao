while True:
    a, d = map(int, input().split())
    if a == d == 0: break
    
    atacantes = sorted([int(i) for i in input().split()])
    defensores =  sorted([int(i) for i in input().split()])
    
    impedido = False
    for at in atacantes:
        if at < defensores[1]:
            impedido = True
            break
    
    print('Y') if impedido else print('N')