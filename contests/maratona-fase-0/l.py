n = int(input())
quartos = input().split()
dormindo = {c:0 for c in input().split()}

incomodando = []

for i in range(n):
    for chave, valor in dormindo.items():
        if valor == 0:
            maisNova = chave
            break
        
    incomodando.append(maisNova)
    del dormindo[quartos[i]]
    
print(*incomodando)