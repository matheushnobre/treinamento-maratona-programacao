c1, n1, v1 = map(float, input().split())
c2, n2, v2 = map(float, input().split())

v = n1 * v1 + n2 * v2
print('VALOR A PAGAR: R$ {:.2f}'.format(round(v, 2)))