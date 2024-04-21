n = int(input())
s = input()

count = 0
for i, c in enumerate(s):
    try:
        if i != 0 and c == 'a' == s[i-1]:
            count += 1
        elif i !=c == 'a' == s[i+1]:
            count += 1
    except IndexError:
        break
print(count)