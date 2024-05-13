n = int(input())
cart = [[int(i)] for i in input().split()]

while True:
    parar = True
    i = 0
    while i < len(cart)-1:
        if cart[i][-1] >= cart[i+1][0]:
            cart[i].extend(cart[i+1])
            del cart[i+1]
            parar = False
        i += 1
    if parar: 
        break
    
print(len(cart))