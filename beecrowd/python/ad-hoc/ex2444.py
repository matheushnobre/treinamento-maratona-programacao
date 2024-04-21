v, t = map(int, input().split())
a = [int(i) for i in input().split()]

for al in a:
	v += al
	if v < 0: v = 0
	elif v > 100: v = 100

print(v)