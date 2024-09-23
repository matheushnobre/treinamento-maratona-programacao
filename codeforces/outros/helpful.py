s = input()
numbers = []
for v in s:
    if v != '+':
        numbers.append(v)
numbers.sort()
print(*numbers, sep='+', end='')