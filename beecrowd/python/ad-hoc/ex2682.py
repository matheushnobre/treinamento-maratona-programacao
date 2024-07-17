ant = -1
ign = False
while True:
    try:
        n = int(input())
        if n < ant and not ign:
            print(ant+1)
            ign = True
        else:
            ant=n
    except:
        if not ign:
            print(ant+1)
        break