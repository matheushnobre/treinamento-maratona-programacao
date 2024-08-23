t = int(input())
for i in range(t):
    n = int(input())
    array = [int(i) for i in input().split()]
    m = int(input())
    for j in range(m):
        string = input()
        dicLetras = {}
        dicNumbers = {}
        saida = True
        if len(string) == n:
            for c in range(len(string)):
                if string[c] in dicLetras:
                    if dicLetras[string[c]] != array[c]:
                        saida = False
                        break
                else:
                    dicLetras[string[c]] = array[c]
                    
                if array[c] in dicNumbers:
                    if dicNumbers[array[c]] != string[c]:
                        saida = False
                        break
                else:
                    dicNumbers[array[c]] = string[c]
        else: saida = False
        if saida: print('YES')
        else: print('NO')
            