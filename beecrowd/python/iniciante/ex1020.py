n = int(input())
anos = n // 365
meses = n % 365 // 30
dias = n - (meses*30 + anos*365)

print(anos, 'ano(s)')
print(meses, 'mes(es)')
print(dias, 'dia(s)')