from random import randrange

class Battle:
    def __init__(self, background, enemy, our_actions, dmg, health):
        self.background = background
        self.enemy  = enemy
        self.our_actions = our_actions
        self.dmg = dmg
        self.health = health

    def drawing(self, window):
        window.blit(self.background, (0, 0))
        for b in self.our_actions:
            b.draw_button(window)
    def is_beaten(self):
        return self.beaten

    def action(self, mouse):
        for at in self.our_actions:
            if(at.collides(mouse)):
                enemy.get_hit( dmg(at.result) + randrnge(10))
                break


