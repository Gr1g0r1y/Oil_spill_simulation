import sys
import math
from random import randint

import pygame as pg
from pygame.locals import *

import colors as color
import config as cfg
from objects import Fish, InputBox, Oil

if __name__ == "__main__":
    pg.init()
    
    fpsClock = pg.time.Clock()
    screen = pg.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
    
    startProcess = False
    fishKelledCounter = 0
    startTime = 0
    
    fishes = pg.sprite.Group()
    for _ in range(cfg.FISH_COUNT):
        f = Fish(randint(0, cfg.WIDTH), randint(0, cfg.HEIGHT - 100))
        fishes.add(f)
    
    img = pg.image.load("img.png")
    
    input_box_Q = InputBox(220, 540, 100, 32)
    input_box_d_p = InputBox(220, 610, 100, 32)
    input_box_q = InputBox(455, 540, 100, 32)
    input_box_mu = InputBox(455, 610, 100, 32)
    input_box_V = InputBox(670, 540, 100, 32)
    input_box_Z = InputBox(670, 610, 100, 32)
    
    input_boxes = [
        input_box_d_p, input_box_Q,
        input_box_mu, input_box_q,
        input_box_V, input_box_Z
    ]
    
    scoreFont = pg.font.SysFont("monospace", 15)
    f_p = pg.font.SysFont('arial', 48)
    text_Q = f_p.render("Q =", 2, (0, 0, 0))
    text_mu = f_p.render("μ =", 2, (0, 0, 0))
    text_q = f_p.render("δ =", 2, (0, 0, 0))
    text_d_p = f_p.render("Δρ =", 2, (0, 0, 0))
    text_v = f_p.render("V =", 2, (0, 0, 0))
    text_zalupa = f_p.render("x =", 2, (0, 0, 0))
    text_s = f_p.render("S = 0", 2, (0, 0, 0))
    text_h = pg.font.SysFont('arial', 40).render("H = 0 см", 2, (0, 0, 0))
    
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
                    oil = Oil(d_p=float(input_box_d_p.text), q=float(input_box_q.text), mu_0=float(input_box_mu.text),
                              Q=float(input_box_Q.text), V=float(input_box_V.text), zalupa=float(input_box_Z.text))
                    startProcess = True
                    oil.run(pg.time.get_ticks())
            
            for box in input_boxes:
                box.handle_event(event)
        
        if startProcess:
            oil.draw(screen, pg.time.get_ticks())
            fishes.update(oil)
            text_time = pg.font.SysFont('arial', 40).render(f"t = {oil.time // 100 / 10}s", 2, (0, 0, 0))
            text_r = pg.font.SysFont('arial', 40).render(f"R = {oil.getNewRadius(pg.time.get_ticks())} м", 2, (0, 0, 0))
            text_s = pg.font.SysFont('arial', 40).render(f"S = {round(oil.get_square())} м^2", 2, (0, 0, 0))
            text_h = pg.font.SysFont('arial', 40).render(f"H = {round(oil.get_h() * 1000, 1)} * 10^5 м", 2, (0, 0, 0))
        else:
            fishes.update(None)
            text_time = pg.font.SysFont('arial', 40).render("t = 0s", 2, (0, 0, 0))
            text_r = pg.font.SysFont('arial', 40).render("R = 0 м", 2, (0, 0, 0))
        
        # fishes
        fishes.draw(screen)
        
        # panel
        pg.draw.rect(screen, color.PANEL, (0, 500, cfg.WIDTH, 200))
        pg.draw.rect(screen, color.START_BUTTON, (20, 620, 100, 50))
        
        for f in fishes:
            fishKelledCounter += f.getPoint()
        
        for box in input_boxes:
            box.update()
            box.draw(screen)
        
        screen.blit(text_time, (800, 500))
        screen.blit(text_r, (800, 550))
        screen.blit(text_s, (800, 600))
        screen.blit(text_h, (800, 650))
        label = scoreFont.render(f"Fishs alive: {cfg.FISH_COUNT - fishKelledCounter}", 2, (255, 0, 0))
        
        # Отрисовка текста на основном окне игры
        screen.blit(label, (10, 10))
        
        screen.blit(text_Q, (145, 529))
        screen.blit(text_d_p, (127, 599))
        screen.blit(text_mu, (390, 529))
        screen.blit(text_q, (390, 599))
        screen.blit(text_v, (600, 529))
        screen.blit(text_zalupa, (608, 599))


        pg.display.flip()
        fpsClock.tick(cfg.FPS)
