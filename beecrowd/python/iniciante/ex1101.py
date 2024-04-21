while True:
    n1, n2 = map(int, input().split(' '))
    n1, n2 = min(n1, n2), max(n1, n2)
    
    if n1 <= 0:
        break
    
    resposta = ''
    soma = 0
    for i in range(n1, n2+1):
        resposta += str(i) + ' '
        soma += i
        
    resposta += "Sum=" + str(soma)
    print(resposta)