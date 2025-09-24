import pygame

class Button:
    def __init__(self, screen, x, y, width, height, color, displayText, displayTextColor, displayTextSize, onClick):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.displayText = displayText
        self.displayTextColor = displayTextColor
        self.displayTextSize = displayTextSize
        self.onClick = onClick

        self.isHovered = False
        self.isleftClicked = False
        self.isrightClicked = False


    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

        font = pygame.font.Font(pygame.font.get_default_font(), self.displayTextSize)


        text = font.render(self.displayText, True, self.displayTextColor)
        newRect = text.get_rect()
        newRect.center = (self.x+(self.width/2),self.y+(self.height/2),)
        self.screen.blit(text, newRect)

    def clicked(self, mx, my, mouseClick):
        if self.hover(mx, my) and mouseClick[0]:
            self.isleftClicked = True
        elif self.hover(mx, my) and mouseClick[2]:
            self.isrightClicked = True
        else:
            self.isleftClicked = False
            self.isrightClicked = False
        return self.isleftClicked

    def hover(self, mx, my):
        temp = pygame.Rect(self.x, self.y, self.width, self.height)
        self.isHovered = temp.collidepoint((mx, my))
        return self.isHovered

