t = int(input())
for e in range(t):
    n = int(input())
    pascal = []
    for i in range(n):
        tam = i+1
        linha = [1] * tam
        for j in range(1, tam-1):
            linha[j] = pascal[-1][j] + pascal[-1][j-1]
        pascal.append(linha)

    soma = 0
    for linha in pascal:
        for elemento in linha:
            soma += elemento
    print(soma)