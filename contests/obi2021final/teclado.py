teclado = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

num = input()
n = int(input())
s = 0
for i in range(n):
    string = input()
    if len(string) != len(num):
        continue
    ehPossivel = True
    for c in range(len(string)):
        if string[c] not in teclado[int(num[c])]:
            ehPossivel = False
            break
    if ehPossivel:
        s += 1
print(s)