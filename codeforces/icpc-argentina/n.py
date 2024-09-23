n = map(int, input().split())
lista = list(map(int, input().split()))
lista.sort()
a = lista[-1]
b = lista[0]
c = lista[0]

ganho = a**2 + b**2 + c**2
gasto = a*b + b*c + c*a
lucro = ganho - gasto
print(lucro)