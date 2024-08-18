import image
img = image.Image("luther.jpg")

width = img.getWidth()
height = img.getHeight()
newimg = image.EmptyImage(width*2, height*2)
win = image.ImageWin(width*2, height*2)

for x in range (img.getWidth()):
    for y in range(img.getHeight()):
        p = img.getPixel(x, y)
        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        newpixel = image.Pixel(red, green, blue)
        newimg.setPixel(2*x, 2*y, newpixel)
        newimg.setPixel(2*x + 1, 2*y, newpixel)
        newimg.setPixel(2*x, 2*y + 1, newpixel)
        newimg.setPixel(2*x + 1, 2*y + 1, newpixel)

newimg.draw(win)
win.exitonclick()