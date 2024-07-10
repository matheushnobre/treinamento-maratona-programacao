n = int(input())
for i in range(n):
    p = input()
    if len(p) == 3:
        if p[0] == 'o' and p[1] == 'n': print(1)
        elif p[0] == 'o' and p[2] == 'e': print(1)
        elif p[1] == 'n' and p[2] == 'e': print(1)
        else: print(2)
    else: print(3)