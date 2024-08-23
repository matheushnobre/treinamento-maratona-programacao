t = int(input())

for _ in range(t):
    n = int(input())
    numbers = [int(i) for i in input().split()]
    somaTotal = sum(numbers)
    values = list(input())
    
    pont = 0
    i = 0
    j = n-1
    while i < j:
        if values[i] != 'L' and i < j:
            somaTotal -= numbers[i]
            i += 1
        if values[j] != 'R' and j > i:
            somaTotal -= numbers[j]
            j -= 1
        if values[i] == 'L' and values[j] == 'R' and i< j: 
            pont += somaTotal
            somaTotal -= numbers[i]
            somaTotal -= numbers[j]
            i += 1
            j -= 1
    print(pont)