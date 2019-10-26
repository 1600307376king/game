import sys
import pygame
from pygame.locals import *

pygame.init()
size = width, height = 640, 720
screen = pygame.display.set_mode(size)
game_bg = pygame.image.load('./images/bg.png')
bg_rect = game_bg.get_rect()

piece = pygame.image.load('./images/piece.png')
piece_rect = piece.get_rect()

cursor = pygame.image.load('./images/cursor.png')
cursor_rect = cursor.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # piece_rect = piece_rect.move([1, 1])
    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width() / 2
    y -= cursor.get_height() / 2

    screen.blit(game_bg, bg_rect)
    screen.blit(piece, piece_rect)

    screen.blit(cursor, (x, y))
    pygame.display.flip()

