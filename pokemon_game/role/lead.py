#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 0020 9:27
# @Author  : HelloWorld
# @File    : lead.py

import pygame
from pokemon_game.config import *


def change_direction(d):
    res = {'0': (-1, 0), '4': (0, 1), '8': (1, 0), '12': (0, -1)}
    return res[str(d)]


# 主角
class Lead(object):

    def __init__(self):
        # 初始化图片名称列表并加载

        self.image_name_list = [str(i + 1) + '.png' for i in range(16)]

        self.images = [pygame.image.load(IMAGE_PATH + 'lead/' + j) for j in self.image_name_list]

        self.image_width, self.image_height = self.images[0].get_rect()[2:]

        # 设置角色初始坐标
        self.position_x = (WIDTH - self.image_width) / 2
        self.position_y = (HEIGHT - self.image_height) / 2
        self.walk_frequency = 8   # 图片切换频率 越小越快
        self.image_frame = 0  # 角色走路动画帧
        self.walk_time_frequency = 0  # 开始走路频率
        self.left_move = 0  # 横向移动
        self.up_move = 0  # 纵向移动速度
        self.is_walk = False  # 是否走路
        self.speed = 4  # 走路速度
        self.press_time = 0  # 方向键按键持续时间
        self.direction = 0  # 角色方向 0 -> 下 4 -> 左 8 -> 上 12 -> 右
        self.is_continued = 0  # 是否持续运动

    def get_position(self, i=0):
        return self.images[i].get_rect(left=self.position_x, top=self.position_y)

    def update_state(self, pos, screen, frame_number):
        pos.top = pos.top + change_direction(self.direction)[0] * self.walk_time_frequency * self.speed
        pos.left = pos.left + change_direction(self.direction)[1] * self.walk_time_frequency * self.speed

        # 角色停止运动 相关数值恢复到初始值
        if self.is_continued == 0:
            self.is_walk = False
            self.walk_time_frequency = 0
            self.speed = 4
            self.walk_frequency = 8
            self.press_time = 0

        # 角色走路持续按到一定时间，速度增加
        if self.is_continued == 1:
            self.press_time += 1
            if self.press_time >= 30:
                self.speed = 8
                self.walk_frequency = 4

        # 控制主角动画频率
        if self.is_walk:
            if frame_number % self.walk_frequency == 0:
                self.image_frame += 1
            if self.image_frame > 3:
                self.image_frame = 0
            screen.blit(self.images[self.direction + self.image_frame], self.get_position())
        else:
            screen.blit(self.images[self.direction + 0], self.get_position())




