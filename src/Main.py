import pygame

import ImageRepixler


class main:
    def __init__(self):
        self.imagerepixler = ImageRepixler.ImageRepixler()
        self.run()

    def run(self):

        colors = ""
        image = ""

        self.imagerepixler.loadColors(colors)
        self.imagerepixler.loadImage(image)


if __name__ == "__main__":
    main()
