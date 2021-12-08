import random
import json
import os

import game_framework
from pico2d import *
import game_world
import main_state

from klrby import *
from monster import *
from bossland import *
from boss import *

name = "Bossstate"
image = None
logo_time = 0.0
klrby = None
boss_terrain = None
boss = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_attack(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_attack()
    left_b, bottom_b, right_b, top_b = b.get_bb_attack()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_jump(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_jump()
    left_b, bottom_b, right_b, top_b = b.get_bb_jump()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_hammer(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_hammer()
    left_b, bottom_b, right_b, top_b = b.get_bb_hammer()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_fire(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_fire()
    left_b, bottom_b, right_b, top_b = b.get_bb_fire()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    global image
    global klrby
    klrby = Klrby()
    game_world.add_object(klrby, 1)
    klrby.x,klrby.y = 100,50
    klrby.dir = 1
    klrby.velocity = 0
    klrby.swallow_change = 1
    global boss_terrain
    boss_terrain = Bossland()
    game_world.add_object(boss_terrain, 0)

    global boss
    boss = Boss()
    game_world.add_object(boss,1)
    image = load_image('boss_background.png')

def exit():
    global image
    del(image)
    game_world.clear()
    pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if collide(klrby,boss_terrain):
        klrby.fallstop()

    if collide_attack(klrby,boss):
        boss.get_damaged()

    if collide_jump(klrby,boss):
        klrby.dead()

    if collide_hammer(klrby,boss):
        klrby.dead()

    if collide_fire(klrby,boss):
        klrby.dead()

def draw():
    global image
    clear_canvas()
    image.draw(800,400)
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    pass




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            klrby.handle_event(event)


def pause(): pass


def resume(): pass



