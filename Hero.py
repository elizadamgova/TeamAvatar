import pygame

width, height = 55, 55

class HERO:
    def __init__(self, name, picture, screen_w, screen_h):
        self.name = name
        self.picture = picture
        self.rect = pygame.Rect(0, 0, width, height)
        self.x = 0
        self.y = 0
        self.screen_w = screen_w
        self.screen_h = screen_h

    def move(self, x, y):
        if(self.x + x > self.screen_w - width or self.x + x <0):
            return
        if(self.y + y > self.screen_h - height or self.y + y <0):
            return
        self.x += x
        self.y += y
        self.rect.move(x, y)


    def draw(self, window):
        window.blit(self.picture, (self.x, self.y))