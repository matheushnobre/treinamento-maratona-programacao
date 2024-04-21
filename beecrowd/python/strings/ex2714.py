n = int(input())
for i in range(n):
    senha = input()
    if len(senha) == 20 and senha[0] == 'R' and senha[1] == 'A':
        for index, caractere in enumerate(senha):
            if caractere.isdigit() and caractere != '0':
                print(senha[index:])
                break
    else: print('INVALID DATA')