#import pygame

width_button, height_button = 50, 30


class Button:
    def __init__(self, x, y, picture, pygame, hit_result):
        self.picture = picture
        self.pygame = pygame
        self.hit_result = hit_result
        self.rect = self.pygame.Rect(x, y, width_button, height_button)

    def draw_button(self, window):
        #self.pygame.draw.rect(window, (0, 0, 0), self.rect)
        window.blit(self.picture, (self.rect.x, self.rect.y))
    def collides(self, mouse):
        return self.rect.collidepoint(mouse)
    def result(self):
        return self.hit_result

    """def draw_button_image(self): #name = image
        #pygame.draw.rect(window, (255, 0, 0), self.rect)

        the_image = pygame.transform.scale(  pygame.image.load(self.name), (50, 30))


"""
