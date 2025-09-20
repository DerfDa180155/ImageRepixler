import pygame
import os

import ImageRepixler
import Button


class main:
    def __init__(self):
        pygame.init()
        pygame.display.init()

        pygame.display.gl_set_attribute(pygame.GL_ACCELERATED_VISUAL, 0)
        pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)

        self.windowWidth = 1500
        self.windowHeight = 1500

        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.RESIZABLE | pygame.GL_DOUBLEBUFFER)
        pygame.display.set_caption("Image Repixler by David Derflinger")

        self.clock = pygame.time.Clock()
        self.running = True

        self.imagerepixler = ImageRepixler.ImageRepixler()

        self.buttons = []
        self.buttons.append(Button.Button(self.screen,100,100,200,200,(255,255,255), "loadColor"))
        self.buttons.append(Button.Button(self.screen,100,400,200,200,(255,255,255), "repixel"))

        self.run()

    def run(self):
        oldMousePressed = pygame.mouse.get_pressed()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Quit the Game
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Quit the Game
                        self.running = False

            self.windowWidth = self.screen.get_width()
            self.windowHeight = self.screen.get_height()

            self.screen.fill((50, 50, 50))

            mx, my = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            mousePressedUp = []
            mousePressedDown = []
            for i in range(len(mousePressed)):
                mousePressedUp.append(not mousePressed[i] and oldMousePressed[i])
                mousePressedDown.append(mousePressed[i] and not oldMousePressed[i])

            oldMousePressed = mousePressed




            colorFileName = "colors.txt"
            imageFileName = "testImage.png"

            #self.imagerepixler.loadColors(colorFileName)
            #self.imagerepixler.loadImage(imageFileName)

            #self.imagerepixler.repixel()
            #self.imagerepixler.saveImage()

            for button in self.buttons:
                button.hover(mx, my)
                button.clicked(mx, my, mousePressedUp)
                button.draw()

                if button.isleftClicked:
                    print(button.onClick)


            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    main()
