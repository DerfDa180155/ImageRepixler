import pygame
import os

import ImageRepixler


class main:
    def __init__(self):
        self.imagerepixler = ImageRepixler.ImageRepixler()
        self.run()

    def run(self):
        colorFileName = "colors.txt"
        imageFileName = "testImage.png"


        self.imagerepixler.loadColors(colorFileName)
        self.imagerepixler.loadImage(imageFileName)

        self.imagerepixler.repixel()
        self.imagerepixler.saveImage()

        print(self.imagerepixler.colors)
        print(self.imagerepixler.imageArray)


if __name__ == "__main__":
    main()
