def qtdCorridas(part):
    if part == 1:
        return 0
    elif part == 2 or part == 3:
        return 1
    else:
        part = part / 3
        if part % 1 != 0:
            part = int(part + 1)
        return part + qtdCorridas(part)

while True:
    n = int(input())
    if n == 0: break
    print(int(qtdCorridas(n)))