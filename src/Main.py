import pygame
import os

import ImageRepixler


class main:
    def __init__(self):
        self.imagerepixler = ImageRepixler.ImageRepixler()
        self.run()

    def run(self):
        colorFileName = "colors.txt"

        for subdir, dirs, files in os.walk('./'):
            for file in files:
                print(file)

        colors = ""
        image = ""

        self.imagerepixler.loadColors(colors)
        self.imagerepixler.loadImage(image)


if __name__ == "__main__":
    main()
