while True:
	try:
		n = int(input())
		epr = 0
		ehd = 0
		for i in range(n):
			m, s = input().split()
			if s == 'EPR':
				epr += 1
			elif s == 'EHD':
				ehd += 1
		print(f'EPR: {epr}')
		print(f'EHD: {ehd}')
		print(f'INTRUSOS: {n-epr-ehd}')
	except EOFError:
		break