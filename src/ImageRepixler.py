import numpy as np
from PIL import Image

class ImageRepixler:
    def __init__(self):
        self.colors = []
        self.colorsAvg = []
        self.imageArray = []
        self.imageFile = ""

    def reset(self):
        self.colors = []
        self.colorsAvg = []
        self.imageArray = []
        self.imageFile = ""

    def loadColors(self, fileName):
        self.colors = []
        with open(fileName) as colorsFile:
            line = colorsFile.readline()
            while line != "":
                line = line.replace("(", "").replace(")", "").replace("\n", "")
                temp = line.split(",")
                self.colors.append((int(temp[0]), int(temp[1]), int(temp[2])))
                line = colorsFile.readline()

        for color in self.colors:
            self.colorsAvg.append((color[0]+color[1]+color[2])/3)

    def loadImage(self, fileName):
        self.imageFile = fileName
        image = Image.open(fileName)
        self.imageArray = np.array(image)

    def saveImage(self, sameFile = False):
        image = Image.fromarray(self.imageArray)
        if sameFile:
            image.save(self.imageFile)
        else:
            image.save("Test.png")

    def repixel(self):
        x = 0
        y = 0
        while x < len(self.imageArray):
            y = 0
            while y < len(self.imageArray[x]):
                self.imageArray[x][y] = self.newColor(self.imageArray[x][y])
                y += 1
            x += 1

    def newColor(self, oldColor):
        oldColorAvg = (oldColor[0]+oldColor[1]+oldColor[2])/3

        returnColor = self.colors[0]
        currentAvg = np.abs(oldColorAvg-self.colorsAvg[0])

        count = 0
        for newAvg in self.colorsAvg:
            temp = np.abs(oldColorAvg-newAvg)
            if temp < currentAvg:
                returnColor = self.colors[count]
                currentAvg = temp
            count += 1

        return returnColor

    def rgbToLab(self, rgbColor):
        r = rgbColor[0] / 255
        g = rgbColor[1] / 255
        b = rgbColor[2] / 255

        if r <= 0.04045:
            r = r/12.92
        else:
            r = ((r + 0.055) / 1.055) ** 2.4

        if g <= 0.04045:
            g = g/12.92
        else:
            g = ((g + 0.055) / 1.055) ** 2.4

        if b <= 0.04045:
            b = b/12.92
        else:
            b = ((b + 0.055) / 1.055) ** 2.4

        x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
        y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
        z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

        x = x * 100
        y = y * 100
        z = z * 100

        xn = 95.047
        yn = 100.0
        zn = 108.883


