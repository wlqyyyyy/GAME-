import pygame

WIN_WIDTH = 512
WIN_HEIGHT = 768


class Map(object):
    def __init__(self, win):
        self.img = pygame.image.load("res/img_bg_level_2.jpg")
        self.img2 = pygame.image.load("res/img_bg_level_2.jpg")
        self.window = win

        self.y = 0
        self.y2 = -WIN_HEIGHT

    def move(self):
        self.y += 1
        self.y2 += 1

        if self.y > WIN_HEIGHT:
            self.y = -WIN_HEIGHT
        if self.y2 > WIN_HEIGHT:
            self.y2 = -WIN_HEIGHT

    def blited(self):
        self.window.blit(self.img, (0, self.y))
        self.window.blit(self.img2, (0, self.y2))
