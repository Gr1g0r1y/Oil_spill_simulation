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


class InputBox:

    def __init__(self, x, y, w, h, text='1'):
        self.rect = pg.Rect(x, y, w, h)
        self.color = color.COLOR_INACTIVE
        self.text = text
        self.txt_surface = pg.font.Font(None, 32).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = color.COLOR_ACTIVE if self.active else color.COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = pg.font.Font(None, 32).render(self.text, True, self.color)

    def update(self):
        width = max(120, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(screen, self.color, self.rect, 2)


class Oil:
    def __init__(self, k0=0.5, d_p=1, Q=1, mu_0=1, q=1, V=1000, zalupa=1):
        self.startTime = 0
        self.v = V
        self.zalupa = zalupa
        g = 9.81
        a = 2 * math.pi * k0 * (q ** 2) / (d_p * g * mu_0 * Q)
        f = (a - (a ** 2 + 2 * a) ** 0.5 + 1) ** 0.125
        self.const_for_r = (k0 / math.pi ** 3) ** 0.125 * ((d_p * g * Q ** 3) / mu_0) ** 0.125 * f
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
        self.a = math.acos(self.s_x / ((self.s_x ** 2 + self.s_y ** 2)**0.5 + 0.000000001))
        self.mini_r = round(self.s_y / math.cos(self.a))
        self.centre_of_circle = (round(self.s_x + math.tan(self.a) * self.s_y), 250)
        pg.draw.circle(screen, color.BLACK, self.centre_of_circle, self.mini_r)
        pg.draw.polygon(screen, color.BLACK, [[0, 250], [0 + round(self.s_x / self.zalupa),
                                                         250 + round(self.s_y / self.zalupa)],
                                              [0 + round(self.s_x / self.zalupa),
                                               250 - round(self.s_y / self.zalupa)]])
