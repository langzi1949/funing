# encoding = utf-8
import pygame
"""飞船类"""


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并且设置初始化位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像
        #E:/funing/battle/images/ship.bmp 这个是win上
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标记
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞船的位置,并且保证飞机的位置不能在屏幕外'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
