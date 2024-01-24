import pygame as pg
import colors as color
import config as cfg
from objects import Fish, Oil
from tkinter import *





if __name__ == "__main__":
    pg.init()
    fpsClock = pg.time.Clock()
    pg.display.set_icon(pg.image.load('logo.png'))
    pg.display.set_caption('SIMULATION')
    screen = pg.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
    startTime = 0
    
    f = open('variables.txt')
    d_of_v = dict()
    for line in f:
        key, item = map(str, line.split('='))
        d_of_v[key] = float(item)
    oil = Oil(ro_w=d_of_v['ro_w'],
              ro_0=d_of_v['ro_0'],
              mu=d_of_v['mu'],
              g=d_of_v['g'],
              kin_vis_w=d_of_v['kin_vis_w'],
              kin_vis_0=d_of_v['kin_vis_0'],
              v0=d_of_v['v_0'],
              p_a=d_of_v['p_a'],
              W_x=d_of_v['W_x'],
              W_y=d_of_v['W_y'],
              horseshoe=d_of_v['horseshoe'],
              fi=d_of_v['fi'], u_w=d_of_v['u_w'],
              v_w=d_of_v['v_w'], scale=d_of_v['scale'],
              C_d=d_of_v['C_d'],
              max_t=d_of_v['time'])

    while True:
        screen.fill(color.ICE_BLUE)

        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                pg.quit()
                sys.exit()

        # oil.run(pg.time.get_ticks())
        oil.draw(screen, pg.time.get_ticks())
        text_time = pg.font.SysFont('arial', 40).render(f"t = {oil.time // 10 /10} h", 2, (0, 0, 0))
        # if oil.time // 100 > d_of_v['time']:
        #     exit()
        text_r = pg.font.SysFont('arial', 40).render(f"L = {round(oil.l * oil.scale / 10 / 1000, 3)} km", 2, (0, 0, 0))
        text_s = pg.font.SysFont('arial', 40).render(f"S = {round(oil.square / 100000000, 2)} km^2", 2, (0, 0, 0))
        # text_h = pg.font.SysFont('arial', 40).render(f"H = {round(oil.get_h() * 1000, 1)} * 10^5 M", 2, (0, 0, 0))
        text_scale = pg.font.SysFont('arial', 40).render(f'1:{int(oil.scale)}', 2, color.YELLOW)
        
        pg.draw.rect(screen, color.PANEL, (cfg.WIDTH - 350, cfg.HEIGHT - 200, cfg.WIDTH, cfg.HEIGHT))
        with open('result.txt', 'w') as file_op:
            file_op.write(f'L={round(oil.l * oil.scale / 10 / 1000, 3)}\nt={oil.time // 100}\nS={round(oil.square / 100000000, 2)}')
        screen.blit(text_time, (cfg.WIDTH - 300, 550))
        
        screen.blit(text_r, (cfg.WIDTH - 300, 600))
        screen.blit(text_s, (cfg.WIDTH - 300, 650))
        # screen.blit(text_h, (cfg.WIDTH - 300, 650))
        screen.blit(text_scale, (0, 0))

        pg.display.flip()
        fpsClock.tick(cfg.FPS)
