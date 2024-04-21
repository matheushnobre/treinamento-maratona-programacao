n = int(input())

if n <= 10:
	p = 7
elif n <= 30:
	p = 7 + (n-10)
elif n <= 100:
	p = 27 + (n-30)*2
else:
	p = 167 + (n-100)*5

print(p)