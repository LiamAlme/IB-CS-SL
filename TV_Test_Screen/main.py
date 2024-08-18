import image

img = image.EmptyImage(700,600)
win = image.ImageWin(700,600)

color = image.Pixel(255,255,255)
c = 255
d = 0

for x in range(700):
    for y in range(600):
        gradient = image.Pixel(c, c, c)
        gradient2 = image.Pixel(d, d, d)
        if x >= 0:
            color = image.Pixel(255,255,255)
            if y >= 300:
                color = image.Pixel(0,0,255)
        if x >= 100:
            color = image.Pixel(255,255,0)
            if y >= 300:
                color = image.Pixel(0,0,0)
        if x >= 200:
            color = image.Pixel(0,255,255)
            if y >= 300:
                color = image.Pixel(255,0,255)
        if x >= 300:
            color = image.Pixel(0,255,0)
            if y >= 300:
                color = image.Pixel(0,0,0)
        if x >= 400:
            color = image.Pixel(255,0,255)
            if y >= 300:
                color = image.Pixel(0,255,255)
        if x >= 500:
            color = image.Pixel(255,0,0)
            if y >= 300:
                color = image.Pixel(0,0,0)
        if x >= 600:
            color = image.Pixel(0,0,255)
            if y >= 300:
                color = image.Pixel(255,255,255)
        if y >= 400:
            color = gradient
        if y >= 500:
            color = gradient2
        img.setPixel(x,y,color)
    c -= 1
    if c == 0:
        c = 255
    if x%20 == 0:
        if d <= 2:
            d += 15
        if d == 25:
            d = 0


img.draw(win)
win.exitonclick()