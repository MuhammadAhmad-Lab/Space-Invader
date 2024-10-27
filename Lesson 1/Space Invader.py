import math
import random
import pygame

Screen_Width = 800
Screen_Height = 500
Player_Start_X = 370
Player_Start_Y = 380
Enemy_Start_Y_Min = 50
Enemy_Start_X_Min = 150
Enemy_Speed_X = 4
Enemy_Speed_Y = 40
Bullet_Speed_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((Screen_Width, Screen_Height))
background = pygame.image.load('https://www.google.com/imgres?q=galaxy%20cartoon&imgurl=https%3A%2F%2Fpics.craiyon.com%2F2023-06-27%2Fc129c445d61b4c2a9b0ef6378e9aca26.webp&imgrefurl=https%3A%2F%2Fwww.craiyon.com%2Fimage%2FZ2g_S6ItTzK77uudWk8HgQ&docid=mVVhRHMkF_OdxM&tbnid=ppn0R5LN58gm2M&vet=12ahUKEwi84JDA0q6JAxUf-QIHHcvIGUEQM3oECGcQAA..i&w=1024&h=1024&hcb=2&ved=2ahUKEwi84JDA0q6JAxUf-QIHHcvIGUEQM3oECGcQAA')
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load('')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('')
playerX = Player_Start_X
playerY = Player_Start_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(''))
    enemyX.append(random.randint(Enemy_Start_Y))