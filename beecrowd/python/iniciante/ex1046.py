a, b = map(int, input().split())

if b > a:
	d = b-a
elif b < a:
	d = 24-a + b
else:
	d = 24
print(f'O JOGO DUROU {d} HORA(S)')