import random
from datetime import datetime, timedelta

import pygame
from constants import (
    GREEN,
    RED,
    WHITE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    WINDOW_HEIGHT_DRAW,
    BLOCKSIZE,
)
from snake_node import SnakeNode

pygame.init()
pygame.display.set_caption("Rofo Library Snake Game Example")
running = True
move_x = 0
move_y = 1


kaboom_image = pygame.image.load("kaboom.png")
kaboom_image = pygame.transform.scale(kaboom_image, (90, 90))
food_spots = set()
snake_head: SnakeNode = SnakeNode(10, 10)


SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
last_move = None

score = 0
# Set the size of the grid block


def draw_grid():
    """
    draws our basic grid
    """

    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT_DRAW, BLOCKSIZE):  # we want black space at
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


def add_food():
    """
    handles adding food to the array
    """
    random.seed()
    rand_x = random.randrange(19)
    random.seed()
    rand_y = random.randrange(19)
    food_spots.add((rand_x, rand_y))


def draw_text(pygame, surface):
    """
        draws text to the pygame surface

    Args:
        pygame (pygame): the pygame object
        surface (surface): the surface we are writing this text too.
    """
    font1 = pygame.font.SysFont("timenewroman.ttf", 24)
    img1 = font1.render(f"Score:{score}", True, RED)
    img2 = font1.render("Press r to Restart", True, RED)

    surface.blit(img1, (0, 400))
    surface.blit(img2, (0, 415))


def draw_food():
    """
    food drawing method.
    """
    for spot in food_spots:
        rect = pygame.Rect(
            spot[0] * BLOCKSIZE, spot[1] * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE
        )
        pygame.draw.rect(SCREEN, GREEN, rect, BLOCKSIZE)


def eat_food():
    """
    when the snake head intersects with any food remove it
    from the board and fire off a tail adding event
    """
    food_hold = None
    for food in food_spots:
        if food[0] == snake_head.x and food[1] == snake_head.y:
            snake_head.add_tail()
            food_spots.discard(food)
            global score
            score += 10
            break


def snake_update():
    """
    handle drawing the snake and its tail nows and move them if necessary
    """
    if snake_head.should_move() and not snake_head.dead:
        snake_head.move(move_x, move_y)
    rect = pygame.Rect(
        snake_head.x * BLOCKSIZE, snake_head.y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE
    )
    pygame.draw.rect(SCREEN, RED, rect, BLOCKSIZE)
    tail_node = snake_head.next_node

    while tail_node:
        rect = pygame.Rect(
            tail_node.x * BLOCKSIZE, tail_node.y * BLOCKSIZE, BLOCKSIZE, BLOCKSIZE
        )
        pygame.draw.rect(SCREEN, RED, rect, BLOCKSIZE)
        tail_node = tail_node.next_node
    if snake_head.dead:
        SCREEN.blit(
            kaboom_image, (snake_head.x * BLOCKSIZE - 10, snake_head.y * BLOCKSIZE - 10)
        )
        SCREEN.convert_alpha()


food_time = datetime.now()
while running:
    # poll for events in this event loop, and react
    # pygame.QUIT event means the user clicked X to close your window
    # pygame.KEYDOWN means you are looking for a set of keys being pressed down, not held.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                move_x = -1
                move_y = 0
            elif event.key in [pygame.K_UP, pygame.K_w]:
                move_x = 0
                move_y = -1
            elif event.key in [pygame.K_DOWN, pygame.K_s]:
                move_x = 0
                move_y = 1
            elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                move_x = 1
                move_y = 0
            elif event.key in [pygame.K_r]:
                food_spots = set()
                score = 0
                snake_head.reset()
                food_time = datetime.now()

    SCREEN.fill("black")
    draw_grid()
    snake_update()
    if food_time + timedelta(seconds=5) <= datetime.now():
        add_food()
        food_time = datetime.now()
    draw_food()
    eat_food()
    draw_text(pygame, SCREEN)
    pygame.display.flip()

    
