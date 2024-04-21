d = list()
while True:
	try:
		n = input()
	except EOFError:
		break
	d.append(int(input()))
m = round(sum(d)/len(d), 1)
print(m)