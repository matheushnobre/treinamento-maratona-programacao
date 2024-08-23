lista = [0, 0, 0, 0, 0]
while True:
    try:
        i=0
        for item in input().split():
            lista[i]+=int(item)
            i+=1
        
    except EOFError: 
        m = max(lista)
        if m == lista[0]:
            print('NINHO')
        elif m == lista[1]:
            print('CONDENSADO')
        elif m == lista[2]:
            print('TAPIOCA')
        elif m == lista[3]:
            print('MORANGO')
        else:
            print('CHOCOLATE')
        break