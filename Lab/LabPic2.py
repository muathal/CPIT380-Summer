from jes4py import media as m
def sas (photo):
    for pixel in m.getPixels(photo):
        r = m.getRed(pixel)
        g = m.getGreen(pixel)
        b = m.getBlue(pixel)
        grm = (r+g+b)/3
        gr = m.makeColor(grm,grm,grm)
        m.setColor(pixel,gr)
    return photo
def applyThresholding():
    sourceFile = m.pickAFile()
    sourcePicture = m.makePicture(sourceFile)
    threshold = int(eval(input(("Enter the threshold value:"))))
    for i in range(m.getWidth(sourcePicture)):
        for j in range(m.getHeight(sourcePicture)):
            red = m.getRed(m.getPixel(sourcePicture, i, j))
            green = m.getGreen(m.getPixel(sourcePicture, i, j))
            blue = m.getBlue(m.getPixel(sourcePicture, i, j))
            average = (red + green + blue) / 3
            if average >= threshold:
                m.setColor(m.getPixel(sourcePicture, i, j), m.white)
            else:
                m.setColor(m.getPixel(sourcePicture, i, j), m.black)
    m.writePictureTo(sourcePicture,"../img/catThe.jpeg")
def Laplacian():
    # Create the picture
    sourceFile = m.pickAFile()
    pic = m.makePicture(sourceFile)
    # Convert the picture to grayscale
    sas(pic)
    # Create a new picture with the same width and height as the original picture
    newPicture = m.makeEmptyPicture(m.getWidth(pic), m.getHeight(pic))
    # Loop through all the pixels
    for x in range(1, m.getWidth(pic) - 1):
        for y in range(1, m.getHeight(pic) - 1):
            pixel1 = m.getPixel(pic, x - 1, y - 1)
            pixel2 = m.getPixel(pic, x - 1, y)
            pixel3 = m.getPixel(pic, x - 1, y + 1)
            pixel4 = m.getPixel(pic, x, y - 1)
            pixel5 = m.getPixel(pic, x, y)
            pixel6 = m.getPixel(pic, x, y + 1)
            pixel7 = m.getPixel(pic, x + 1, y - 1)
            pixel8 = m.getPixel(pic, x + 1, y)
            pixel9 = m.getPixel(pic, x + 1, y + 1)
            # Multiply the operator values by the pixels
            value = (1 * m.getRed(pixel1)) + (-2 * m.getRed(pixel2)) + (1 * m.getRed(pixel3))
            (+ (-2 * m.getRed(pixel4)) + (4 * m.getRed(pixel5)) + (-2 * m.getRed(pixel6)) +
             (1 * m.getRed(pixel7)) + (-2 * m.getRed(pixel8)) + (1 * m.getRed(pixel9)))
            # Check the value and set it in the range (0-255) if it is not
            if value > 255:
                value = 255
            elif value < 0:
                value = 0
            # Set the value in the new picture
            m.setColor(m.getPixel(newPicture, x, y), m.makeColor(value, value, value))
    m.writePictureTo(newPicture,"../img/catLap.jpeg")

applyThresholding()
#file = m.pickAFile()
#pic = m.makePicture(file)
#m.repaint(pic)
#m.explore(pic)
