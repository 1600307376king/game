import sys
import pygame
from pokemon_game.config import *
from pokemon_game.role.lead import *


# 背景
class BackgroundImage(object):

    def __init__(self):
        self.images = [pygame.image.load(IMAGE_PATH + 'background/bg.png')]
        self.image_width, self.image_height = self.images[0].get_rect()[2:]

        self.position_x = (WIDTH - self.image_width) / 2
        self.position_y = (HEIGHT - self.image_height) / 2

    def get_position(self, i=0):
        return self.images[i].get_rect(left=self.position_x, top=self.position_y)


pygame.init()

screen = pygame.display.set_mode(SIZE)  # 设置屏幕大小
bgi = BackgroundImage()  # 创建背景对象
pos = bgi.get_position()  # 背景矩形对象
lead = Lead()   # 创建主角对象
clock = pygame.time.Clock()  # 创建时钟
wt = 0  # 角色每步计时变量
frame_number = 0
while True:
    clock.tick(60)  # 每秒60次
    frame_number += 1
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        # 此判断角色是否走完一格

        if event.type == pygame.KEYDOWN:
            lead.walk_time_frequency = 1
            lead.is_walk = True
            # 判断是否按下
            if event.key == pygame.K_DOWN:
                lead.direction = 0
            elif event.key == pygame.K_LEFT:
                lead.direction = 4
            elif event.key == pygame.K_UP:
                lead.direction = 8
            elif event.key == pygame.K_RIGHT:
                lead.direction = 12
    key_press = pygame.key.get_pressed()
    # 判断是否持续按压
    if key_press[pygame.K_DOWN]:
        lead.is_continued = 1
    elif key_press[pygame.K_LEFT]:
        lead.is_continued = 1
    elif key_press[pygame.K_UP]:
        lead.is_continued = 1
    elif key_press[pygame.K_RIGHT]:
        lead.is_continued = 1
    else:
        lead.is_continued = 0

    screen.fill(game_background)
    screen.blit(bgi.images[0], pos)

    wt = lead.update_state(pos, screen, frame_number)

    pygame.display.flip()

pygame.quit()
