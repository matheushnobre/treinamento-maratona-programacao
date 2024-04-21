n = int(input())
criancas = []
b, m = 0, 0
for i in range(n):
    c = input()
    if c[0] == '+': b+=1
    else: m+=1
    criancas.append(c[2:])
criancas.sort()
for crianca in criancas: print(crianca)
print(f'Se comportaram: {b} | Nao se comportaram: {m}')