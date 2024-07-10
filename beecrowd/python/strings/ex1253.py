# A=65, Z=90
n = int(input())
for _ in range(n):
    pal = list(input())
    d = int(input())
    for i, c in enumerate(pal):
        asc = ord(c) - d
        if asc >= 65: pal[i] = chr(asc)
        else: pal[i] = chr(asc + 26)
    print(*pal, sep='')