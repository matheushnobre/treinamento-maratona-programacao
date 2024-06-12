while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    esp = n//2
    for i in range(1, n+1, 2):
        print(esp*' '+i*'*')
        esp -= 1
    
    esp = n//2
    print(esp*' '+'*')
    esp -= 1
    print(esp*' '+'***')
    print()