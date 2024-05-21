linha = input()

if linha.count('O') in [2, 3] or linha.count('X') == 3:
    print('?')
elif linha[0] == linha[1] or linha[1] == linha[2]:
    print('Alice')
else:
    print('*')