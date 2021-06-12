import random
class Battle:
    def __init__(self, enemy, hero, background, attacks):
        self.enemy = enemy
        self.hero = hero
        self.background = background
        self.attacks = attacks
        self.text = ''
        self.win = False
        self.lose = False

    def draw(self, window):
        window.blit(self.background, (0, 0))
        self.hero.draw_in_battle(window, (400, 400), (400, 350))
        if self.win:
            window.blit(self.enemy.font.render("WIN", True, (0, 0, 0)), (600, 200))
            return
        if self.lose:
            window.blit(self.enemy.font.render("LOSE", True, (0, 0, 0)), (600, 200))
            return

        self.enemy.draw(window, (400, 100), (400, 50))
        self.hero.draw_in_battle(window, (400, 400), (400, 350))
        window.blit(self.enemy.font.render(self.text, True, (0, 0, 0)), (600, 200))
        for att in self.attacks:
            att.draw_button(window)

    """
    def fight(self, mouse):

        if self.win or self.lose:

            return
        #bonus_ac = 0
        #attacked = False
        for att in self.attacks:

            if att.collides(mouse):
                print("HI")
                #attacked = True
                #if att.type == "block":
                  #  bonus_ac = 10
                #else:
                    #hit = random.randint(self.hero.attack, self.hero.attack + 10)
                    #if self.enemy.get_hit(hit):
                if self.enemy.take_dmg(10 + random.randint(0, 5)):
                    self.win = True
                    return
                if self.hero.take_dmg(self.enemy.dmg()):
                    self.lose = True
                    return
                break
        if attacked:
            #if self.hero.get_hit(self.enemy.attack() - bonus_ac):
           if self.hero.take_dmg(self.enemy.dmg()):
                self.lose = True
"""

    def fight(self,  pygame):
            if self.win or self.lose:

                return
            #bonus_ac = 0
            #attacked = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_a:
                        print("HI")
                        #attacked = True
                        #if att.type == "block":
                          #  bonus_ac = 10
                        #else:
                            #hit = random.randint(self.hero.attack, self.hero.attack + 10)
                            #if self.enemy.get_hit(hit):
                        if self.enemy.take_dmg(5 + random.randint(0, 5)):#10 + random.randint(0, 5)):
                            self.win = True
                            return
                        if self.hero.take_dmg(self.enemy.dmg()):
                            self.lose = True
                            return
                        break

            """if attacked:
                #if self.hero.get_hit(self.enemy.attack() - bonus_ac):
               if self.hero.take_dmg(self.enemy.dmg()):
                    self.lose = True"""

