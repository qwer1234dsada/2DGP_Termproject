import random
from pico2d import *
import klrby
import game_world
import game_framework
import end_state
global output_dead_timer
output_dead_timer = 0

class Boss:
    image = None
    image2 = None
    image3 = None
    image4 = None
    image5 = None
    image6 = None

    def __init__(self):
        if Boss.image == None:
            Boss.image = load_image('boss_stand_image.png')
            Boss.image2 = load_image('boss_fireball_image.png')
            Boss.image3 = load_image('boss_jump_image.png')
            Boss.image4 = load_image('boss_attack_image.png')
            Boss.image5 = load_image('boss_dead_image.png')
            Boss.image6 = load_image('fire_effect.png')
        self.x, self.y = 1200, 50
        self.random_skill = 0
        self.hp = 1000
        self.skill_delay = 0
        self.frame = 0
        self.frame_timer = 0
        self.random_timer = 0
        self.jump_count = 0
        self.paturn_delay = 0
        self.get_damaged_delay = 0
        self.dead_animation = 0
        self.boss_bgm = load_wav('boss_bgm.wav')
        self.boss_bgm.set_volume(64)
        self.boss_bgm.repeat_play()

    def draw(self):
        if self.hp >= 0:
            if self.random_skill == 0:
                self.image.clip_draw(112 * self.frame, 0, 100, 100, self.x, self.y, 300, 300)
            elif self.random_skill == 1:
                self.image6.clip_draw(0, -20, 1000, 1800, self.x - 800, self.y + 100, 1600, 300)
                self.image2.clip_draw(112 * self.frame, -20, 120, 120, self.x, self.y + 100, 300, 300)
            elif self.random_skill == 2:
                self.image3.clip_draw(112 * self.frame, 0, 100, 100, self.x, self.y, 300, 300)
            elif self.random_skill == 3:
                self.image4.clip_draw(112 * self.frame, 0, 100, 150, self.x, self.y + 100, 300, 300)
        else:
            self.image5.clip_draw(0, 0, 100, 100, self.x, self.y - self.dead_animation, 300, 300)

        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_jump())
        draw_rectangle(*self.get_bb_hammer())
        draw_rectangle(*self.get_bb_fire())

    def update(self):
        global output_dead_timer
        if self.get_damaged_delay == -1:
            self.get_damaged_delay = 100

        if self.get_damaged_delay > 0:
            self.get_damaged_delay -= 1

        self.frame_timer += 0.01

        if self.frame_timer > 1:
            self.frame += 1
            self.frame_timer = 0

        if self.random_skill == 0 or self.random_skill == 1:
            if self.frame == 4:
                self.frame = 0
                if self.random_skill == 1:
                    self.random_skill = 0
        elif self.random_skill == 2:
            if self.frame == 6:
                self.frame = 0
            if self.jump_count >= 400:
                self.random_skill = 0
        elif self.random_skill == 3:
            if self.frame == 6:
                self.frame = 0
                self.random_skill = 0
        self.random_timer += 1

        if self.hp > 1:
            if self.random_timer == 5000:
                print("ㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊㅊ")
                self.random_skill = random.randint(1,3)
                self.random_timer = 0

        if self.random_skill == 2:
            if self.jump_count <= 200:
                self.y += 1
            elif 200 < self.jump_count < 400:
                self.y -= 1

            self.jump_count += 1
            if self.jump_count > 400:
                self.jump_count = 0
        print("_______________________________________ %d" %self.jump_count)

        if self.hp < 1:
            self.dead_animation += 0.09

        if self.dead_animation > 300:
            game_framework.change_state(end_state)

        output_dead_timer = self.dead_animation

    def get_dead(self):
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def get_bb_hammer(self):
        if self.random_skill == 3:
            if self.frame == 3:
                return self.x - 300, self.y - 50, self.x + 200, self.y + 100
            else:
                return 0, 1000, 0, 1000
        else:
            return 0,1000,0,1000

    def get_bb_jump(self):
        if self.random_skill == 2:
            if self.jump_count > 300:
                return 0, 0, 1800, 40
            else:
                return 0, 1000, 0, 1000
        else:
            return 0,1000,0,1000

    def get_bb_attack(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def get_bb_fire(self):
        if self.random_skill == 1:
            return self.x - 1800, self.y + 100, self.x, self.y + 200
        else:
            return 0,1000,0,1000

    def get_damaged(self):
        if self.get_damaged_delay == 0:
            self.hp -= 50
            self.get_damaged_delay -= 1