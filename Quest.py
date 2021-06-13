x, y = 200, 200

class Quest:
    def __init__(self,name,  pygame, font, NPCname, battle, text, background, setloot, title):
        self.taken = False
        self.name = name
        self.rect = pygame.Rect(x, y, 200, 200)
        self.font = font
        self.NPCname = NPCname
        self.battle = battle
        self.text = text
        self.background = background
        self.setloot = setloot
        self.completed = False
        self.progress = 0
        self.title = title

    def draw(self, window, x, y):
        window.blit(self.background, x, y)
        window.blit(self.font.render(self.text, True, (0, 0, 0)), x + 50, y)
        window.blit(self.font.render("Progress: {}/{}".format(self.progress, len(self.setloot)), True, (0, 0, 0)), x+100 , y)

    def is_finished(self):
        if(self.progress == len(self.setloot)):
            #self.completed = True
            return True
        return False

    def piece_of_set(self, item):
        if(self.name != item.setOfQuest):
            return "Wrong set"
        self.setloot[item.name] +=1
        prog = 0
        for s in  self.setloot.keys():
            if self.setloot[s] > 0:
                prog += 1
        self.progress = prog
        return self.is_finished()

    def completed(self, NPC):
        if self.is_finished() and NPC.name == self.NPCname:
            self.completed = True

