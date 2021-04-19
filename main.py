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

#start_cart = Button(50, 50, pygame.transform.scale(pygame.image.load("StartButton.png"), (50, 50)), pygame, "earth" )
start = Button(50, 50, pygame.transform.scale(pygame.image.load("StartButton.png"), (50, 50)), pygame, "earth" )
n_ready = pygame.image.load("NotReady.png")
not_ready= Begin(n_ready, [start])



earth_kingdom = pygame.transform.scale(pygame.image.load("Earth_kingdom.jpg"), (width, height) )
city_earth_kingdom = pygame.transform.scale(pygame.image.load("The_well.png"), (width, height) )

tavern = Button(50, 750, pygame.transform.scale(pygame.image.load("Tavern.png"), (50, 50)), pygame, "city")
market = Button(750, 750, pygame.transform.scale(pygame.image.load("Market.png"), (50, 50)), pygame, "city")
start_cart = Button(50, 50, pygame.transform.scale(pygame.image.load("StartButton.png"), (50, 50)), pygame, "first" )

earth_scene= Begin(earth_kingdom, [start_cart, tavern, market])
city_earth_scene= Begin(city_earth_kingdom, [start_cart])


start_cart = Button(50, 50, pygame.transform.scale(pygame.image.load("StartButton.png"), (50, 50)), pygame, "red" )
background = pygame.transform.scale((pygame.image.load("menu_background3.png")), (width, height))
first_scene = Begin(background, [start_cart])


#fire = Button(50, 50, pygame.transform.scale(pygame.image.load("StartButton.png"), (50, 50)), pygame, "NotReady")
BigMap = pygame.transform.scale((pygame.image.load("BigMap.png")), (width, height))


fire = Button(50, 50, pygame.transform.scale(pygame.image.load("Fire.png"), (50, 50)), pygame, "NotReady")
water = Button(750, 50, pygame.transform.scale(pygame.image.load("Water.png"), (50, 50)), pygame, "NotReady")
darkness = Button(50, 750, pygame.transform.scale(pygame.image.load("Darkness.png"), (50, 50)), pygame, "NotReady")
earth = Button(750, 750, pygame.transform.scale(pygame.image.load("Earth.png"), (50, 50)), pygame, "earth")
#fire = Button(50, 50, pygame.transform.scale(pygame.image.load("StartButton.png"), (50, 50)), pygame, "NotReady")
BigMap = pygame.transform.scale((pygame.image.load("BigMap.png")), (width, height))
second_scene = Begin(BigMap, [fire, water, darkness, earth])


scenes = {"red": second_scene,
          "NotReady": not_ready,
          "earth":earth_scene,
          "first":first_scene,
          "city": city_earth_scene}
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