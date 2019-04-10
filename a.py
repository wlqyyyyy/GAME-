import pygame
import sys

from map import Map   # 从map模块中导入Map这个类
from hero import Hero    # 从hero模块中导入Hero这个类
from enemy import Enemy

WIN_WIDTH = 512
WIN_HEIGHT = 768


class PlaneWar(object):

    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
        self.set_window()
        self.map = Map(window)
        self.hero = Hero(window)
        self.enemy = [Enemy(window) for _ in range(4)]

    @staticmethod
    def set_window():
        pygame.display.set_caption("飞机大战v1.0")
        icon = pygame.image.load("res/game.ico")
        pygame.display.set_icon(icon)
        pygame.display.set_icon(icon)
        pygame.mixer.music.load("./res/bg2.ogg")
        pygame.mixer.music.play(-1)

    def events(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                print("关闭了窗口")
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    # print("按了 空格")
                    self.hero.shoot()

    def move(self):
        self.map.move()
        self.hero.move()

        for i in self.hero.bullets:
            i.move()

        for j in self.enemy:
            j.move()

    def blit(self):
        self.map.blited()
        self.hero.blited()
        for i in self.enemy:
            i.blited()

    def display(self):
        pygame.display.update()

    def is_bullet_hit_enemy(self):

        for i in self.hero.bullets:  
            for j in self.enemy:  
                if pygame.Rect.colliderect(i.rect, j.rect):
                    j.reset()

    def is_hero_hit_enemy(self):

        for i in self.enemy:
            if pygame.Rect.colliderect(i.rect, self.hero.rect):
                return True
        else:
            return False

    def gameover(self):
        pygame.mixer.music.stop()
        boom_sound = pygame.mixer.Sound("./res/gameover.wav")
        boom_sound.play()
        while True:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    print("关闭了窗口")
                    sys.exit()

    def run(self):

        while True:
            self.events()
            self.move()
            self.is_bullet_hit_enemy()

            if self.is_hero_hit_enemy():
                break

            self.blit()
            self.display()
        self.gameover()

if __name__ == "__main__":
    game = PlaneWar()
    game.run()
