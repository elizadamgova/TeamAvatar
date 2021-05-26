width, height = 200, 100

class button:
    def __init__(self, pygame, picture, x, y, result, sizew = 200, sizeh = 100):
        self.picture = picture
        self.resultt = result
        self.rect = pygame.Rect(x, y, sizew, sizeh)
        self.position = (x, y)
        self.type = None

    def draw_button(self, window):
        window.blit(self.picture, self.position)

    def collides(self, mouse):
        return self.rect.collidepoint(mouse)

    def result(self):
        return self.resultt
    def set_type(self, type):
        self.type = type
