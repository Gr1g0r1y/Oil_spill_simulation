import sys
import pygame as pg
from pygame.locals import *
import math
import colors as color
import config as cfg

from sprites import Fish, fishKelledCounter
from random import randint

pg.init()

fpsClock = pg.time.Clock()

screen = pg.display.set_mode((cfg.WIDTH, cfg.HEIGHT))

startProcess = False
startTime = 0

fishes = pg.sprite.Group()
for _ in range(cfg.FISH_COUNT):
    f = Fish(randint(0, cfg.WIDTH), randint(0, cfg.HEIGHT - 100), "img.png")
    fishes.add(f)

myfont = pg.font.SysFont("monospace", 15)


# render text
# class Timer():
#     def __init(self, current_time):
    

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
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width
    
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(screen, self.color, self.rect, 2)


class Oil:
    def __init__(self, k0=0.5, d_p=1, Q=1, mu_0=1, q=1):
        self.startTime = 0
        g = 9.81
        a = 2 * math.pi * k0 * (q ** 2) / (d_p * g * mu_0 * Q)
        f = (a - (a ** 2 + 2 * a) ** 0.5 + 1) ** 0.125
        self.const_for_r = (k0 / math.pi ** 3) ** 0.125 * ((d_p * g * Q ** 3) / mu_0) ** 0.125 * f
        self.max_r = 250
    
    def run(self, startTime: int):
        self.startTime = startTime
    
    def getNewRadius(self, currentTime) -> int:
        time = currentTime - self.startTime
        r = self.const_for_r * math.sqrt(time)
        if r > self.max_r:
            return round(self.max_r)
        return round(r)
    
    def draw(self, screen, current_time):
        currentRadius = self.getNewRadius(current_time)
        pg.draw.circle(screen, color.BLACK, (cfg.WIDTH // 2, (cfg.HEIGHT - 200) // 2), currentRadius)


img = pg.image.load("img.png")

input_box_Q = InputBox(220, 540, 140, 32)
input_box_d_p = InputBox(220, 610, 140, 32)
input_box_q = InputBox(530, 540, 140, 32)
input_box_mu = InputBox(530, 610, 140, 32)

input_boxes = [input_box_d_p, input_box_Q, input_box_mu, input_box_q]
# Game loop.
while True:
    screen.fill(color.ICE_BLUE)
    
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            ms_x, ms_y = pg.mouse.get_pos()
            if 20 <= ms_x <= 120 and 620 <= ms_y <= 670:
                Oil = Oil(d_p=float(input_box_d_p.text), q=float(input_box_q.text), mu_0=float(input_box_mu.text),
                          Q=float(input_box_Q.text))
                startProcess = True
                Oil.run(pg.time.get_ticks())
        
        for box in input_boxes:
            box.handle_event(event)
    
    # fishes.draw(screen)
    
    # pg
    pg.draw.rect(screen, color.PANEL, (0, 500, cfg.WIDTH, 200))
    pg.draw.rect(screen, color.START_BUTTON, (20, 620, 100, 50))
    
    for box in input_boxes:
        box.update()
        box.draw(screen)
    
    if startProcess:
        Oil.draw(screen, pg.time.get_ticks())
    
    # label = myfont.render(f"{fishKelledCounter}", 20, (255,0,0))
    # screen.blit(label, (100, 100))
    
    myfont = pg.font.SysFont("monospace", 15)
    f_p = pg.font.SysFont('arial', 48)
    text_Q = f_p.render("Q =", 2, (0, 0, 0))
    text_mu = f_p.render("μ =", 2, (0, 0, 0))
    text_q = f_p.render("δ =", 2, (0, 0, 0))
    text_d_p = f_p.render("Δρ =", 2, (0, 0, 0))
    label = myfont.render(f"Fishs alive: {cfg.FISH_COUNT - fishKelledCounter}", 2, (255, 0, 0))
    
    # Отрисовка текста на основном окне игры
    screen.blit(label, (10, 10))
    
    screen.blit(text_Q, (150, 529))
    screen.blit(text_d_p, (132, 599))
    screen.blit(text_mu, (460, 529))
    screen.blit(text_q, (460, 599))
    
    pg.display.flip()
    fpsClock.tick(cfg.FPS)
