from itertools import permutations

s = input()
n = len(s)
letras = [0] * 26

for l in s:
    letras[ord(l)-ord('a')] += 1
    
perm = list(set(permutations(s)))
perm.sort()
print(len(perm))
for p in perm:
    print(''.join(p))