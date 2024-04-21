while True:
    try:
        num1, num2 = map(int, input().split(' '))
        print(num1 ^ num2) # ^ realiza operações a nível de bit
        
    except EOFError:
        break