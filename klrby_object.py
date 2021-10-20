from pico2d import *


# constant
KLRBYx = 75
KLRBYy = 75
running = True
collide = False

class Terrian:
    global KLRBYy
    global KLRBYx
    global collide

    def __init__(self):
        self.x1, self.x2, self.y1, self.y2 = -133, 0, 25, 0
        self.image = load_image('klrby_terrain.png')

    def draw(self):
        self.image.draw(self.x1, self.y1, 266, 51)

    def check_collide(self):
        if self.x1 < KLRBYx - 25 and KLRBYx + 25 < self.x2 and self.y1 < KLRBYy - 25 and KLRBYy + 25 < self.y2:
            collide = True

class Map:
    def __init__(self):
        self.image = load_image('klrby_background.png')

    def draw(self):
        self.image.draw(400,300,800,600)

class Klrby:
    global KLRBYx
    global KLRBYy

    def __init__(self):
        self.x, self.y = KLRBYx, KLRBYy
        self.frame = 0
        self.image = load_image('klrby_walk_animation.png')
        self.count = 0
        self.dir = 0
        self.lastdir = 1
        self.gravity = 9.8
        self.acc = 0
        self.jumpcount = 0

    def update(self):
        if self.count % 5 == 0:
            self.frame = (self.frame + 1) % 10

        self.count += 1

        if self.dir == 1:
            self.x += 5
        elif self.dir == 2:
            self.x -= 5
        if self.jumpcount == True:
            if 0 < self.acc <= 20:
                self.y += 20 - self.acc
                if self.x > 500 and 240 < self.y < 250:
                    self.y = 250
                    self.acc = 0
                    self.jumpcount = False
            elif 20 < self.acc < 40:
                self.y -= 40 - self.acc
            elif self.acc == 40:
                self.jumpcount = False
                self.acc = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(0 + self.frame * 30, 0, 30, 23, self.x, self.y,50,50)
        elif self.dir == 2:
            self.image.clip_draw(0 + self.frame * 30, 24, 30, 23, self.x, self.y,50,50)
        elif self.dir == 0:
            if self.lastdir == 1:
                self.image.clip_draw(60, 0, 30, 24, self.x, self.y,50,50)
            elif self.lastdir == 2:
                self.image.clip_draw(210, 24, 30, 24, self.x, self.y,50,50)


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            klrby.dir = 1
            klrby.lastdir = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            klrby.dir = 2
            klrby.lastdir = 2
        elif event.type == SDL_KEYUP and ( event.key == SDLK_RIGHT or event.key == SDLK_LEFT ):
            klrby.dir = 0
        if event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            klrby.jumpcount = True

open_canvas(800,600)
klrby = Klrby()
map = Map()
terrians1 = Terrian()
terrians2 = Terrian()
terrians3 = Terrian()
terrians4 = Terrian()
terrians5 = Terrian()

while (running):
    handle_events()
    if klrby.jumpcount == True:
        if klrby.acc < 40:
            klrby.acc += 1

    clear_canvas()
    map.draw()
    klrby.draw()
    terrians1.x1 = 133
    terrians2.x1 = 399
    terrians3.x1 = 665
    terrians4.x1 = 800
    terrians5.x1 = 670
    terrians5.y1 = 200
    terrians1.draw()
    terrians2.draw()
    terrians3.draw()
    terrians4.draw()
    terrians5.draw()
    klrby.update()

    update_canvas()

    delay(0.01)
