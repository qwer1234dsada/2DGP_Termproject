import random
from pico2d import *
import klrby
import game_world
import game_framework

class Monster2:
    image = None

    def __init__(self):
        if Monster2.image == None:
            Monster2.image = load_image('fire.png')
        self.x, self.y = 1800, 110
        self.movecount = 1300
        self.moveflag = 0
        self.swallow_suck = 0
        self.trun_amount = 0
        self.move_amount = 0
        self.swallow_finish_type = 0
        self.type = 0
        self.timer = 0

    def get_bb(self):
        if klrby.global_klrby_x < self.x- ( klrby.Camera_movex):
            if klrby.Camera_movex < 0 or klrby.Camera_movex > 800:
                return self.x - 20- self.move_amount, self.y - 25, self.x + 20- self.move_amount, self.y + 15
            else:
                return self.x - 20 - ( klrby.Camera_movex * 2)- self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 )- self.move_amount, self.y + 15
        elif klrby.global_klrby_x > self.x- ( klrby.Camera_movex):
            if klrby.Camera_movex < 0 or klrby.Camera_movex > 800:
                return self.x - 20 + self.move_amount, self.y - 25, self.x + 20 + self.move_amount, self.y + 15
            else:
                return self.x - 20 - ( klrby.Camera_movex * 2 ) + self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 ) + self.move_amount, self.y + 15

    def get_bb_attack(self):
        if klrby.global_klrby_x < self.x- ( klrby.Camera_movex):
            if klrby.Camera_movex < 0 or klrby.Camera_movex > 800:
                return self.x - 20- self.move_amount, self.y - 25, self.x + 20- self.move_amount, self.y + 15
            else:
                return self.x - 20 - ( klrby.Camera_movex * 2)- self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 )- self.move_amount, self.y + 15
        elif klrby.global_klrby_x > self.x- ( klrby.Camera_movex):
            if klrby.Camera_movex < 0 or klrby.Camera_movex > 800:
                return self.x - 20 + self.move_amount, self.y - 25, self.x + 20 + self.move_amount, self.y + 15
            else:
                return self.x - 20 - ( klrby.Camera_movex * 2 ) + self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 ) + self.move_amount, self.y + 15

    def get_bb_dead(self):
        if self.swallow_finish_type == 1 or self.swallow_suck == 1:
            return 10000,10000,10000,10000
        else:
            if klrby.global_klrby_x < self.x- ( klrby.Camera_movex):
                if klrby.Camera_movex < 0 or klrby.Camera_movex > 800:
                    return self.x - 20- self.move_amount, self.y - 25, self.x + 20- self.move_amount, self.y + 15
                else:
                    return self.x - 20 - ( klrby.Camera_movex * 2)- self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 )- self.move_amount, self.y + 15
            elif klrby.global_klrby_x > self.x- ( klrby.Camera_movex):
                if klrby.Camera_movex < 0 or klrby.Camera_movex > 800:
                    return self.x - 20 + self.move_amount, self.y - 25, self.x + 20 + self.move_amount, self.y + 15
                else:
                    return self.x - 20 - ( klrby.Camera_movex * 2 ) + self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 ) + self.move_amount, self.y + 15

    def get_bb_swallow(self):
        if klrby.global_klrby_x < self.x- ( klrby.Camera_movex):
            if klrby.Camera_movex < 0 or klrby.Camera_movex > 800:
                return self.x - 20 - self.move_amount, self.y - 25, self.x + 20 - self.move_amount, self.y + 15
            else:
                return self.x - 20 - ( klrby.Camera_movex * 2 ) - self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 ) - self.move_amount, self.y + 15
        elif klrby.global_klrby_x > self.x- ( klrby.Camera_movex):
            if klrby.Camera_movex < 0 or klrby.Camera_movex > 800:
                return self.x - 20 + self.move_amount, self.y - 25, self.x + 20 + self.move_amount, self.y + 15
            else:
                return self.x - 20 - ( klrby.Camera_movex * 2 ) + self.move_amount, self.y - 25, self.x + 20 + ( klrby.Camera_movex * 2 ) + self.move_amount, self.y + 15

    def get_bb_swallow_finish(self):
        if klrby.global_klrby_x < self.x - ( klrby.Camera_movex):
            if klrby.Camera_movex < 0 or klrby.Camera_movex > 800:
                return self.x - 20- self.move_amount, self.y - 25, self.x + 20- self.move_amount, self.y + 15
            else:
                return self.x - 20 - ( klrby.Camera_movex * 2 )- self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 )- self.move_amount, self.y + 15
        elif klrby.global_klrby_x > self.x - ( klrby.Camera_movex):
            if klrby.Camera_movex < 0 or klrby.Camera_movex > 800:
                return self.x - 20 + self.move_amount, self.y - 25, self.x + 20 + self.move_amount, self.y + 15
            else:
                return self.x - 20 - ( klrby.Camera_movex * 2 ) + self.move_amount, self.y - 25, self.x + 20 - ( klrby.Camera_movex * 2 ) + self.move_amount, self.y + 15

    def draw(self):
        if self.type == 0:
            if self.swallow_finish_type == 0:
                if self.moveflag == 0:
                    if klrby.Camera_movex > 0 and klrby.Camera_movex < 800:
                        self.image.clip_draw(0, 0, 30, 24, self.x - ( klrby.Camera_movex * 2 ), self.y, 50, 50)
                    else:
                        self.image.clip_draw(0, 0, 30, 24, self.x, self.y, 50, 50)
                elif self.moveflag == 1:
                    if klrby.Camera_movex > 0 and klrby.Camera_movex < 800:
                        self.image.clip_composite_draw(0, 0, 30, 24, -3.14, 'v', self.x - ( klrby.Camera_movex * 2 ), self.y, 50, 50)
                    else:
                        self.image.clip_composite_draw(0, 0, 30, 24, -3.14, 'v', self.x, self.y, 50, 50)

                if self.swallow_suck == 1:
                    self.moveflag = 3
                    if klrby.global_klrby_x < self.x- ( klrby.Camera_movex*2):
                        if klrby.Camera_movex > 0 and klrby.Camera_movex < 800:
                            self.image.clip_composite_draw(0, 0, 30, 24, self.trun_amount, '', self.x - ( klrby.Camera_movex * 2 ) - self.move_amount, self.y, 50, 50)
                        else:
                            self.image.clip_composite_draw(0, 0, 30, 24,  self.trun_amount, '', self.x - self.move_amount, self.y, 50, 50)
                    elif klrby.global_klrby_x > self.x - ( klrby.Camera_movex*2):
                        if klrby.Camera_movex > 0 and klrby.Camera_movex < 800:
                            self.image.clip_composite_draw(0, 0, 30, 24, self.trun_amount, '',self.x - (klrby.Camera_movex * 2) + self.move_amount, self.y, 50, 50)
                        else:
                            self.image.clip_composite_draw(0, 0, 30, 24, self.trun_amount, '', self.x + self.move_amount, self.y, 50, 50)

                    self.trun_amount += 0.1
                    self.move_amount += 0.1

        else:
            pass

    def update(self):
        if self.moveflag == 0:
            self.x -= 0.2
            self.movecount -= 1
        elif self.moveflag == 1:
            self.x += 0.2
            self.movecount += 1

        if self.movecount == 1300:
            self.moveflag = 0

        if self.movecount == 0:
            self.moveflag = 1

    def swallow(self):
        self.swallow_suck = 1

    def swallow_finish(self):
        self.swallow_finish_type = 1

    def get_dead(self):
        self.x = 0
        self.y = 1000

