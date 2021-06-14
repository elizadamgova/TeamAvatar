import pygame, time
from Map import map_class
from Button import button
from Hero import HERO
from NPC import npc
from Scene import SCENE
from Enemy import Enemy
from Battle import Battle
from Quest import Quest
from Item import Item

pygame.init()
pygame.display.init()

width, height = 1000, 700 ##1550, 990 #
wh = (width, height)
window = pygame.display.set_mode(wh)
clock = pygame.time.Clock()
clock.tick(30)
text_font = pygame.font.Font('freesansbold.ttf', 20)
hello = text_font.render('Hello, world!', True, (0, 0, 0))

the_well = pygame.transform.scale(pygame.image.load("the_well.png"), wh)
hero_pic = pygame.transform.scale(pygame.image.load("red.png"), (55, 55))
npc_pic = pygame.transform.scale(pygame.image.load("blue.png"), (55, 55))
old_book = pygame.transform.scale(pygame.image.load("old_book.png"), wh)
enemy_pic = pygame.transform.scale(pygame.image.load("blue.png"), (55, 55))
battle_pic = pygame.transform.scale(pygame.image.load("Battle.jpg"), wh)
black_canvas = pygame.transform.scale(pygame.image.load("black_canvas.jpg"), (600, 600))

pygame.display.set_caption("the four elements")
iconImage =pygame.image.load("IconImage.jpg")
pygame.display.set_icon(iconImage)

hero = HERO('Mark', hero_pic, width, height, text_font) #ok
npc1 = npc(text_font, pygame, 'Mimi', npc_pic , 55, 10, old_book, ["Hi"])

enemy = Enemy(pygame.Rect(600, 600, 55, 55), 50, 5,  enemy_pic, text_font)#pygame.Rect(600, 600, 55, 55)
battle = Battle(enemy, hero, battle_pic)
loot_pic = pygame.transform.scale(pygame.image.load("loot_2.jpg"), (55, 55))

loot = [Item("head", loot_pic, "headloot" ), Item("sword", loot_pic, "headloot")]

quest = Quest("headloot", pygame, text_font, "Mimi", battle, "Hi, take this mushroom and kill that god", black_canvas, loot, "Godslayer")

scene = SCENE(the_well, hero, npc1, [pygame.Rect(600, 280, 200, 200), pygame.Rect(50, 100, 200, 200)], enemy, quest)

while True:
    #scene.draw(pygame, window)
    scene.moving(pygame, window)
    #scene.actions(pygame, window)
    pygame.display.update()