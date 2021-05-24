import pygame
from Map import map_class
from Button import button
from Hero import HERO
from NPC import npc
from Scene import SCENE

pygame.init()
pygame.display.init()

width, height = 1550, 990 #1000, 700 ##
wh = (width, height)
window = pygame.display.set_mode(wh)
clock = pygame.time.Clock()
clock.tick(30)
text_font = pygame.font.Font('freesansbold.ttf', 20)
hello = text_font.render('Hello, world!', True, (0, 0, 0))



pygame.display.set_caption("the four elements")
iconImage =pygame.image.load("IconImage.jpg")
pygame.display.set_icon(iconImage)
menu = pygame.transform.scale(pygame.image.load("old_book_v2.jpg"), wh)



on_map = False
map = {}
notReady = map_class( pygame.transform.scale(pygame.image.load("NotReady.png"), wh), [])
map["notready"] = notReady

fire_kingdom = button(pygame, pygame.image.load("fire.png"), 250, 100, "notready")#"fire_kingdom")
earth_kingdom = button(pygame, pygame.image.load("earth.png"), 250, 750, "notready")#"earth_kingdom")
water_kingdom = button(pygame, pygame.image.load("water.png"), 750, 100, "notready")#"water_kingdom")
air_kingdom = button(pygame, pygame.image.load("air.png"), 750, 750, "notready")#"air_kingdom")
bigmap = map_class( pygame.transform.scale(pygame.image.load("Vankila.jpg"), wh), [fire_kingdom, earth_kingdom, water_kingdom, air_kingdom])

map["fire_kingdom"] = fire_kingdom
map["earth_kingdom"] = earth_kingdom
map["water_kingdom"] = water_kingdom
map["air_kingdom"] = air_kingdom

open_map = bigmap


hero = HERO('Mark', pygame.transform.scale(pygame.image.load("red.png"), (55, 55)), width, height)
npc1 = npc(text_font, pygame, 'Mimi',  pygame.transform.scale(pygame.image.load("blue.png"), (55, 55)), 55, 10, pygame.transform.scale(pygame.image.load("old_book.png"), wh), "talk", ["Hi"])

scene = SCENE(pygame.transform.scale(pygame.image.load("the_well.png"), wh), hero, [npc1], [pygame.Rect(600, 280, 200, 200)])# pygame.Rect(200, 100, 100, 100)
on_scene = True


running = True
while running:
    if(on_map):
        open_map.draw_map(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if(open_map.hit_button((mx, my))):
                    open_map = map[open_map.hit_button((mx, my))]
    elif(on_scene):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    x, y = 0, 0
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                    elif event.key == pygame.K_RIGHT:
                        x+=10
                        #scene.move(10, 0)
                    elif event.key == pygame.K_LEFT:
                        x-=10
                        #scene.move(-10, 0)
                    elif event.key == pygame.K_DOWN:
                        y+=10
                        #scene.move(0, 10)
                    elif event.key == pygame.K_UP:
                        y-=10
                        #scene.move(0, -10)
                    elif event.key == pygame.K_t:
                        scene.talk(window, (x, y))
                        #scene.on_npc_con = True
                    scene.move(pygame, x, y)
        scene.draw(pygame, window)


    else:
        window.blit(menu, (0, 0))
        window.blit(hello, (250, 250))
        """       keys = pygame.key.get_pressed()
        if keys[pygame.QUIT]:
            running = False
            break
        elif keys[pygame.K_ESCAPE]:
            running = False
            break
        elif keys[pygame.K_RIGHT]:
            hero.move(10, 0)
        elif keys[pygame.K_LEFT]:
            hero.move(-10, 0)
        elif keys[pygame.K_DOWN]:
            hero.move(0, 10)
        elif keys[pygame.K_UP]:
            hero.move(0, -10)"""

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                    elif event.key == pygame.K_RIGHT:
                        hero.move(10, 0)
                    elif event.key == pygame.K_LEFT:
                        hero.move(-10, 0)
                    elif event.key == pygame.K_DOWN:
                        hero.move(0, 10)
                    elif event.key == pygame.K_UP:
                        hero.move(0, -10)

        hero.draw(window)
    pygame.display.update()

pygame.quit()

