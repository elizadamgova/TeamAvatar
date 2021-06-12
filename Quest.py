x, y = 200, 200

class Quest:
    def __init__(self,name,  pygame, font, NPCname, battle, text, background, setloot):
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

    def draw(self, window):
        window.blit(self.background, (x, y))
        window.blit(self.font.render(self.text, True, (0, 0, 0)), 250, 250)
        window.blit(self.font.render("Progress: {}/{}".format(self.progress, len(self.setloot)), True, (0, 0, 0)), 350, 350)

    def is_finished(self):
        if(self.progress == len(self.setloot)):
            self.completed = True
            return True
        return False

    def piece_of_set(self, item):
        if(self.name != item.setOfQuest):
            return "Wrong set"
        self.setloot[item.name] +=1
        return self.is_finished()