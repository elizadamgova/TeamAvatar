width, height = 200, 100


class npc:
    def __init__(self, font, pygame, name, picture, x, y, background, type, conversation):
        self.name = font.render(name, True, (0, 0, 0))
        self.picture = picture
        self.position = (x, y)
        self.rect = pygame.Rect(x, y, width+20, height+20)
        self.background = background
        self.type = type
        self.conversation = []
        for con in conversation:
            self.conversation.append(font.render(con, True, (0, 0, 0)))


    def interacts(self, mouse):
        return self.rect.collidepoint(mouse)

    def draw(self, window):
        window.blit(self.picture, self.position)
        window.blit(self.name, self.position)
        window.blit(self.name, self.position)

    def talk_draw(self, window):
        window.blit(self.background, (0, 0))
        window.blit(self.picture, (250, 250))
        window.blit(self.conversation[0], self.position)
    def talk(self, window, mouse):
        if self.type == "talk":
            window.blit(self.background, (0, 0))
            window.blit(self.picture, (250, 250))
            window.blit(self.conversation[0], self.position)