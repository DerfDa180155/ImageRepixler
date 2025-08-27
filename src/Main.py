import pygame
import os

import ImageRepixler


class main:
    def __init__(self):
        self.imagerepixler = ImageRepixler.ImageRepixler()
        self.run()

    def run(self):
        colorFileName = "colors.txt"
        colors = []
        image = ""

        with open(colorFileName) as colorsFile:
            line = colorsFile.readline()
            while line != "":
                colors.append(line.replace("\n", ""))
                line = colorsFile.readline()

        print(colors)


        self.imagerepixler.loadColors(colors)
        self.imagerepixler.loadImage(image)


if __name__ == "__main__":
    main()
