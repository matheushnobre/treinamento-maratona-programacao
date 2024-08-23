def ehPalindromo(string):
    i=0
    j=len(string)-1
    while i<j:
        if string[i] != string[j]:
            return False
        i+=1
        j-=1
    return True
        
r = input()
v = 'aeiou'

rsc = ''
for c in r:
    if c in v:
        rsc += c
        
if ehPalindromo(rsc):
    print('S')
else:
    print('N')
