import sys
import pygame

SIZE = WIDTH, HEIGHT = 1280, 720
IMAGE_PATH = './pokemon_game/image/'
green = 0, 0, 0
game_background = green


# 主角
class Lead(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMAGE_PATH + 'lead/1.png').convert_alpha()
                       # pygame.image.load(IMAGE_PATH + 'lead/2.png'),
                       # pygame.image.load(IMAGE_PATH + 'lead/3.png'),
                       # pygame.image.load(IMAGE_PATH + 'lead/4.png')]

        # self.image_width, self.image_height = self.images[0].get_rect()[2:]
        #
        # self.position_x = (WIDTH - self.image_width) / 2
        # self.position_y = (HEIGHT - self.image_height) / 2
        # self.walk_frequency = 10  # 每10帧刷新动图
        # self.left_move = 0  # 横向移动
        # self.up_move = 0  # 纵向移动速度
        # self.is_walk = False  # 是否走路
        # self.walk_speed = 2  # 走路速度
        # self.is_run = False  # 是否跑步
        # self.run_speed = 0  # 跑步速度

        self.rect = self.image.get_rect()
        self.image_width, self.image_height = self.rect[2:]
        self.position_x = (WIDTH - self.image_width) / 2
        self.position_y = (HEIGHT - self.image_height) / 2
        self.walk_speed = 5

    def move_up(self):
        if self.rect.top > 0:
            self.rect.top -= self.walk_speed

        else:
            self.rect.top = 0

    def move_down(self):
        if self.rect.bottom < HEIGHT:
            self.rect.top += self.walk_speed
        else:
            self.rect.bottom = HEIGHT

    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.walk_speed
        else:
            self.rect.left = 0

    def move_right(self):
        if self.rect.right < WIDTH:
            self.rect.right += self.walk_speed
        else:
            self.rect.right = WIDTH


# 背景
class BackgroundImage(object):

    def __init__(self):
        self.images = [pygame.image.load(IMAGE_PATH + 'background/bg.png')]
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

        if event.type == pygame.QUIT:
            sys.exit()
    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_UP]:
        lead.move_up()
    if key_press[pygame.K_RIGHT]:
        lead.move_right()
    if key_press[pygame.K_DOWN]:
        lead.move_down()
    if key_press[pygame.K_LEFT]:
        lead.move_left()

    screen.blit(bgi.images[0], pos)
    screen.blit(lead.image, lead.rect)

    pygame.display.flip()

pygame.quit()
