x, y, z = map(int, input().split())

if x**2 != y**2 + z**2:
    print('Nao eh retangulo!')
else:
    a1 = (y*z)/2
    a2 = (3*((z/2)**2))/2
    a = a1+a2
    print(f'AREA = {a:.0f}')