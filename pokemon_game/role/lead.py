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


def frame_list(frequency=4):
    ls = []
    for i in range(frequency):
        for j in range(4):
            ls.append(i)
    return ls


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
        self.image_frame = 0  # 角色走路动画帧
        self.walk_time_frequency = 0  # 开始走路频率
        self.walk_time = 0  # 开始走路计时
        self.walk_frequency = 10  # 每10帧刷新动图
        self.left_move = 0  # 横向移动
        self.up_move = 0  # 纵向移动速度
        self.is_walk = False  # 是否走路
        self.walk_speed = 6  # 走路速度
        self.is_run = False  # 是否跑步
        self.run_speed = 0  # 跑步速度
        self.direction = 0  # 角色方向 0 -> 下 4 -> 左 8 -> 上 12 -> 右
        self.is_continued = 0  # 是否持续运动

    def get_position(self, i=0):
        return self.images[i].get_rect(left=self.position_x, top=self.position_y)

    def update_state(self, pos, screen, frame_number):
        pos.top = pos.top + change_direction(self.direction)[0] * self.walk_time_frequency * self.walk_speed
        pos.left = pos.left + change_direction(self.direction)[1] * self.walk_time_frequency * self.walk_speed

        self.walk_time += self.walk_time_frequency
        if self.walk_time > CELL_LENGTH // self.walk_speed:
            self.walk_time = 0
            self.walk_time_frequency = self.is_continued
            self.is_walk = self.is_continued
            self.image_frame = 0

        # 控制主角动画频率
        if self.is_walk:

            if frame_number % 4 == 0:
                self.image_frame += 1
            # if self.walk_time % 9 == 0:
            #
            if self.image_frame > 3:
                self.image_frame = 0
            #     self.image_frame += 1

            screen.blit(self.images[self.direction + self.image_frame], self.get_position())
        else:
            screen.blit(self.images[self.direction + 0], self.get_position())
        # print((self.direction, self.image_frame))
        return self.walk_time


