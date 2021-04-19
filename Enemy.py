from random import randrange
class Enemy:
    def __init__(self, name, attacks, loot, picture, health):
        self.name = name
        self.attacks = attacks
        self.loot = loot
        self.picture = picture
        self.beaten = False
        self.health = health

    def is_beaten(self):
        return self.loot

    def atacks(self):
        return ( self.atacks + randrange(5))
    def get_hit(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.beaten = True
            return True
        else:
            return False