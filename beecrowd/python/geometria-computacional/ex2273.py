from math import sqrt

def distancia(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2) 

while True:
    try:
        xi, yi, xf, yf, v = map(int, input().split())
        xl, yl, xr, yr = map(int, input().split())
        
        d1 = distancia(xi, yi, xl, yr) + xr - xl + distancia(xr, yr, xf, yf)
        d2 = distancia(xi, yi, xl, yl) + xr - xl + distancia(xr, yl, xf, yf)
        d = min(d1, d2)
        
        print(round(d/v, 1)) 
    except EOFError:
        break   