def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(n-1, 1, -1):
            if n % i == 0:
                return False
    return True

while True:
    try:
        m = int(input())
        moedas = []
        for i in range(m):
            moedas.append(int(input()))
        n = int(input())
    
        soma = 0
        for i in range(len(moedas)-1, -1, -n):
            soma += moedas[i]
            
        if is_prime(soma):
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
        
    except EOFError: break