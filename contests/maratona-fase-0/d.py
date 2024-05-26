velocidade, extensao = map(int, input().split())

horas = (velocidade // extensao + 19) % 24
min = int((velocidade / extensao * 60) % 60)

if horas < 10:
    horas = '0'+str(horas)

if min < 10:
    min = '0'+str(min)
    
print(f'{horas}:{min}')