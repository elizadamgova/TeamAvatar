import pygame

width, height = 55, 55

class HERO:
    def __init__(self, name, picture, screen_w, screen_h, font):
        self.name = name
        self.picture = picture
        self.rect = pygame.Rect(0, 0, width, height)
        self.x = 0
        self.y = 0
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.hp = 50
        self.max_hp = 100
        self.AC = 10
        self.attack = 10
        self.font = font
        self.titles = []

    def move(self,pygame, x, y):
        if(self.x + x > self.screen_w - width or self.x + x <0):
            return
        if(self.y + y > self.screen_h - height or self.y + y <0):
            return
        self.x += x
        self.y += y
        pygame.Rect.move(self.rect, (self.x + x, self.y + y))
        #self.rect.move(x, y)


    def draw(self, window):
        window.blit(self.picture, (self.x, self.y))
    def draw_in_battle(self, window, pos, pos_hp):
        window.blit(self.picture, pos)
        window.blit(self.font.render("{} / {}".format(self.hp, self.max_hp), True, (0, 0, 0)), pos_hp)

    def is_dead(self):
        if self.hp <= 0:
            self.hp = 0
            return True
        return False

    def get_hit(self, attack):
        if attack >= self.ac:
            return True
        return False

    def take_dmg(self, dmg):
        self.hp -= dmg
        return self.is_dead()