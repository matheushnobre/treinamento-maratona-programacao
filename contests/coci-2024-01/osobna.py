l1 = input()
l2 = input()
l3 = input()

dig = ''
for v in l1:
    if v in '0123456789':
        dig+=v
pin = dig[10:]

dig = ''
for v in l2:
    if v in '0123456789':
        dig+=v
year = dig[:2]
if int(year) <= 24: year = '20'+year
else: year='19'+year
month = dig[2:4]
day = dig[4:6]

names = l3.split('<')
first = names[0]
last = names[2]

print(f'Ime: {first.capitalize()}')
print(f'Prezime: {last.capitalize()}')
print(f'Datum rodjenja: {day}-{month}-{year}')
print(f'OIB: {pin}')