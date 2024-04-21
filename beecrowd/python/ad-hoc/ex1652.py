consoantes = 'bcdfghjklmnopqrstvwxyz'

l, n = map(int, input().split())

irregulares = dict()
for i in range(l):
    e = input().split()
    irregulares[e[0]] = e[1]

for i in range(n):
    p = input()
    if p in irregulares.keys():
        print(irregulares[p])
    elif p[-2] in consoantes and p[-1] == 'y':
        print(p[:-1] + 'ies')
    elif p[-1] == 'o' or p[-1] == 's' or p[-1] == 'x':
        print(p + 'es')
    elif (p[-1] == 'h') and (p[-2] == 's' or p[-2] == 'c'):
        print(p + 'es')
    else:
        print(p + 's')