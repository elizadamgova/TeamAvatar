import random
class Enemy:
    def __init__(self, rect, hp, max_hp, attack, ac, picture, font):
        self.rect = rect
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.ac = ac
        self.picture = picture
        self.font = font
        self.type = "battle"


    def interacts(self, pygame, heropos):
        return pygame.Rect.colliderect(heropos, self.rect)
    def is_dead(self):
        if self.hp <= 0:
            return True
        return False

    def draw(self, window, pos, pos_hp):
        window.blit(self.picture, pos)
        window.blit(self.font.render("{} / {}".format(self.hp, self.max_hp), True, (0, 0, 0)), pos_hp)
    def get_hit(self, attack):
        if attack >= self.ac:
            return True
        return  False
    def take_dmg(self, dmg):
        self.hp -= dmg
        return self.is_dead()

    def attack(self):
        hit = random.randint(self.attack, self.attack + 10)
        return hit
    def dmg(self):
        dmg = 5 + random.randint(0, 5)
        return dmg



