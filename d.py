import pygame
import random
WIN_WIDTH = 512
WIN_HEIGHT = 768

class Enemy(object):
    def __init__(self, win):
        self.img = pygame.image.load("res/3.png" % random.randint(1, 7))
        self.window = win
        self.rect = self.img.get_rect()

        self.rect[1] = random.randint(-100, 50)
        self.rect[0] = random.randint(0, WIN_WIDTH-self.rect[2])
        self.speed = random.randint(25, 50) * 0.1

    def move(self):
        self.rect[1] += self.speed
        # pass

        if self.rect[1] > WIN_HEIGHT:
            self.reset()

    def reset(self):
        self.img = pygame.image.load("res/3.png" % random.randint(1, 7))
        self.rect[1] = random.randint(-100, 50)
        self.rect[0] = random.randint(0, WIN_WIDTH - self.rect[2])
        self.speed = random.randint(30, 50) * 0.1

    def blited(self):
        self.window.blit(self.img, (self.rect[0],self.rect[1]))
