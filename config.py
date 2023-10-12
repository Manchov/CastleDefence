import pygame
# Game parameters
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 500
PLAYGROUND_WIDTH = 500
PLAYGROUND_HEIGHT = 500
BACKGROUND_COLOR = (0, 0, 0)  # Black

castle_x = (PLAYGROUND_WIDTH - 64) / 2
castle_y = (PLAYGROUND_HEIGHT - 64) / 2

path0 = pygame.image.load('img/Pateka0.bmp')
path1 = pygame.image.load('img/Pateka1.bmp')
path2 = pygame.image.load('img/Pateka2.bmp')
path3 = pygame.image.load('img/Pateka3.bmp')

terrain0 = pygame.image.load('img/terren0.bmp')
terrain1 = pygame.image.load('img/terren1.bmp')
terrain2 = pygame.image.load('img/terren2.bmp')
terrain3 = pygame.image.load('img/terren3.bmp')

cobbleUI = pygame.image.load('img/wall.png')