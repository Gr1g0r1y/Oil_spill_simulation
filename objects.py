import math as math
import random

import pygame as pg

import config as cfg
import colors as color


class Fish(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.rot = random.choice([True, False])
        self.image = pg.transform.flip(pg.image.load("img.png").convert_alpha(), self.rot, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.canSwim = True
        self.hasPoint = True
    
    def getPoint(self):
        if self.canSwim:
            return 0
        if self.hasPoint:
            self.hasPoint = False
            return 1
        return 0
    
    def changeImage(self):
        self.image = pg.transform.rotate(pg.image.load("imgD.png").convert_alpha(), 180)
        self.canSwim = False
    
    def update(self, curr_r):
        if not self.canSwim:
            return 0
        
        x = self.rect.centerx
        y = self.rect.centery
        w2, h2 = cfg.WIDTH // 2, (cfg.HEIGHT - 200) // 2
        
        if ((x - w2) ** 2 + (y - h2) ** 2) <= curr_r ** 2:
            self.changeImage()
            return
        
        self.rect.x += 1 if not self.rot else -1
        if self.rect.x > cfg.WIDTH + 50:
            self.rect.x = 0
            self.rect.y = random.randint(0, cfg.HEIGHT - 200)
            return
        if self.rect.x < -50:
            self.rect.x = cfg.WIDTH
            self.rect.y = random.randint(0, cfg.HEIGHT - 200)
            return


class Oil:
    def __init__(self, ro_0=1, bett=1, mu=1, g=1, ro_w=1, V_0=1, h=1, d_h=1, d_r=1, ro_a=1, C_d=1, W_x=1, scale=1):
        self.startTime = 0
        self.v = V_0
        self.scale = scale
        self.ro_0 = ro_0
        self.bett = bett
        self.mu = mu
        self.g = g
        self.ro_w = ro_w
        self.h = h
        self.d_h = d_h
        self.d_r = d_r
        self.ro_a = ro_a
        self.C_d = C_d
        self.W_x = W_x
        g = 9.81
        a = 2 * 232
        f = (a - (a ** 2 + 2 * a) ** 0.5 + 1) ** 0.125
        self.const_for_r = (h / math.pi ** 3) ** 0.125 * ((mu * g * C_d ** 3) / d_h) ** 0.125 * f
        self.max_r = 2500
        self.currentRadius = 0
    
    def run(self, startTime: int):
        self.startTime = startTime
    
    def get_square(self):
        return math.pi * self.currentRadius ** 2
    
    def get_h(self):
        if self.get_square() == 0:
            return self.v
        return self.v / self.get_square()
    
    def getNewRadius(self, currentTime) -> int:
        time = currentTime - self.startTime
        self.time = time
        r = self.const_for_r * math.sqrt(time)
        if r > self.max_r:
            return round(self.max_r, 2)
        return round(r, 2)
    
    def getNewVx(self, currentTime):
        pass
    
    def getNewVy(self, currentTime):
        pass
    
    def draw(self, screen, current_time):
        self.currentRadius = self.getNewRadius(current_time)
        self.s_x = self.currentRadius
        self.s_y = self.currentRadius
        self.a = math.acos(self.s_x / ((self.s_x ** 2 + (2 * self.s_y) ** 2) ** 0.5 + 0.000000001))
        self.mini_r = round(2 * self.s_y / math.cos(self.a) / self.scale)
        self.centre_of_circle = (round((self.s_x + math.tan(self.a) * 2 * self.s_y) / self.scale), cfg.HEIGHT // 2)
        pg.draw.circle(screen, color.BLACK, self.centre_of_circle, self.mini_r)
        self.p1 = [0, cfg.HEIGHT // 2]
        self.p2 = [0 + round(self.s_x / self.scale), cfg.HEIGHT // 2 + 2 * round(self.s_y / self.scale)]
        self.p3 = [0 + round(self.s_x / self.scale), cfg.HEIGHT // 2 - 2 * round(self.s_y / self.scale)]
        pg.draw.polygon(screen, color.BLACK, [self.p1, self.p2, self.p3])
