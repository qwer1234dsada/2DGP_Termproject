import random
import json
import os

from pico2d import *
import game_framework
import game_world
import grass

from klrby import *
from grass import *
from monster import *

name = "MainState"

klrby = None
grasses = None
monsteres = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_block(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_block()
    left_b, bottom_b, right_b, top_b = b.get_bb_block()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_another(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_another()
    left_b, bottom_b, right_b, top_b = b.get_bb_another()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_swallow(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_swallow()
    left_b, bottom_b, right_b, top_b = b.get_bb_swallow()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collide_swallow_finish(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb_swallow_finish()
    left_b, bottom_b, right_b, top_b = b.get_bb_swallow_finish()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    global klrby
    klrby = Klrby()
    game_world.add_object(klrby, 1)

    global grasses
    grasses = Grass()
    game_world.add_object(grasses, 0)

    global monsteres
    monsteres = Monster()
    game_world.add_object(monsteres, 1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
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


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if collide(klrby,grasses):
        klrby.fallstop()

    if collide_block(klrby,grasses):
        klrby.stop()

    if collide_another(klrby,grasses):
        klrby.fallstop()

    if collide_swallow(klrby,monsteres):
        monsteres.swallow()

    if collide_swallow_finish(klrby,monsteres):
        monsteres.swallow_finish()
        klrby.swallow_finish()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






