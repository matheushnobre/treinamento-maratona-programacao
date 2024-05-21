def regraDeTres(a, b, c):
    return (c * b) / a

graf, din, geo = map(int, input().split())
maximizar = input()

if maximizar == 'A':
    graf += regraDeTres(2, 3, din)
    graf += regraDeTres(2, 5, geo)
    print(int(graf))
elif maximizar == 'B':
    graf += regraDeTres(2, 5, geo)
    din += regraDeTres(3, 2, graf)
    print(int(din))
elif maximizar == 'C':
    graf += regraDeTres(2, 3, din)
    geo += regraDeTres(5, 2, graf)
    print(int(geo))