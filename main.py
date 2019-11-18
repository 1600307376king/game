import sys
import pygame
from pygame.locals import *


pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

green = 0, 0, 0
game_background = green
bg_img = pygame.image.load('./sc/start_home.png')
bg_img_rect = bg_img.get_rect()
walk_lead = pygame.image.load('./sc/1.png')
lead_rect = walk_lead.get_rect()
speed = [1, 1]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:

                bg_img_rect.left -= 1
            if event.key == K_LEFT:
                bg_img_rect.right += 1
            if event.key == K_DOWN:
                bg_img_rect.bottom -= 1
            if event.key == K_UP:
                bg_img_rect.top += 1

    lead_rect.left = (width - lead_rect.width) / 2
    lead_rect.top = (height - lead_rect.height) / 2
    screen.fill(game_background)
    screen.blit(bg_img, bg_img_rect)
    screen.blit(walk_lead, lead_rect)
    pygame.display.flip()


pygame.quit()




