from jes4py import media as m;
def luminance (pixel):
    r = m.getRed(pixel)
    g = m.getGreen(pixel)
    b = m.getBlue(pixel)
    return (r+g+b)/3
def edgeDetect(img):
    for px in m.getPixels(img):
        x = m.getX(px)
        y = m.getY(px)
        if y < m.getHeight(img) - 1 and x < m.getWidth(img) - 1:
            botrt = m.getPixel(img,x+1,y+1)
            thislum = luminance(px)
            brlum = luminance(botrt)
            if abs(brlum -thislum) > 10:
                m.setColor(px,m.black)
            if abs(brlum - thislum) <= 10:
                m.setColor(px, m.white)
    return img
def swapback(img,back,newback):
    for px in m.getPixels(img):
        x = m.getX(px)
        y = m.getY(px)
        bgPx = m.getPixel(back,x,y)
        pxcol = m.getColor(px)
        bgcol = m.getColor(bgPx)
        if (m.distance(pxcol,bgcol)<15.0):
            newcol = m.getColor(m.getPixel(newback,x,y))
            m.setColor(px,newcol)
    return img
def edgeDetection(amount):
    # Create the picture
    sourceFile = m.pickAFile()
    sourcePicture = m.makePicture(sourceFile)
    endY = m.getHeight(sourcePicture) - 1
    for y in range(endY):
        for x in range(m.getWidth(sourcePicture)):
            # Get the top and bottom pixels
            topPixel = m.getPixel(sourcePicture, x, y)
            bottomPixel = m.getPixel(sourcePicture, x, y + 1)
            # Calculate the average color values
            topAverage = (m.getRed(topPixel) + m.getGreen(topPixel) + m.getBlue(topPixel)) / 3.0
            bottomAverage = (m.getRed(bottomPixel) + m.getGreen(bottomPixel) + m.getBlue(bottomPixel)) / 3.0
            # Compare the averages and set the color based on the threshold
            if abs(topAverage - bottomAverage) < amount:
                m.setColor(topPixel, m.white)
            else:
                m.setColor(topPixel, m.black)
def medianFilter():
    # Create the picture
    sourceFile = m.pickAFile()
    sourcePicture = m.makePicture(sourceFile)
    # Define an array of size 9 since the filter size is 3x3
    pixel = [0] * 9

    # Loop through all the pixels starting from (1,1) to (picture's width -1,picture's height -1)
    for i in range(1, m.getWidth(sourcePicture) - 1):
        for j in range(1, m.getHeight(sourcePicture) - 1):
            # Get the average of the 9 pixels and store them in the array
            pixel[0] = (m.getPixel(sourcePicture, i - 1, j - 1).getRed() +
                        m.getPixel(sourcePicture, i - 1, j - 1).getGreen() + m.getPixel(sourcePicture, i - 1,
                                                                                        j - 1).getBlue()) / 3
            pixel[1] = (m.getPixel(sourcePicture, i - 1, j).getRed() +
                        m.getPixel(sourcePicture, i - 1, j).getGreen() + m.getPixel(sourcePicture, i - 1,
                                                                                    j).getBlue()) / 3
            pixel[2] = (m.getPixel(sourcePicture, i - 1, j + 1).getRed() +
                        m.getPixel(sourcePicture, i - 1, j + 1).getGreen() + m.getPixel(sourcePicture, i - 1,
                                                                                        j + 1).getBlue()) / 3
            pixel[3] = (m.getPixel(sourcePicture, i, j + 1).getRed() +
                        m.getPixel(sourcePicture, i, j + 1).getGreen() + m.getPixel(sourcePicture, i,
                                                                                    j + 1).getBlue()) / 3
            pixel[4] = (m.getPixel(sourcePicture, i + 1, j + 1).getRed() +
                        m.getPixel(sourcePicture, i + 1, j + 1).getGreen() + m.getPixel(sourcePicture, i + 1,
                                                                                        j + 1).getBlue()) / 3
            pixel[5] = (m.getPixel(sourcePicture, i + 1, j).getRed() +
                        m.getPixel(sourcePicture, i + 1, j).getGreen() + m.getPixel(sourcePicture, i + 1,
                                                                                    j).getBlue()) / 3
            pixel[6] = (m.getPixel(sourcePicture, i + 1, j - 1).getRed() +
                        m.getPixel(sourcePicture, i + 1, j - 1).getGreen() + m.getPixel(sourcePicture, i + 1,
                                                                                        j - 1).getBlue()) / 3
            pixel[7] = (m.getPixel(sourcePicture, i, j - 1).getRed() +
                        m.getPixel(sourcePicture, i, j - 1).getGreen() + m.getPixel(sourcePicture, i,
                                                                                    j - 1).getBlue()) / 3
            pixel[8] = (m.getPixel(sourcePicture, i, j).getRed() +
                        m.getPixel(sourcePicture, i, j).getGreen() + m.getPixel(sourcePicture, i, j).getBlue()) / 3
        # Sort the array to get the median value
        pixel.sort()
        # Set the median value (pixel[4]) in the pixel (i, j)
        newColor = m.makeColor(pixel[4], pixel[4], pixel[4])
        m.setColor(m.getPixel(sourcePicture, i, j), newColor)

img = m.makePicture("../img/muath1.jpg")
back = m.makePicture("../img/back.jpg")
newback = m.makePicture("../img/jungel.jpg")
img2 = swapback(img,back,newback)
m.writePictureTo(img2,"../img/muath4.jpg")