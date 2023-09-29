import random
import math
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

hand = load_image('hand_arrow.png')

boy_x, boy_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
destination_list = []
clicking = False

frame = 0
direction = 1

def handle_events():
    global destination_list, clicking, direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            destination_x, destination_y = event.x, TUK_HEIGHT - event.y
            destination_list.append((destination_x, destination_y))
            clicking = True
            if destination_x < boy_x:
                direction = -1
            else:
                direction = 1

def move_to_destination(destination):
    global boy_x, boy_y, clicking, frame
    distance = math.sqrt((destination[0] - boy_x) ** 2 + (destination[1] - boy_y) ** 2)
    speed = 5
    if distance > speed:
        angle = math.atan2(destination[1] - boy_y, destination[0] - boy_x)
        boy_x += speed * math.cos(angle)
        boy_y += speed * math.sin(angle)
        frame = (frame + 1) % 8
    else:
        boy_x, boy_y = destination[0], destination[1]
        destination_list.pop(0)
        if len(destination_list) == 0:
            clicking = False

while True:
    clear_canvas()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if clicking:
        hand.draw(destination_list[0][0], destination_list[0][1])

    if clicking:
        if direction == 1:
            character.clip_draw(frame * 100, 100, 100, 100, boy_x, boy_y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, boy_x, boy_y)
    else:
        if direction == 1:
            character.clip_draw(0, 100, 100, 100, boy_x, boy_y)
        else:
            character.clip_draw(0, 0, 100, 100, boy_x, boy_y)

    if clicking:
        move_to_destination(destination_list[0])

    update_canvas()

    handle_events()
    delay(0.02)





