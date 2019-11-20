#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 0020 9:27
# @Author  : HelloWorld
# @File    : lead.py

import pygame
from pokemon_game.config import *


class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(IMAGE_PATH + '/obstacle/obstacle.png')

        self.image_width, self.image_height = self.image.get_rect()[2:]

        # 设置角色初始坐标
        self.position_x = 0
        self.position_y = 0

        # 精灵碰撞检测必写定义
        self.rect = self.image.get_rect(left=self.position_x, top=self.position_y)


    def get_position(self):
        return self.image.get_rect(left=self.position_x, top=self.position_y)

    def update_state(self, screen, pos2):
        self.position_x = pos2.left
        self.position_y = pos2.top

        screen.blit(self.image, pos2)

