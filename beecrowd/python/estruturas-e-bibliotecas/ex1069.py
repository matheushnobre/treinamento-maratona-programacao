def extrair_diamantes(mina):
    total_diamantes = 0
    pilha = []
    for item in mina:
        if item == '<':
            pilha.append('<')
        elif item == '>':
            if len(pilha) > 0:
                pilha.pop()
                total_diamantes += 1
            else:
                continue
    return total_diamantes


num_entradas = int(input())
entradas = []

for i in range(num_entradas):
    entradas.append(input())
    
for entrada in entradas:
    print(extrair_diamantes(entrada))