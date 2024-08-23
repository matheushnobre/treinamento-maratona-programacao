e = int(input())
text = str(e)
soma = sum([int(a) for a in text])

if e < 550:
    print('VOU TENTAR PROXIMO ANO', end='')
elif soma % 11 == 0:
    if e >= 700:
        print('COMPUTACAO', end='')
    else:
        print('VOU TENTAR PROXIMO ANO', end='')
elif len(set(text)) == 1:
    if e >= 600:
        print('MATEMATICA', end='')
    else:
        print('VOU TENTAR PROXIMO ANO', end='')
else:
    if e > 780:
        print('MEDICINA')
    if e >= 700:
        print('COMPUTACAO')
    if e >= 650:
        print('DIREITO')
    if e >= 600:
        print('MATEMATICA')
    if e >= 550:
        print('FILOSOFIA', end='')