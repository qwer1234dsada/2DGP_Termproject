from pico2d import *

import klrby
import game_framework

class Bossland:

    def __init__(self, x = 0, y = 0):
        self.image = load_image('klrby_terrain.png')
        self.x, self.y = x, y

    def get_bb(self):
        return 0,0,1600,20

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 800, 400, 800, 0, 1600, 40)
