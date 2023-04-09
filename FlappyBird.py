import pygame
import random

pygame.init()

# set up the display
screen = pygame.display.set_mode((288, 512))
pygame.display.set_caption("Flappy Bird")

# load the images
background_image = pygame.image.load("background.png").convert()
bird_image = pygame.image.load("bird.png").convert_alpha()
pipe_image = pygame.image.load("pipe.png").convert_alpha()

# set up the clock
clock = pygame.time.Clock()

# define the game variables
bird_x = 50
bird_y = 200
bird_velocity = 0
gravity = 0.5
jump_strength = 8
pipe_gap = 150
pipe_speed = 2
pipe_interval = 1500
pipes = []

# define functions for drawing the game objects
def draw_background():
    screen.blit(background_image, (0, 0))

def draw_bird():
    screen.blit(bird_image, (bird_x, bird_y))

def draw_pipe(pipe):
    screen.blit(pipe_image, (pipe['x'], pipe['top']))
    screen.blit(pygame.transform.flip(pipe_image, False, True), (pipe['x'], pipe['bottom']))

# define a function for generating new pipes
def generate_pipes():
    top_pipe_height = random.randint(50, 250)
    bottom_pipe_height = 512 - pipe_gap - top_pipe_height
    pipes.append({'x': 288, 'top': top_pipe_height - 320, 'bottom': bottom_pipe_height + pipe_gap})

# define a function for checking if the bird collides with a pipe
def check_collision(pipe):
    if bird_x + bird_image.get_width() > pipe['x'] and bird_x < pipe['x'] + pipe_image.get_width():
        if bird_y < pipe['top'] + 320 or bird_y + bird_image.get_height() > pipe['bottom'] + 320:
            return True
    return False

# define the game loop
while True:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -jump_strength

    # update the game objects
    bird_velocity += gravity
    bird_y += bird_velocity
    if len(pipes) > 0 and pipes[0]['x'] < -pipe_image.get_width():
        pipes.pop(0)
    for pipe in pipes:
        pipe['x'] -= pipe_speed
        if check_collision(pipe):
            pygame.quit()
            quit()
    if len(pipes) == 0 or pipes[-1]['x'] < 288 - pipe_interval:
        generate_pipes()

    # draw the game objects
    draw_background()
    draw_bird()
    for pipe in pipes:
        draw_pipe(pipe)

    # update the display
    pygame.display.update()

    # set the frame rate
    clock.tick(60)
