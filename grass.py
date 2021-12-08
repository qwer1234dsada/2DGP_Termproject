from pico2d import *

import klrby
import game_framework
import boss_state
from klrby import Camera_movex
colidetype = 0

class Grass:

    def __init__(self, x = 500, y = 500):
        self.image = load_image('klrby_background.png')
        self.x, self.y = x, y
        self.bgm = load_music('bgm_music.wav')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        global colidetype

        print("camera in grass : %d" %klrby.Camera_movex)
        if 0 > klrby.Camera_movex:
            self.image.clip_draw(0, 0, 800, 400, 800, 400, 1600, 800)
        elif 800 < klrby.Camera_movex:
            self.image.clip_draw(800, 0, 800, 400, 800, 400, 1600, 800)
        else:
            self.image.clip_draw(0 + int(klrby.Camera_movex), 0, 800, 400, 800, 400, 1600, 800)

        draw_rectangle(*self.get_bb_another())
        draw_rectangle(*self.get_bb_block())
        draw_rectangle(*self.get_bb())

    #바닥 벽이랑 따로
    def get_bb(self):
        if -800 < klrby.Camera_movex < -420:
            return 0,50,365,62
        elif -30 < klrby.Camera_movex < 266:
            return 790,50,850,80
        elif 301 < klrby.Camera_movex < 320:
            return 780,50,820,110
        elif 770 < klrby.Camera_movex < 791:
            return 780,50,820,160
        elif 890 < klrby.Camera_movex < 910:
            return 880,50,910,160
        elif 1486 < klrby.Camera_movex < 1600:
            return 1486,50,1600,120
        else:
            return 10,10,10,10

    def get_bb_block(self):
        if -460 < klrby.Camera_movex < -410:
            return 360,50,370,70
        elif -360 < klrby.Camera_movex < -350:
            return 428,50,440,70
        elif -32 < klrby.Camera_movex < -10:
            return 790,50,800,70
        elif 37 < klrby.Camera_movex < 50:
            return 790,50,830,120
        elif 80 < klrby.Camera_movex < 87:
            return 770,50,800,120
        elif 265 < klrby.Camera_movex < 280:
            return 780,50,820,140
        elif 301 < klrby.Camera_movex < 303:
            return 780,50,790,140
        elif 765 < klrby.Camera_movex < 775:
            return 790,50,800,140
        else:
            return 10,10,10,10

    def get_bb_another(self):
        if -460 < klrby.Camera_movex < -353:
            return 360,50,450,80
        elif -360 < klrby.Camera_movex < -20:
            return 410,50,800,60
        elif 40 < klrby.Camera_movex < 87:
            return 790, 50, 850, 130
        elif 267 < klrby.Camera_movex < 300:
            return 780,50,820,150
        elif 321 < klrby.Camera_movex < 780:
            return 780,50,820,80
        elif 790 < klrby.Camera_movex < 889:
            return 780,50,880,100
        elif 921 < klrby.Camera_movex < 1500:
            return 921,50,1500,80
        else:
            return 10,10,10,10

    def get_bb_move_bossstage(self):
        if 1529 < klrby.Camera_movex < 1570:
            return 1529,50,1570,200
        else:
            return 999,999,999,999

    def move_to_boss_stage(self):
        if klrby.enter_bossroom == 1:
            game_framework.change_state(boss_state)
            self.bgm.stop()
