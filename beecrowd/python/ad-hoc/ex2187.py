t = 1
while True:
	n = int(input())
	if n == 0: break

	i, n = n//50, n%50
	j, n = n//10, n%10
	k, n = n//5, n%5
	l = n//1

	print(f'Teste {t}')
	print(i, j, k, l, sep=' ')
	print('')
	t += 1
