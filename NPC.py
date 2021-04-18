class NPC:
    def __init__(self, name, text, iconNPC, x, y):
        self.name = name
        self.text = Button_font.render(text, 1, (255, 255, 100))
        self.imageNPC = pygame.transform.scale(pygame.image.load(iconNPC), (50, 30))
        self.rect = pygame.Rect(x, y, 50, 30)

    def draw_NPC(self):
        window.blit(self.imageNPC, (self.rect.x, self.rect.y))
        window.blit(self.text, (self.rect.x, self.rect.y + 10))
