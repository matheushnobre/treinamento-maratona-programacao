n = int(input())

if n == 0:
    print('*\n*')
elif n <= 5:
    print("I"*n)
    print('*')
else:
    print('I'*5)
    print('I'*(n-5))