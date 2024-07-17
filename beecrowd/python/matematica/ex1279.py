first=True
while True:
    isBissexto = False
    isOrdinary = True
    try:
        n = int(input())
        if not first: 
            print()
        first=False
        if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
            print('This is leap year.')
            isBissexto = True
            isOrdinary = False
        if n % 15 == 0:
            print('This is huluculu festival year.')
            isOrdinary = False
        if isBissexto and n % 55 == 0:
            isOrdinary = False
            print('This is bulukulu festival year.')
        if isOrdinary:
            print('This is an ordinary year.')
    except EOFError:
        break
    
    