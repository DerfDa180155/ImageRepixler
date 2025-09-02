import numpy as np
from PIL import Image

class ImageRepixler:
    def __init__(self):
        self.colors = []
        self.imageArray = []

    def reset(self):
        self.colors = []
        self.imageArray = []

    def loadColors(self, fileName):
        self.colors = []
        with open(fileName) as colorsFile:
            line = colorsFile.readline()
            while line != "":
                line = line.replace("(", "").replace(")", "").replace("\n", "")
                temp = line.split(",")
                self.colors.append((int(temp[0]), int(temp[1]), int(temp[2])))
                line = colorsFile.readline()

    def loadImage(self, fileName):
        image = Image.open(fileName)
        self.imageArray = np.array(image)

    def saveImage(self):
        image = Image.fromarray(self.imageArray)
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
        return self.colors[0]

