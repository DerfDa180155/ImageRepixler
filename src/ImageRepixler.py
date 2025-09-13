import numpy as np
from PIL import Image

class ImageRepixler:
    def __init__(self):
        self.colors = []
        self.colorsLab = []
        self.imageArray = []
        self.imageFile = ""

    def reset(self):
        self.colors = []
        self.colorsLab = []
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
            self.colorsLab.append(self.rgbToLab(color))

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
        currentAvg = np.abs(oldColorAvg-self.colorsLab[0])

        count = 0
        for newAvg in self.colorsLab:
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

        temp = x / xn
        if temp > 0.008856:
            fx = temp ** (1 / 3)
        else:
            fx = 7.787 * temp + 16 / 116

        temp = y / yn
        if temp > 0.008856:
            fy = temp ** (1 / 3)
        else:
            fy = 7.787 * temp + 16 / 116

        temp = z / zn
        if temp > 0.008856:
            fz = temp ** (1 / 3)
        else:
            fz = 7.787 * temp + 16 / 116

        L = (116 * fy) - 16
        a = 500 * (fx - fy)
        b = 200 * (fy - fz)

        return (L, a, b)

    def calcDif(self, color1, color2):
        return np.sqrt(np.power(color1[0]-color2[0], 2) + np.power(color1[1]-color2[1], 2) + np.power(color1[2]-color2[2], 2))

