from itertools import groupby

def ordenar(lista):
    impares = [i for i in lista if i % 2 == 1]
    impares.sort(reverse=True)
    pares = [i for i in lista if i % 2 == 0]
    pares.sort()
    lista[:] = impares + pares

while True:
    n, m = map(int, input().split())
    print(n, m)
    if n == m == 0: break
    
    nums = []
    for i in range(n):
        num = int(input())
        if num < 0:
            mod = num % -m
        else:
            mod = num % m
        nums.append({'n': num, 'mod': mod})

    nums.sort(key = lambda x : x['mod'])
    nums = groupby(nums, key = lambda x : x['mod'])
    
    for chave, grupo in nums:
        lista = []
        for num in list(grupo):
            lista.append(num['n'])
        ordenar(lista)
        print(*lista, sep='\n')