s = float(input())

if s <= 400:
	r = 15
elif s <= 800:
	r = 12
elif s <= 1200:
	r = 10
elif s <= 2000:
	 r = 7
else:
	r = 4

novo = s + s*(r/100)
print('Novo salario: {:.2f}'.format(novo))
print('Reajuste ganho: {:.2f}'.format(novo - s))
print('Em percentual: {} %'.format(r))