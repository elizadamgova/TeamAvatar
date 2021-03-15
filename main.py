import pygame


#class Button












width, height = 640, 400
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("The four elements")
iconImage = pygame.image.load("icon.png")
pygame.display.set_icon(iconImage)

background = pygame.transform.scale((pygame.image.load("menu_background3.png")), (width, height))

window.blit(background, (0,0))
pygame.display.update()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()
