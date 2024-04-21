t = 1
while True:
	n = int(input())
	if n == 0: break

	print(f'Teste {t}')
	j, z = 0, 0
	for i in range(n):
		a, b = map(int, input().split())
		j += a 
		z += b
		print(j - z)
	print('')

	t += 1