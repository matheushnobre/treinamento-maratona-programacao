while True:
    e = input().split()
    if e == ['0']:
        break
    
    q, d, p = map(int, e)
    resp = int(((p*d) / (p-q)) * q)
    
    print(f'{resp} paginas') if resp != 1 else print(f'{resp} pagina')