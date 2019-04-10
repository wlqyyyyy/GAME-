import pygame
from bullet import Bullet

WIN_WIDTH = 512
WIN_HEIGHT = 768


class Hero(object):
    def __init__(self, win):
        self.img = pygame.image.load("res/1.png")
        self.window = win
        self.rect = self.img.get_rect()

        self.rect[1] = 600
        self.rect[0] = WIN_WIDTH / 2 - self.rect[2] / 2
        self.speed = 2
        self.bullets = []

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            if self.rect[1] > 0:
                self.rect[1] -= self.speed
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            if self.rect[1] < (WIN_HEIGHT - self.rect[3]):
                self.rect[1] += self.speed
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self.rect[0] > 0:
                self.rect[0] -= self.speed
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if self.rect[0] < (WIN_WIDTH - self.rect[2]):
                self.rect[0] += self.speed

    def shoot(self):
        self.bullets.append(Bullet(self.window, self.rect[0], self.rect[1], self.rect[2]))

    def blited(self):
        self.window.blit(self.img, (self.rect[0],self.rect[1]))

        for i in self.bullets:
            if i.rect[1] < 0:
                self.bullets.remove(i)
            else:
                i.blited()
