def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def mmc(a, b):
    return a * (b / mdc(a, b))

r = float(input())
r = r * 100
r = round(r, 0)
m = mmc(36000, r)
resultado = int(m // r)

print(resultado)