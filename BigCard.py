class Card:
	def __init__(self, buttons, picture):
		self.buttons = buttons

		self.background = picture
	def draw_the_buttons(self, window):
		for bnt in self.buttons:
			bnt