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
    def __init__(self, startTime=0, ro_w=1100, ro_0=860, scale=50, g=9.81, mu=0.05, kin_vis_w=1.519, v0=10, kin_vis_0=0.05,
                 p_a=1.2754, C_d=0.005, W_x=100, W_y=10 ** -10, fi=1, horseshoe=7.2921 * 10 ** (-5), u_w=1, v_w=1, max_t=100):
        self.ro_w = ro_w
        self.scale = scale
        self.ro_0 = ro_0
        self.g = g
        self.mu = mu
        self.kin_vis_w = kin_vis_w
        self.v0 = v0
        self.kin_vis_0 = kin_vis_0
        self.p_a = p_a
        self.C_d = C_d
        self.W_x = W_x
        self.W_y = W_y
        self.horseshoe = horseshoe * 10 ** (-5)
        self.fi = fi * math.pi / 180
        self.u_w = u_w
        self.v_w = v_w

        self.s_x = 0
        self.s_y = 0
        self.u_d = 0
        self.v_d = 0
        self.r = 0
        self.h = 0
        self.time = 0
        self.startTime = startTime
        self.s = 0
        self.square = 0
        self.max_time = max_t * 100
    
    def run(self, startTime: int):
        self.startTime = startTime
    
    def get_h(self):
        return self.h
    
    def get_new_V(self, currentTime):
        if self.time > self.max_time:
            return (0, 0)
        else:
            t = (currentTime - self.startTime + 10 ** (-10)) / 100000
            e0 = 4 / 162 ** 0.125  # 1
            d = (self.ro_w - self.ro_0) / self.ro_0  # 3
            alf = self.ro_0 * d * self.g / (4 * self.mu)  # 2
            d_w = 1.72 * (self.kin_vis_w * t)  # 4
            h = (e0 ** (2 / 3)) * ((self.v0 / 2 / math.pi / alf / t) ** 0.25) * (3 ** (1 / 3)) / 4  # 12
            b1 = 1 + (self.ro_0 * self.kin_vis_0 * d_w) / (
                    self.ro_w * self.kin_vis_w * h + self.ro_0 * self.kin_vis_0 * d_w)  # 6
            b2 = 1 - (self.ro_0 * self.kin_vis_0 * d_w) / (
                    self.ro_w * self.kin_vis_w * h + self.ro_0 * self.kin_vis_0 * d_w)  # 5
            y = (self.ro_0 * self.kin_vis_0 * self.kin_vis_w) / (
                    self.ro_w * self.kin_vis_w * h + self.ro_0 * self.kin_vis_0 * d_w)  # 7
            t_0_x = self.p_a * self.C_d * (self.W_x - self.u_d) * abs(self.W_x - self.u_d)  # 8
            t_0_y = self.p_a * self.C_d * (self.W_y - self.v_d) * abs(self.W_y - self.v_d)  # 9
            # print(t_0_y, self.v_d)
            f = 2 * self.horseshoe * math.sin(self.fi)  # 10
            r = e0 * ((self.v0 ** 3 * alf * t) / (8 * math.pi ** 3)) ** 0.125  # 11
            d_r = r - self.r
            self.r = r
            d_h = self.h - h
            self.h = h
            U_0 = (self.ro_0 * d * self.g * h ** 2) / self.mu * (d_h / d_r)  # 13
            u_wd = t_0_x / (self.ro_0 * h * f)  # 15
            v_wd = t_0_y / (self.ro_0 * h * f)  # 16
            u_cd = (((2 * y / (f * h * b1)) ** 2 - b2 / b1) * self.u_w + (b2 / b1 + 1) * self.v_w * 2 * y / (
                    f * h * b1)) / (
                       1 + (2 * y / (f * h * b1)) ** 2)
            v_cd = (((2 * y / (f * h * b1)) ** 2 - b2 / b1) * self.v_w + (b2 / b1 + 1) * self.u_w * 2 * y / (
                    f * h * b1)) / (
                       1 + (2 * y / (f * h * b1)) ** 2)
            self.u_d = u_wd + u_cd
            self.v_d = v_wd + v_cd
            self.time = t * 10000
            return (u_cd + U_0, U_0 - v_cd)
    
    def getNewVx(self, currentTime):
        pass
    
    def getNewVy(self, currentTime):
        pass
    
    def draw(self, screen, current_time):
        cort_v = self.get_new_V(current_time)
        self.s_x = self.s_x + cort_v[0] / self.scale
        self.s_y = self.s_y + cort_v[1] / self.scale
        self.a = math.acos(self.s_x / ((self.s_x ** 2 + self.s_y ** 2) ** 0.5 + 0.000000001))
        self.mini_r = round(self.s_y / math.cos(self.a))
        self.centre_of_circle = (round((self.s_x + math.tan(self.a) * self.s_y)), cfg.HEIGHT // 2)
        self.l = (self.s_x + math.tan(self.a) * self.s_y) + self.mini_r
        pg.draw.circle(screen, color.BLACK, self.centre_of_circle, self.mini_r)
        self.p1 = [0, cfg.HEIGHT // 2]
        self.p2 = [0 + round(self.s_x), cfg.HEIGHT // 2 + round(self.s_y)]
        self.p3 = [0 + round(self.s_x), cfg.HEIGHT // 2 - round(self.s_y)]
        pg.draw.polygon(screen, color.BLACK, [self.p1, self.p2, self.p3])
        self.square = self.s_y * self.scale * self.centre_of_circle[0] * self.scale + (self.mini_r * self.scale) ** 2 * (math.pi + 2 * self.a) / 2
