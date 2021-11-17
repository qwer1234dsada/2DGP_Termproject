import random
from pico2d import *
import klrby
import game_world
import game_framework

class Monster:
    image = None

    def __init__(self):
        if Monster.image == None:
            Monster.image = load_image('knight.png')
        self.x, self.y = 1000, 110
        self.movecount = 1000
        self.moveflag = 0
        self.swallow_suck = 0
        self.trun_amount = 0
        self.move_amount = 0
        self.swallow_finish_type = 0

    def get_bb(self):
        if klrby.Camera_movex < 0:
            return self.x - 20- self.move_amount, self.y - 25, self.x + 20- self.move_amount, self.y + 15
        else:
            return self.x - 20 - ( klrby.Camera_movex * 2 )- self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 )- self.move_amount, self.y + 15

    def get_bb_swallow(self):
        if klrby.Camera_movex < 0:
            return self.x - 20 - self.move_amount, self.y - 25, self.x + 20 - self.move_amount, self.y + 15
        else:
            return self.x - 20 - ( klrby.Camera_movex * 2 ) - self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 ) - self.move_amount, self.y + 15

    def get_bb_swallow_finish(self):
        if klrby.Camera_movex < 0:
            return self.x - 20- self.move_amount, self.y - 25, self.x + 20- self.move_amount, self.y + 15
        else:
            return self.x - 20 - ( klrby.Camera_movex * 2 )- self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 )- self.move_amount, self.y + 15

    def draw(self):
        if self.swallow_finish_type == 0:
            if self.moveflag == 1:
                if klrby.Camera_movex > 0:
                    self.image.clip_draw(0, 0, 30, 24, self.x - ( klrby.Camera_movex * 2 ), self.y, 50, 50)
                else:
                    self.image.clip_draw(0, 0, 30, 24, self.x, self.y, 50, 50)
            elif self.moveflag == 0:
                if klrby.Camera_movex > 0:
                    self.image.clip_composite_draw(0, 0, 30, 24, -3.14, 'v', self.x - ( klrby.Camera_movex * 2 ), self.y, 50, 50)
                else:
                    self.image.clip_composite_draw(0, 0, 30, 24, -3.14, 'v', self.x, self.y, 50, 50)

            if self.swallow_suck == 1:
                self.moveflag = 3
                if klrby.Camera_movex > 0:
                    self.image.clip_composite_draw(0, 0, 30, 24, self.trun_amount, '', self.x - ( klrby.Camera_movex * 2 ) - self.move_amount, self.y, 50, 50)
                else:
                    self.image.clip_composite_draw(0, 0, 30, 24,  self.trun_amount, '', self.x - self.move_amount, self.y, 50, 50)
                self.trun_amount += 0.1
                self.move_amount += 0.1
        else:
            pass

        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_swallow_finish())

    def update(self):
        if self.moveflag == 0:
            self.x += 0.2
            self.movecount -= 1
        elif self.moveflag == 1:
            self.x -= 0.2
            self.movecount += 1

        if self.movecount == 1000:
            self.moveflag = 0

        if self.movecount == 0:
            self.moveflag = 1

        print("movecount = %d" %self.movecount)

    def swallow(self):
        self.swallow_suck = 1

    def swallow_finish(self):
        print("_________________________________________________________swallow")
        self.swallow_finish_type = 1