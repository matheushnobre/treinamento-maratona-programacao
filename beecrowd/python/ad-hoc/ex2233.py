r = int(input(), 16)
g = int(input(), 16)
b = int(input(), 16)

verm = 1
verd = (r // g)
if 2*r > g:
    verd2 = ((r - g) // g) + 1
    verd = verd * verd2
azul = (g // b)
if 2*g > b:
    azul2 = ((g - b) // b) + 1
    azul = azul * azul2
azul = azul * verd
    
print(hex(verm+verd+azul)[2:])