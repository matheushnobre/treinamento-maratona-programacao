def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def mmc(a, b):
    return a * (b / mdc(a, b))

r = float(input())
r = r * 100
if r % 1 != 0:
    if r - int(r) < 0.5:
        r = int(r)
    else:
        r = int(r) + 1
r = int(r)
m = mmc(36000, r)
resultado = int(m // r)

print(resultado)