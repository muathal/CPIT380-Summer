import os
def theBoysInTheCafe(directory):
    frameloc = "..\\Frame"
    cafe12 = getMediaPath("../img/cafe12.jpg")
    cafe = getMediaPath("../img/cafe.jpg")
    back0 = makePicture(cafe12)
    back1 = makePicture(cafe)
    num = 0
    for frameFile in os.listdir(frameloc):
        num = num + 1
        printNow("Frame: " + str(num))
        if frameFile.endswith(".jpg"):

            print(frameFile)
            if ((int(frameFile[5:8]) >=106 and int(frameFile[5:8])<=149)):
                printNow("Frame: " + str(num))
                frame = makePicture(frameloc+"/"+frameFile)
                for p in getPixels(frame):
                    if distance(getColor(p), getColor(getPixel(frame,788,419))) <= 80:
                        if frame.getWidth() == 1280:
                            setColor(p, getColor(getPixel(back0, getX(p), getY(p))))
                        elif frame.getWidth() == 848:
                            setColor(p, getColor(getPixel(back1, getX(p), getY(p))))
                writePictureTo(frame, directory+frameFile)
def addText(directory):
    frameloc = "..\\Frames"
    num = 0
    xn = 396
    yn = 580
    xm = 362
    ym = 505
    xmh = 448
    ymh = 292
    for frameFile in os.listdir(frameloc):
        num = num + 1
        if frameFile.endswith(".jpg"):
            if int(frameFile[5:8]) >=37 and int(frameFile[5:8])<=49:
                printNow("Frame: " + str(num))
                frame = makePicture(frameloc+"/"+frameFile)
                frame.addRectFilled(white,xn,yn,100,50)
                frame.addText(black,xn,yn,"Nawaf AlGhamdi")
                xn = xn+20
                yn = yn-20
                writePictureTo(frame, directory + frameFile)
            elif int(frameFile[5:8]) >=106 and int(frameFile[5:8])<=149:
                printNow("Frame: " + str(num))
                frame = makePicture(frameloc+"/"+frameFile)
                frame.addRectFilled(white,xm,ym,100,50)
                frame.addText(black,xm,ym,"Muath Alhurtumi")
                xm = xm+10
                ym = ym-10
                writePictureTo(frame, directory + frameFile)
            elif int(frameFile[5:8]) >=181 and int(frameFile[5:8])<=205:
                printNow("Frame: " + str(num))
                frame = makePicture(frameloc+"/"+frameFile)
                frame.addRectFilled(white,xmh,ymh,100,50)
                frame.addText(black,xmh,ymh,"Mohammad AlKhayat")
                xmh = xmh+20
                ymh = ymh-20
                writePictureTo(frame, directory + frameFile)
def makeVid():
    vid = makeMovieFromInitialFile(pickAFile())
    newVid = writeQuicktime(vid,"C:\\Users\\Wmksa\\Desktop\\CPIT380\\boys at cafe.mov",10)
    
    
