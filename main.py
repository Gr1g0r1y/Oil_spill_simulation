import pygame as pg
import colors as color
import config as cfg
from objects import Fish, Oil
from tkinter import *





if __name__ == "__main__":
    pg.init()
    fpsClock = pg.time.Clock()
    screen = pg.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
    startTime = 0
    
    f = open('file.txt')
    d_of_v = dict()
    for line in f:
        key, item = map(str, line.split('='))
        d_of_v[key] = float(item)
    
    
    
    while True:
        screen.fill(color.ICE_BLUE)
        
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                pg.quit()
                sys.exit()
        oil = Oil()
        oil.run(pg.time.get_ticks())
        oil.draw(screen, pg.time.get_ticks())
        text_time = pg.font.SysFont('arial', 40).render(f"t = {oil.time // 100 / 10}s", 2, (0, 0, 0))
        text_r = pg.font.SysFont('arial', 40).render(f"A = {oil.get_new_V(pg.time.get_ticks())} м", 2, (0, 0, 0))
        text_s = pg.font.SysFont('arial', 40).render(f"S = {round(oil.get_square())} м^2", 2, (0, 0, 0))
        text_h = pg.font.SysFont('arial', 40).render(f"H = {round(oil.get_h() * 1000, 1)} * 10^5 м", 2, (0, 0, 0))
        
        pg.draw.rect(screen, color.PANEL, (cfg.WIDTH - 350, cfg.HEIGHT - 250, cfg.WIDTH, cfg.HEIGHT))
        
        screen.blit(text_time, (cfg.WIDTH - 300, 500))
        screen.blit(text_r, (cfg.WIDTH - 300, 550))
        screen.blit(text_s, (cfg.WIDTH - 300, 600))
        screen.blit(text_h, (cfg.WIDTH - 300, 650))

        pg.display.flip()
        fpsClock.tick(cfg.FPS)
