while True:
    n = input()
    
    if n[:2] == '0x':
        print(int(n, 16))
    elif int(n) < 0: 
        break
    else:
        n = int(n)
        print(hex(n).upper().replace('X', 'x'))