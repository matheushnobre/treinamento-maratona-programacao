n = int(input())
print(n)

while len(str(n)) != 1:
    a = int(str(n)[:-1])
    b = int(str(n)[-1])
    
    n = a * 3 + b
    print(n)