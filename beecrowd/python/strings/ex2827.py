palavras = [p.lower() for p in input().split()]
subsequencias = {}

for p in palavras:
    for i in range(len(p)-1):
        s = p[i] + p[i+1]
        if s not in subsequencias:
            subsequencias[s] = 1
        else:
            subsequencias[s] += 1

subsequencias = sorted(subsequencias.items(), key = lambda x : (-x[1], x[0]))
print(f'{subsequencias[0][0]}:{subsequencias[0][1]}')