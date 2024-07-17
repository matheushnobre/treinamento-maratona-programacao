renas = {
    0: 'Rudolph',
    8: 'Blitzen',
    7: 'Donner',
    6: 'Cupid',
    5: 'Comet',
    4: 'Vixen',
    3: 'Prancer',
    2: 'Dancer',
    1: 'Dasher'
}

r = [int(i) for i in input().split()]
s = sum(r) % 9
print(renas[s])