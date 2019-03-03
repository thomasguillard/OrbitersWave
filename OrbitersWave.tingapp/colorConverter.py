def HSVToRGB(h, s, v):
    h = h % 360
    c = v * s
    x = c * (1-abs((h/60)%2-1))
    m = v - c
    r = (0,0,0)
    if h < 60:
        r = (c,x,0)
    elif h < 120:
        r = (x,c,0)
    elif h < 180:
        r = (0,c,x)
    elif h < 240:
        r = (0,x,c)
    elif h < 300:
        r = (x,0,c)
    elif h <= 360:
        r = (c,0,x)
    
    return tuple(x2*255 for x2 in tuple(x1+m for x1 in r))