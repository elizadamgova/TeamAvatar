width, height = 200, 100

class button:
    def __init__(self, pygame, picture, x, y, result):
        self.picture = picture
        self.resultt = result
        self.rect = pygame.Rect(x, y, width, height)
        self.position = (x, y)

    def draw_button(self, window):
        window.blit(self.picture, self.position)

    def collides(self, mouse):
        return self.rect.collidepoint(mouse)

    def result(self):
        return self.resultt