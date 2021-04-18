import pygame
from Button import Button
from Begining import Begin

pygame.init()
pygame.display.init()

width, height = 1550, 990
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()  # for control over fps
clock.tick(60)
pygame.display.set_caption("The four elements")
iconImage = pygame.image.load("icon.png")
pygame.display.set_icon(iconImage)

character_icon = "red.png"
buttons = Button(50, 50, pygame.transform.scale(pygame.image.load("StartButton.png"), (50, 50)), pygame, "red" )
background = pygame.transform.scale((pygame.image.load("menu_background3.png")), (width, height))
first_scene = Begin(background, [buttons])
background1 = pygame.transform.scale((pygame.image.load("icon.png")), (width, height))
second_scene = Begin(background1, [])
scenes = {"red":second_scene}
scene = first_scene

running = True
while running:
    scene.drawing(window)
    pygame.display.update()
    # mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if(scene.hit_button((mx, my))):
                scene = scenes[scene.hit_button((mx, my))]
            #if(b.collides((mx, my))):
             #   window.fill((255, 255, 0))

    if (running == False):  # else there will be segmentation fault
        break

    #b.draw_button(window)#(255, 255, 255)
    """red.draw_button(window)
    blue.draw_button(window)
    silver.draw_button(window)
    green.draw_button(window)
    """
    #pygame.display.update()

pygame.quit()