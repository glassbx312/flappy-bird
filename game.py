from pygame import *
from random import randint

init()

W, H = 1000, 650
FPS = 60
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (51, 147, 189)

window = display.set_mode((W, H))
display.set_caption("Flappy Bird")

clock = time.Clock()

def generate_pipes(
        count,
        pipe_width = 100,
        gap = 280,
        min_height = 50,
        max_height = 440,
        distance = 650):
    pipes = []
    start_x = H
    for _ in range(count):
        height = randint(min_height, max_height)
        top_pipe = Rect(start_x, 0, pipe_width, height)
        bottom_pipe = Rect(start_x, height + gap, pipe_width, H - (height + gap))
        pipes.extend([top_pipe, bottom_pipe])
        start_x += distance
    return pipes

pipes = generate_pipes(150)

player = Rect(50, 250, 100, 100)

game = True
lose = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(BLUE)

    if not lose:
        for pipe in pipes:
            pipe.x -= 10
            draw.rect(window, GREEN, pipe)
            if pipe.x <= -100:
                pipes.remove(pipe)
        draw.rect(window, YELLOW, player)


    clock.tick(FPS)
    display.update()


