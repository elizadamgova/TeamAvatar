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
        self.hero.move(x, y)
    #def action(self, command):
    def talk(self,window,  mouse):
        for n in self.NPCS:
            if n.interacts(mouse):
                n.talk(window, mouse)
                self.on_npc_con = True
                print("Hi")
                self.talking_to = n
