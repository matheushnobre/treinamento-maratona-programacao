while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    botas = []
    pares = 0
    for i in range(n):
        m, l = input().split()
        o = 'D' if l == 'E' else 'E'
        if [m, o] in botas:
            pares += 1
            botas.remove([m, o])
        else: botas.append([m, l])
    print(pares)