import pygame

pygame.init()
pygame.display.init()

width, height = 640, 400
window = pygame.display.set_mode((width, height))
pygame.font.init()
Button_font = pygame.font.SysFont('Times New Roman', 20)
width_button, height_button = 50, 30

clock = pygame.time.Clock() # for control over fps
clock.tick(60)

character_icon = "red.png"


class Button:
	def __init__(self, name,text, posx, posy):
		self.name = name
		self.text = text
		self.rect = pygame.Rect(posx, posy, width_button, height_button)
	def draw_button(self, color):
		pygame.draw.rect(window, (255, 0, 0), self.rect)
		
		the_text = Button_font.render(self.text, 1, color)
		window.blit(the_text, (self.rect.x, self.rect.y))
			

def game():
	run = True
	char = pygame.transform.scale( pygame.image.load(character_icon), (50, 50))
	rect_char = pygame.Rect(0, 0, 50, 50) 
	while run:
		window.fill((0, 0, 0))
		
		#mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

				break
			elif event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_ESCAPE:
				run = False
				break

				
			    elif event.key == pygame.K_RIGHT:
				rect_char.x += 8
			    elif  event.key == pygame.K_LEFT:
				rect_char.x -= 8
			    elif  event.key == pygame.K_DOWN:
				rect_char.y += 8
			    elif  event.key == pygame.K_UP:
				rect_char.y -= 8

		window.blit(char, (rect_char.x, rect_char.y))

		pygame.display.update()


	pygame.quit()


						




pygame.display.set_caption("The four elements")
iconImage = pygame.image.load("icon.png")
pygame.display.set_icon(iconImage)

background = pygame.transform.scale((pygame.image.load("menu_background3.png")), (width, height))

window.blit(background, (0,0))
pygame.display.update()
"""
button = pygame.transform.scale((pygame.image.load("StartButton.png")), (5, height))
b = pygame.Rect(50, 50, 50, 30)
window.blit(button, (b.x,b.y))
pygame.display.update()"""

b = Button("Hi!", "Click me !", 50, 50)
red = Button("Hi", "Red!", 50, 90)
blue = Button("Hi", "Blue!", 50, 140)
silver = Button("Hi", "Silver", 50, 190)
green = Button("Hi", "Green!", 50, 240)

running = True
while running:
	#mx, my = pygame.mouse.get_pos()
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mx, my = pygame.mouse.get_pos()
			if event.button == 1 and b.rect.collidepoint((mx, my)):
				game()
				running = False

				"""background = pygame.transform.scale((pygame.image.load("menu_background1.jpeg")), (width, height))

				window.blit(background, (0,0))
				pygame.display.update()"""		
			elif event.button == 1 and red.rect.collidepoint((mx, my)):
				character_icon = "red.png"
			elif event.button == 1 and blue.rect.collidepoint((mx, my)):
				character_icon = "blue.png"
			elif event.button == 1 and green.rect.collidepoint((mx, my)):
				character_icon = "green.png"
			elif event.button == 1 and silver.rect.collidepoint((mx, my)):
				character_icon = "silver.png"
	if(running == False):#else there will be segmentation fault
		break

	b.draw_button((255, 255, 255))
	red.draw_button((255, 0, 0))
	blue.draw_button((0, 0, 255))
	silver.draw_button((0, 0, 100))
	green.draw_button((0, 255, 0))
	pygame.display.update()

pygame.quit()
