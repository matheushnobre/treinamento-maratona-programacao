n = int(input())
mails = []

for i in range(n):
    e = input()
    user = ''
    ign, cop = False, False
    
    for l in e:
        if l == '+':
            ign = True
        elif l == '@':
            ign = False
            cop = True
            
        if cop:
            user += l
        elif ign == False and l != '.':
            user += l
            
    if user not in mails:
        mails.append(user)

print(len(mails))