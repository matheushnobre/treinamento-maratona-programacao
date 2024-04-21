n, l, d = map(int, input().split())
ln = (d*n)/1000
qtd = ln/l

if qtd % 1 == 0:
	qtd = int(qtd)
else:
	qtd = int(qtd) + 1

print(qtd*l)