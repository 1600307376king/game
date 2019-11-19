import sys
import pygame

SIZE = WIDTH, HEIGHT = 1280, 720
IMAGE_PATH = './pokemon_game/image/'
green = 0, 0, 0
game_background = green
per_press_max_frame_number = 72


# 主角
class Lead(object):

    def __init__(self):
        # 初始化图片名称列表并加载
        self.image_name_label = ['d', 'l', 'r', 'u']
        self.image_name_list = []
        for i in self.image_name_label:
            for k in range(4):
                self.image_name_list.append(i + str(k + 1) + '.png')

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
        self.walk_speed = 2  # 走路速度
        self.is_run = False  # 是否跑步
        self.run_speed = 0  # 跑步速度

    def get_position(self, i=0):
        return self.images[i].get_rect(left=self.position_x, top=self.position_y)

    def lead_move(self):
        pass


# 背景
class BackgroundImage(object):

    def __init__(self):
        self.images = [pygame.image.load(IMAGE_PATH + 'background/game_bg.png')]
        self.image_width, self.image_height = self.images[0].get_rect()[2:]

        self.position_x = (WIDTH - self.image_width) / 2
        self.position_y = (HEIGHT - self.image_height) / 2

    def get_position(self, i=0):
        return self.images[i].get_rect(left=self.position_x, top=self.position_y)


pygame.init()

screen = pygame.display.set_mode(SIZE)
bgi = BackgroundImage()
pos = bgi.get_position()
lead = Lead()
clock = pygame.time.Clock()

while True:
    clock.tick(60)  # 每秒60次

    for event in pygame.event.get():
        key_press = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            lead.walk_time_frequency = 1
            lead.is_walk = True

    pos.top -= lead.walk_time_frequency

    lead.walk_time -= lead.walk_time_frequency
    if lead.walk_time > 72:
        lead.walk_time = 0
        lead.walk_time_frequency = 0
        lead.is_walk = False
        lead.image_frame = 0

    screen.fill(game_background)
    screen.blit(bgi.images[0], pos)
    screen.blit(lead.images[lead.image_frame], lead.get_position())
    if lead.is_walk:
        if lead.walk_time % 9 == 0:
            lead.image_frame += 1
            if lead.image_frame > 3:
                lead.image_frame = 0

    pygame.display.flip()

pygame.quit()
