#encoding = utf-8
import pygame
from pygame.sprite import Sprite
'''子弹类'''


class Bullet(Sprite):
    '''对飞船发射的子弹进行管理的类'''

    def __init__(self, ai_settings, screen, ship):
        '''在飞船所处的地方创建一个子弹'''
        super(Bullet, self).__init__()  # 也可以使用super().__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形,再设置正确的位置
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        '''向上移动子弹'''
        # 更新表示子弹位置的小数值
        self.y -= self.speed
        # 更新表示子弹rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上画子弹'''
        pygame.draw.rect(self.screen, self.color, self.rect)
