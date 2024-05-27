while True:
    try:
        carnes, dias = [], []
        n = int(input())
        for i in range(n):
            c, d = input().split()
            carnes.append(c)
            dias.append(int(d))
        
        for i in range(n-1, 0, -1):
            for j in range(i):
                if dias[j] > dias[j+1]:
                    carnes[j], carnes[j+1] = carnes[j+1], carnes[j]
                    dias[j], dias[j+1] = dias[j+1], dias[j]
                    
        print(*carnes)
                    
    except EOFError:
        break