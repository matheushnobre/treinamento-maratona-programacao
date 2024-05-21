cedulas = [100, 50, 20, 10, 5, 2, 1]
n = int(input())
print(n)
for cedula in cedulas:
    qtd = n // cedula
    n = n % cedula
    print(f"{qtd} nota(s) de R$ {cedula},00", end='\n')