from jes4py import media as m
def makeGreen(pic):
    pixels = m.getPixels(pic)
    for pixel in pixels:
        pixel.setColor(m.green)
def increseBlue(pic):
    pixels = m.getPixels(pic)
    for pixel in pixels:
        pixel.setBlue(int(pixel.getBlue()*1.6))
def darken(picture):
    #Get all the pixels in the picture
    pixels = m.getPixels(picture)
    #Loop through all the pixels
    for pixel in pixels:
        #Get the current color of the pixel
        color = m.getColor(pixel)
        #Make the color darker
        darkerColor = m.makeColor(max(color.getRed() - 30, 0,),
        max(color.getGreen() - 30, 0),
        max(color.getBlue() - 30, 0))
        #Set the pixel to the new darker color
        m.setColor(pixel, darkerColor)
def clearRed(pic):
    pixels = m.getPixels(pic)
    for pixel in pixels:
        pixel.setRed(0)
file = m.pickAFile()
pic = m.makePicture(file)
m.show(pic)
makeGreen(pic)
#increseBlue(pic)
#darken(pic)
#clearRed(pic)
m.repaint(pic)
m.explore(pic)


