n = int(input())

for i in range(n):
    entrada = input()
    
    first, second = entrada.split(' ')
    tamanho_maior_palavra = len(second) if(len(second)) > len(first) else len(first)
    
    nova_palavra = ''
    for i in range(tamanho_maior_palavra):
        try:
            nova_palavra += first[i]
        except IndexError:
            ...
        
        try:
            nova_palavra += second[i]
        except IndexError:
            ...
    
    print(nova_palavra)
    
