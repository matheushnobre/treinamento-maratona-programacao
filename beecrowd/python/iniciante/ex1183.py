operacao = input()
soma = 0
for i in range(12):
    linha = list()
    for j in range(12):
        elemento = float(input())
        if i < j: soma += elemento

if operacao == 'S': print(round(soma, 1))
else: print(round(soma/66, 1))