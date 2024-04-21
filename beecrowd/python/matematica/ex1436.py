ct = 1
t = int(input())

while ct <= t:
    n = input().split()
    idades = []
    for i in range(1, len(n)):
        idades.append(int(n[i]))
    mediana = idades[len(idades) // 2]
    print(f'Case {ct}: {mediana}')
    ct += 1