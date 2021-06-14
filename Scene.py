from random import random

from Hero import HERO

class SCENE:
    def __init__(self,  picture, hero, NPC, collitions, enemy, quest):
        self.picture = picture
        self.hero = hero
        self.npc = NPC
        self.collitions = collitions
        self.on_npc_con = False #True
        #self.talking_to = NPCs[0] #None #NPCs[0]
        self.enemy = enemy
        self.quest = quest
        self.on_battle = False

    def draw(self, pygame, window):
        if self.on_battle:
            self.quest.battle.draw(window)
            return

        if self.on_npc_con:
           # for npc in self.NPCS:
            #if self.npc.name == self.quest.NPCname:
            self.quest.draw(window, 300, 300)
            #self.talking_to.talk_draw(window)
            return
        window.blit(self.picture, (0, 0))
        for coll in self.collitions:
            pygame.draw.rect(window, (0, 0, 0), coll)
        #for npc in self.NPCS:
        self.npc.draw(window)
        self.hero.draw(window)
        self.enemy.draw_onscene(window)

    def move(self, pygame, x, y):
        for i in self.collitions:
            if i.colliderect(pygame.Rect(self.hero.x+x, self.hero.y+y, 55, 55)):
                return
        self.hero.move(pygame, x, y)

    def talk(self, pygame):
        if self.npc.interacts(pygame, pygame.Rect(self.hero.x,self.hero.y, self.hero.screen_w, self.hero.screen_h )):
            self.on_npc_con = True
            return True
        return False

    def fight_attack(self, pygame):
         if self.enemy.interacts(pygame, pygame.Rect(self.hero.x,self.hero.y, self.hero.screen_w, self.hero.screen_h )):
            #self.on_battle = True
            return True
         return False

    def fight(self, pygame, window):
        run = True
        while run:
            self.quest.battle.draw(window)
            if self.quest.battle.fight(pygame, window):
                if self.quest.battle.win:
                    self.quest.piece_of_set(self.quest.setloot.keys()[random.randint])
                    run = False
                elif self.quest.battle.lose:
                    run = False
            if self.quest.is_finished():
                run = False
            pygame.display.update()
            if self.quest.battle.win or self.quest.battle.lose:
                run = False
        self.quest.battle.reDo()


    def moving(self, pygame, window):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        x = 0
        y = 0
        if keys[pygame.K_RIGHT] == True:
            x += 5
        if keys[pygame.K_LEFT]:
            x -= 5
        if keys[pygame.K_DOWN]:
            y += 5
        if keys[pygame.K_UP]:
            y -= 5

        self.move(pygame, x, y)
        self.actions(pygame, window)
        self.draw(pygame, window)

    def actions(self, pygame, window):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.fight_attack(pygame):
            #self.on_battle = True

            self.fight(pygame, window)

            return

        elif keys[pygame.K_t] and self.npc.interacts(pygame,pygame.Rect(self.hero.x,self.hero.y, self.hero.screen_w, self.hero.screen_h )):
            self.on_npc_con = True
            return

        elif keys[pygame.K_x]:
            self.on_npc_con = False
            self.on_battle = False
