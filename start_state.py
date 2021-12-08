import game_framework
from pico2d import *
import main_state

name = "StartState"
image = None
image2 = None
logo_time = 0.0


def enter():
    global image
    global image2
    image = load_image('klrbylogo.png')
    image2 = load_image('klrby_background.png')
    pass


def exit():
    global image
    global image2
    del(image)
    del(image2)
    pass


def update():
    global logo_time

    if ( logo_time > 1.0 ):
        logo_time = 0
        game_framework.change_state(main_state)
    delay(0.01)
    logo_time+= 0.01
    pass


def draw():
    global image
    global image2
    clear_canvas()
    image2.draw(800,400)
    image.draw(800,400)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




