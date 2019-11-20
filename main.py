import sys
import pygame

SIZE = WIDTH, HEIGHT = 1280, 720
IMAGE_PATH = './pokemon_game/image/'
green = 0, 0, 0
game_background = green


# 主角
class Lead(object):

    def __init__(self):
        self.images = [pygame.image.load(IMAGE_PATH + 'lead/9.png'),
                       pygame.image.load(IMAGE_PATH + 'lead/10.png'),
                       pygame.image.load(IMAGE_PATH + 'lead/11.png'),
                       pygame.image.load(IMAGE_PATH + 'lead/12.png')]

        self.image_width, self.image_height = self.images[0].get_rect()[2:]

        self.position_x = (WIDTH - self.image_width) / 2
        self.position_y = (HEIGHT - self.image_height) / 2
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

    def bg_up(self, i=0):

        return self.images[i].get_rect()


pygame.init()

screen = pygame.display.set_mode(SIZE)
bgi = BackgroundImage()
pos = bgi.get_position()
lead = Lead()
clock = pygame.time.Clock()
k = 0
n = 0
while True:
    clock.tick(60)  # 每秒60次

    for event in pygame.event.get():
        key_press = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type != pygame.KEYDOWN:
            bgi.up_move = 0
            bgi.left_move = 0
            bgi.is_walk = False
            k = 0
        if key_press[pygame.K_UP]:
            bgi.up_move = 1
            bgi.is_walk = True

        if key_press[pygame.K_DOWN]:
            bgi.up_move = -1
            bgi.is_walk = k
            bgi.is_walk = True

        if key_press[pygame.K_RIGHT]:
            bgi.left_move = -1
            bgi.is_walk = k
            bgi.is_walk = True

        if key_press[pygame.K_LEFT]:
            bgi.left_move = 1
            bgi.is_walk = k
            bgi.is_walk = True

    pos = pos.move([lead.walk_speed * bgi.left_move, lead.walk_speed * bgi.up_move])
    # if ball_img_rect.left < 0 or ball_img_rect.right > 640 \
    #         or ball_img_rect.top < 0 or ball_img_rect.bottom > 480:
    #     speed = [0, 0]

    screen.fill(game_background)
    screen.blit(bgi.images[0], pos)
    screen.blit(lead.images[k], lead.get_position())
    if bgi.is_walk:
        if n % 10 == 0:
            k += 1
            if k > 3:
                k = 0
    n += 1

    pygame.display.flip()

pygame.quit()
