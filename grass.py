from pico2d import *

import klrby
from klrby import Camera_movex
colidetype = 0

class Grass:

    def __init__(self, x = 500, y = 500):
        self.image = load_image('klrby_background.png')
        self.x, self.y = x, y

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
        else:
            return 10,10,10,10

    def get_bb_another(self):
        if -460 < klrby.Camera_movex < -353:
            return 360,50,450,80
        elif -360 < klrby.Camera_movex < -20:
            return 410,50,800,60
        elif 40 < klrby.Camera_movex < 87:
            return 790, 50, 850, 130
        else:
            return 10,10,10,10
