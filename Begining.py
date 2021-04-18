class Begin:
    def __init__(self, background, buttons):
        self.background = background
        self.buttons = buttons
    def drawing(self, window):
        window.blit(self.background, (0, 0))
        for b in self.buttons:
            b.draw_button(window)

    def hit_button(self, mouse):
        for b in self.buttons:
            if(b.collides(mouse)):
                return b.result()


        return False