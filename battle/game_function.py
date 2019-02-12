# encoding = utf-8
import sys
import pygame
from bullet import Bullet
from alien import Alien
"""游戏需要的方法类"""


def check_events(ai_settings, screen, ship, bullets):
    '''监视键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    '''按键响应'''
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        # 创建子弹
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    '''创建子弹,并限制子弹的数量'''
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, ship):
    '''按键响应'''
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets, aliens):
    '''跟新屏幕上的图像'''
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def create_fleet(ai_settings, screen, aliens):
    """"创建外星人群"""
    # 创建外星人,并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)

    number_aliens_x = get_number_alien_x(ai_settings,alien.rect.width)


    # create a alien
    for alien_number in range(number_aliens_x):
        # create a alien and add aliens
        create_alien(ai_settings,screen,aliens,alien_number)

def get_number_alien_x(ai_settings,alien_width):
    """计算每行可以容下多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings,screen,aliens,alien_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)



def update_bullet(bullets):
    '''更新子弹的状态'''
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
