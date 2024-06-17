while True:
    try:
        pal = input()
    except EOFError:
        break
    
    pal = list(pal)
    el = 0
    while len(pal) > 0:
        print(el*' ', end='')
        print(*pal, sep=' ')
        pal = pal[:-1]
        el += 1
        
    print()