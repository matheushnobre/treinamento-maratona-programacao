def chamar():
	nc = 0
	while True:
		n = float(input())
		if n < 0 or n > 10:
			print('nota invalida')
		else:
			nc += 1
			if nc == 1:
				n1 = n
			else:
				print(f'media = {(n1+n)/2:.2f}')
				break

chamar()
while True:
	o = input('novo calculo (1-sim 2-nao)\n')
	if o == '1':
		chamar()
	elif o == '2':
		break