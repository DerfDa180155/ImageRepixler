import numpy

class ImageRepixler:
    def __init__(self):
        self.colors = []

    def reset(self):
        self.colors = []

    def loadColors(self, fileName):
        self.colors = []
        with open(fileName) as colorsFile:
            line = colorsFile.readline()
            while line != "":
                line = line.replace("(", "").replace(")", "").replace("\n", "")
                temp = line.split(",")
                self.colors.append((int(temp[0]), int(temp[1]), int(temp[2])))
                line = colorsFile.readline()

    def loadImage(self, path):
        pass

    def repixel(self):
        pass