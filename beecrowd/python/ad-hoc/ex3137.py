p = int(input())
if p <= 9:
    s = p
elif p <= 99:
    s = (p-9)*2 + 9
elif p <= 999:
    s = (p-99)*3 + 189
elif p <= 9999:
    s = (p-999)*4 + 2889
elif p <= 99999:
    s = (p-9999)*5 + 38889
else:
    s = (p-99999)*6 + 488889

print(s)