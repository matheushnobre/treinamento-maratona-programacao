from math import sqrt
n = int(input())
s = sqrt(1 + sqrt(n)**2)
s = str(round(s, 3))
print(s[:-1], end='')