class map_class:
    def __init__(self, background, buttons):
        self.background = background
        self.buttons = buttons

    def draw_map(self, window):
        window.blit(self.background, (0, 0))
        for button in self.buttons:
            button.draw_button(window)

    def hit_button(self, mouse):
        for button in self.buttons:
            if button.collides(mouse):
                return button.result()

        return False
