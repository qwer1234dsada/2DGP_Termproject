import game_framework
from pico2d import *


name = "EndState"
image = None
image2 = None
logo_time = 0.0
y = 0

def enter():
    global image
    global image2
    image = load_image('kirby_background.png')
    image2 = load_image('The_End.png')
    pass


def exit():
    global image
    global image2
    del(image)
    del(image2)
    pass


def update():
    global logo_time
    global y
    if ( logo_time > 1.0):
        logo_time = 0
        game_framework.quit()
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(800,400)
    image2.draw(800,400)
    update_canvas()




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




