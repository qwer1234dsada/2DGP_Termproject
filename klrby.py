import game_framework
from pico2d import *
import dead_state
import Camera
from monster import Monster
import game_world

# klrby Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# klrby Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

global Camera_movex
Camera_movex = 0
global klrby_attack_state
klrby_attack_state = 0
global enter_bossroom
enter_bossroom = 0
# klrby Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, E_DOWN, R_DOWN, MOUSE_ATTACK, F_DOWN = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_e): E_DOWN,
    (SDL_KEYDOWN, SDLK_r): R_DOWN,
    (SDL_KEYDOWN, SDLK_f): F_DOWN,
    (SDL_KEYDOWN, SDLK_q): MOUSE_ATTACK,
}

# klrby States
global global_klrby_x
global_klrby_x = 0

global global_klrby_y
global_klrby_y = 0

class IdleState:

    def enter(klrby, event):
        if event == RIGHT_DOWN:
            klrby.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            klrby.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            klrby.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            klrby.velocity += RUN_SPEED_PPS

    def exit(klrby, event):
        if event == SPACE:
            print("________________jump : %d" % klrby.jump)
            klrby.jump = 1
        if event == E_DOWN:
            klrby.swallow_on = 1
        if klrby.swallow_fool == 1:
            if event == R_DOWN:
                klrby.swallow_change = 1
        if klrby.swallow_change == 1:
            if event == MOUSE_ATTACK:
                klrby.attack_on = 1
        if event == F_DOWN:
            klrby.enter_check = 1

    def do(klrby):
        klrby.frame = (klrby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if klrby.swallow_on == 1:
            klrby.swallow_timer -= 1
            if klrby.swallow_timer == 0:
                klrby.swallow_on = 0
                klrby.swallow_timer = 1000

    def draw(klrby):
        if klrby.swallow_change == 0:
            if klrby.swallow_on == 0:
                if klrby.dir == 1:
                    klrby.image.clip_draw(60, 0, 30, 23, klrby.x, klrby.y,50,50)
                else:
                    klrby.image.clip_draw(210, 24, 30, 23, klrby.x, klrby.y,50,50)
            elif klrby.swallow_on == 1:
                if klrby.dir == 1:
                    klrby.image2.clip_draw(int(klrby.frame) * 30, 0, 30, 23, klrby.x, klrby.y,50,50)
                else:
                    klrby.image2.clip_draw(int(klrby.frame) * 30, 24, 30, 23, klrby.x, klrby.y,50,50)
        elif klrby.swallow_change == 1:
            if klrby.attack_on == 0:
                if klrby.dir == 1:
                    klrby.image3.clip_composite_draw(60, 0, 30, 40, 3.14, 'v',klrby.x, klrby.y + 10, 50, 70)
                else:
                    klrby.image3.clip_draw(210, 0, 30, 40, klrby.x, klrby.y + 10, 50, 70)
            elif klrby.attack_on == 1:
                if klrby.dir == 1:
                    if 0 <= klrby.frame < 4:
                        klrby.image5.clip_composite_draw(0, 0, 80, 60, 3.14, 'v',klrby.x + 10, klrby.y , 100, 85)
                    elif 4 <= klrby.frame < 7:
                        klrby.image6.clip_composite_draw(0, 0, 80, 60, 3.14, 'v',klrby.x + 10, klrby.y , 100, 85)
                    else:
                        klrby.image7.clip_composite_draw(0, 0, 80, 60, 3.14, 'v',klrby.x + 10, klrby.y , 100, 85)
                else:
                    if 0 <= klrby.frame < 4:
                        klrby.image5.clip_draw(0, 0, 80, 60, klrby.x - 10, klrby.y , 100, 85)
                    elif 4 <= klrby.frame < 7:
                        klrby.image6.clip_draw(0, 0, 80, 60, klrby.x - 10, klrby.y , 100, 85)
                    else:
                        klrby.image7.clip_draw(0, 0, 80, 60, klrby.x - 10, klrby.y , 100, 85)
                klrby.count += 1
                if klrby.count == 200:
                    klrby.attack_on = 0
                    klrby.count = 0

        print("______________colidedir : %d" % klrby.colide)
        print("dir : %d" % klrby.dir)
        print("++++++++++++++++++++++++++++%d"%klrby.attack_on)


class RunState:

    def enter(klrby, event):
        if event == RIGHT_DOWN:
            klrby.velocity += RUN_SPEED_PPS
            klrby.dir = 1
        elif event == LEFT_DOWN:
            klrby.velocity -= RUN_SPEED_PPS
            klrby.dir = -1
        elif event == RIGHT_UP:
            klrby.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            klrby.velocity += RUN_SPEED_PPS

        if klrby.velocity > 0:
            klrby.dir = 1
        elif klrby.velocity < 0:
            klrby.dir = -1

    def exit(klrby, event):
        if event == SPACE:
            print("________________jump : %d" % klrby.jump)
            klrby.jump = 1
        if event == E_DOWN:
            klrby.swallow_on = 1
        if klrby.swallow_fool == 1:
            if event == R_DOWN:
                klrby.swallow_change = 1
        if klrby.swallow_change == 1:
            if event == MOUSE_ATTACK:
                klrby.attack_on = 1
        if event == F_DOWN:
            klrby.enter_check = 1
        else:
            klrby.enter_check = 0


    def do(klrby):
        global Camera_movex
        global klrby_attack_state
        klrby_attack_state = klrby.attack_on
        klrby.frame = (klrby.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if klrby.colide == 0:
            Camera_movex += klrby.velocity * game_framework.frame_time
        if 0 > Camera_movex or 800 < Camera_movex :
            if klrby.colide == 0:
                klrby.x += klrby.velocity * game_framework.frame_time

        if klrby.swallow_on == 1:
            klrby.swallow_timer -= 1
            if klrby.swallow_timer == 0:
                klrby.swallow_on = 0
                klrby.swallow_timer = 1000

        if klrby.swallow_change == 1:
            klrby.swallow_fool = 0

        klrby.x = clamp(25, klrby.x, 1600 - 25)

    def draw(klrby):
        print("colide : %d" %klrby.colide)
        if klrby.swallow_change == 0:
            if klrby.swallow_on == 0:
                if klrby.dir == 1:
                    klrby.image.clip_draw(int(klrby.frame) * 30, 0, 30, 23, klrby.x, klrby.y,50,50)
                else:
                    klrby.image.clip_draw(int(klrby.frame) * 30, 24, 30, 23, klrby.x, klrby.y,50,50)
            elif klrby.swallow_on == 1:
                if klrby.dir == 1:
                    klrby.image2.clip_draw(int(klrby.frame) * 30, 0, 30, 23, klrby.x, klrby.y,50,50)
                else:
                    klrby.image2.clip_draw(int(klrby.frame) * 30, 24, 30, 23, klrby.x, klrby.y,50,50)
        elif klrby.swallow_change == 1:
            if klrby.attack_on == 0:
                if klrby.dir == 1:
                    klrby.image3.clip_composite_draw(int(klrby.frame) * 30, 0, 30, 40, 3.14, 'v',klrby.x, klrby.y + 10, 50, 70)
                else:
                    klrby.image3.clip_draw(int(klrby.frame) * 30, 0, 30, 40, klrby.x, klrby.y + 10, 50, 70)
            elif klrby.attack_on == 1:
                if klrby.dir == 1:
                    if 0 <= klrby.frame < 4:
                        klrby.image5.clip_composite_draw(0, 0, 80, 60, 3.14, 'v',klrby.x + 10, klrby.y , 100, 85)
                    elif 4 <= klrby.frame < 7:
                        klrby.image6.clip_composite_draw(0, 0, 80, 60, 3.14, 'v',klrby.x + 10, klrby.y , 100, 85)
                    else:
                        klrby.image7.clip_composite_draw(0, 0, 80, 60, 3.14, 'v',klrby.x + 10, klrby.y , 100, 85)
                else:
                    if 0 <= klrby.frame < 4:
                        klrby.image5.clip_draw(0, 0, 80, 60, klrby.x - 10, klrby.y , 100, 85)
                    elif 4 <= klrby.frame < 7:
                        klrby.image6.clip_draw(0, 0, 80, 60, klrby.x - 10, klrby.y , 100, 85)
                    else:
                        klrby.image7.clip_draw(0, 0, 80, 60, klrby.x - 10, klrby.y , 100, 85)
                klrby.count += 1
                if klrby.count == 200:
                    klrby.attack_on = 0
                    klrby.count = 0

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState, E_DOWN: IdleState, R_DOWN: IdleState, MOUSE_ATTACK:IdleState, F_DOWN: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState, E_DOWN: RunState, R_DOWN: RunState, MOUSE_ATTACK:RunState, F_DOWN: RunState},
}

class Klrby:

    def __init__(self):
        self.x, self.y = 1600 // 2, 110
        self.image = load_image('klrby_walk_animation.png')
        self.image2 = load_image('klrby_swallow_animation.png')
        self.image3 = load_image('klrby_sword_animation.png')
        self.image4 = load_image('klrby_sword_attack_animation.png')
        self.image5 = load_image('klrby_sword_attack_animation0.png')
        self.image6 = load_image('klrby_sword_attack_animation1.png')
        self.image7 = load_image('klrby_sword_attack_animation2.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.colide = 0
        self.gravity = 0.5
        self.jump = 0
        self.jump_timer = 1000
        self.swallow_on = 0
        self.swallow_timer = 1000
        self.swallow_fool = 0
        self.swallow_change = 0
        self.attack_on = 0
        self.count = 0
        self.enter_check = 0
        self.sword_sound = load_wav('sword_sound.wav')
        self.sword_sound.set_volume(64)


    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 15

    def get_bb_dead(self):
        if (self.swallow_on == 1 or self.swallow_on == 1):
            return 0,0,0,0
        else:
            return self.x - 20, self.y - 25, self.x + 20, self.y + 15

    def get_bb_block(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 15

    def get_bb_another(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 15

    def get_bb_jump(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 15

    def get_bb_hammer(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 15

    def get_bb_fire(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 15

    def get_bb_swallow(self):
        if self.swallow_on == 1:
            if self.dir == 1:
                return self.x - 20, self.y - 30, self.x + 100, self.y + 30
            elif self.dir == -1:
                return self.x - 100, self.y - 30, self.x + 20, self.y + 30
        else:
            return 0,0,0,0

    def get_bb_swallow_finish(self):
        if self.swallow_on == 1:
            return self.x - 20, self.y - 25, self.x + 20, self.y + 15
        else:
            return 0,0,0,0

    def get_bb_attack(self):
        if self.attack_on == 1:
            if self.dir == 1:
                return self.x - 20, self.y - 30, self.x + 100, self.y + 30
            elif self.dir == -1:
                return self.x - 100, self.y - 30, self.x + 20, self.y + 30
        else:
            return 0,0,0,0

    def get_bb_move_bossstage(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 15

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if self.jump == 0 and self.jump_timer == 1000:
            self.y -= self.gravity
        if self.jump == 1:
            self.y += 1
            self.jump_timer -= 5
            if self.jump_timer == 0:
                self.jump_timer = 1000
                self.jump = 0

        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        global global_klrby_x
        global global_klrby_y
        global enter_bossroom
        enter_bossroom = self.enter_check
        global_klrby_x = self.x
        global_klrby_y = self.y

        if self.attack_on == 1:
            self.sword_sound.play()


    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_block())
        draw_rectangle(*self.get_bb_swallow())
        draw_rectangle(*self.get_bb_swallow_finish())
        draw_rectangle(*self.get_bb_attack())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def fallstop(self):
        if self.jump == 0:
            self.y += self.gravity

    def stop(self):
        if self.dir == 1 and self.colide != -1:
            self.colide = 1
        elif self.dir == -1 and self.colide != 1:
            self.colide = -1

        print("dir : %d" %self.dir)

        if self.colide == 1:
            if self.dir == -1 or self.jump == 1:
                self.colide = 0
        elif self.colide == -1:
            if self.dir == 1 or self.jump == 1:
                self.colide = 0

        print("______________colidedir : %d" %self.colide)

    def swallow_finish(self):
        self.swallow_fool = 1

    def dead(self):
        game_framework.change_state(dead_state)