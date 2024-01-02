import pygame as pg
import config as cfg
from random import randint

fishKelledCounter = 0


class Fish(pg.sprite.Sprite):
    def __init__(self, x, y, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.canSwim = True
        self.hasPoint = True

        
        
    def changeImage(self):
        global fishKelledCounter
        fishKelledCounter += 1
        print("call", fishKelledCounter)
        self.image = pg.transform.rotate(pg.image.load("imgD.png").convert_alpha(), 180)
        # self.rect = self.image.get_rect()
        self.canSwim = False
        
    def update(self, curr_r):
        if not self.canSwim:
            return 0
        
        x = self.rect.centerx
        y = self.rect.centery
        w2, h2 = cfg.WIDTH // 2, cfg.HEIGHT // 2
        
        if x > w2 and y < h2:
            if w2 + curr_r > x and h2 - curr_r < y:
                self.changeImage()
        if x < w2 and y < h2:
            if w2 - curr_r < x and h2 - curr_r < y:
                self.changeImage()
        if x > w2 and y  > h2:
            if w2 + curr_r > x and h2 + curr_r > y:
                self.changeImage()
        if x < w2 and y > h2:
            if w2 - curr_r < x and h2 + curr_r > y:
                self.changeImage()
        
        
        