v = [float(f) for f in input().split()]
menor = min(v)

if v.count(menor) > 1:
    print('Empate')
elif menor == v[0]:
    print('Otavio')
elif menor == v[1]:
    print('Bruno')
else:
    print('Ian')