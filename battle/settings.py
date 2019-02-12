# encoding = utf-8


class Settings():
    """设置信息类"""

    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船速度设置
        self.ship_speed = 1.5
        # 子弹设置
        self.bullet_speed = 0.6
        self.bullet_width = 3
        self.bullet_height = 8
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 4
