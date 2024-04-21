t = 1
while True:
	r, n = map(int, input().split())
	if r == n == 0: break

	l = (r-n)/n 
	if l % 1 == 0:
		l = int(l)
	else:
		l = int(l+1)

	if l > 26: l = 'impossible'
	print(f'Case {t}: {l}') 
	t+=1