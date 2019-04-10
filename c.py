import pygame

WIN_WIDTH = 512
WIN_HEIGHT = 768

class Bullet(object):
    def __init__(self, win, hero_x, hero_y, hero_w):
        self.img = pygame.image.load("res/2.png")
        self.window = win
        self.rect = self.img.get_rect()

        self.rect[1] = hero_y - self.rect[3]
        self.rect[0] = hero_x + hero_w/2 - self.rect[2]/2

    def move(self):
       self.rect[1] -= 3

    def blited(self):
        self.window.blit(self.img, (self.rect[0],self.rect[1]))
