def qtdDivisores(n):
    div = 2 # O 1 e o próprio número
    for i in range(2, n//2+1):
        if n % i == 0:
            div += 1
    return div

c = int(input())
for i in range(c):
    n = int(input())
    bd = 1 # Já considerando a bola 1
    for j in range(2, n):
        if qtdDivisores(j) % 2 == 1:
            bd += 1
    print(n - bd)