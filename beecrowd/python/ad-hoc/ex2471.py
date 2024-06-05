def verificaLinha(n, q):
    soma = sum(q[0])
    for i in range(1, n):
        s = sum(q[i])
        if s != soma: 
            if i == 1: 
                if sum(q[2]) == s:
                    return 0
                else:
                    return 1
            else:
                return i
            
def verificaColuna(n, q):
    soma = sum([q[i][0] for i in range(n)])
    for j in range(1, n):
        s = sum([q[i][j] for i in range(n)])
        if s != soma: 
            if j == 1: 
                if sum([q[i][2] for i in range(n)]) == s:
                    return 0
                else:
                    return 1
            else:
                return j
    
n = int(input())
q = []

for i in range(n):
    q.append([int(i) for i in input().split()])
    
linha = verificaLinha(n, q)
coluna = verificaColuna(n, q)

valorIncorreto = q[linha][coluna]
soma = sum(q[0]) if linha != 0 else sum(q[1])
somaIncorreta = sum(q[linha])

valorCorreto = soma - (somaIncorreta - valorIncorreto)

print(valorCorreto, valorIncorreto)