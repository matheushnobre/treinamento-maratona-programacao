import re
while True:
    try:
        entrada = input()
    except EOFError:
        break
    
    a, b, c = re.split('[+=]', entrada)
    if a == 'R': print(int(c)-int(b))
    elif b == 'L': print(int(c)-int(a))
    else: print(int(a)+int(b))