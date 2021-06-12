from Hero import HERO

class SCENE:
    def __init__(self,  picture, hero, NPCs, collitions):
        self.picture = picture
        self.hero = hero
        self.NPCS = NPCs
        self.collitions = collitions
        self.on_npc_con = False #True
        self.talking_to = NPCs[0] #None #NPCs[0]

    def draw(self, pygame, window):
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
                #print("Hiii")
                return
        #pygame.Rect.move(self.hero.rect, self.hero.x+x, self.hero.y+y)
        self.hero.move(pygame, x, y)
    #def action(self, command):
    def talk(self, pygame, window):
        for n in self.NPCS:
            #print(n.interacts(pygame, pygame.Rect(self.hero.x,self.hero.y, self.hero.screen_w, self.hero.screen_h )))
            if n.interacts(pygame, pygame.Rect(self.hero.x,self.hero.y, self.hero.screen_w, self.hero.screen_h )):
                #print("Hi")
                #n.talk(window,self.hero.rect)
                self.on_npc_con = True
                self.talking_to = n
                return True
        return False
