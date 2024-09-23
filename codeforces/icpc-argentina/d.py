lista = list(map(int, input().split()))
lista.sort()

if lista[2] >= lista[0] + lista[1]:
    print('S')
else:
    print('N')