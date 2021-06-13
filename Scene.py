from random import random

from Hero import HERO

class SCENE:
    def __init__(self,  picture, hero, NPCs, collitions, enemy, quest):
        self.picture = picture
        self.hero = hero
        self.NPCS = NPCs
        self.collitions = collitions
        self.on_npc_con = False #True
        self.talking_to = NPCs[0] #None #NPCs[0]
        self.enemy = enemy
        self.quest = quest
        self.on_battle = False

    def draw(self, pygame, window):
        if self.on_battle:
            self.quest.draw(window)
            return

        if self.on_npc_con:
            self.talking_to.talk_draw(window)
            return
        window.blit(self.picture, (0, 0))
        for coll in self.collitions:
            pygame.draw.rect(window, (0, 0, 0), coll)
        for npc in self.NPCS:
            npc.draw(window)
        self.hero.draw(window)

    def move(self, pygame, x, y):
        for i in self.collitions:
            if i.colliderect(pygame.Rect(self.hero.x+x, self.hero.y+y, 55, 55)):
                return
        self.hero.move(pygame, x, y)
    def talk(self, pygame):
        for n in self.NPCS:
            if n.interacts(pygame, pygame.Rect(self.hero.x,self.hero.y, self.hero.screen_w, self.hero.screen_h )):
                self.on_npc_con = True
                self.talking_to = n
                return True
        return False

    def fight_attack(self, pygame):
         if self.enemy.interacts(pygame, pygame.Rect(self.hero.x,self.hero.y, self.hero.screen_w, self.hero.screen_h )):
            self.on_battle = True
    def fight(self, pygame):
        while True:
            if self.quest.battle.fight(pygame):
                if self.quest.battle.win:
                    self.quest.piece_of_set(self.quest.setloot.keys()[random.randint])
                    self.quest.battle.reRo()
                    break
                elif self.quest.battle.lose:
                    self.quest.battle.reRo()
                    break
