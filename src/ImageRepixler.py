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
                self.colors.append(line.replace("\n", ""))
                line = colorsFile.readline()


    def loadImage(self, path):
        pass

    def repixel(self):
        pass