#!/usr/bin/env python3
#
# Author: jon4hz
# Date: 17.03.2021
# Desc: Conways Game of Life, implemented with pygame
#
#######################################################################################################################
import sys, pygame, argparse
import numpy as np
# pylint: disable=no-name-in-module
from pygame.constants import (
    QUIT,
    MOUSEBUTTONDOWN,
    KEYDOWN,
    K_p
)
# pylint: enable=no-name-in-module

from seeds import seeds

# CONSTANTS
RECT_SIZE = 10
SIZE = WIDTH, HEIGHT = 1000, 1000
WHITE = (200, 200, 200, 255)
BLACK = (0, 0, 0, 255)
TITLE = "Conways Game of Life"

def build_board(seed) -> pygame.Surface:
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(TITLE)
    screen.fill(WHITE)
    pygame.mouse.set_visible(1)
    if seed is not None and seed.any():
        for i in range(seed.shape[0]):
            for j in range(seed.shape[1]):
                if seed[i, j] == 1:
                    rect = pygame.Rect(j*RECT_SIZE, i*RECT_SIZE, RECT_SIZE, RECT_SIZE)
                    pygame.draw.rect(screen, BLACK, rect, 0)
                    pygame.display.update(rect)
                elif seed[i, j] == 0:
                    rect = pygame.Rect(j*RECT_SIZE, i*RECT_SIZE, RECT_SIZE, RECT_SIZE)
                    pygame.draw.rect(screen, WHITE, rect, 0)
                    pygame.draw.rect(screen, BLACK, rect, 1)
                    pygame.display.update(rect)
    else:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                rect = pygame.Rect(x*RECT_SIZE, y*RECT_SIZE, RECT_SIZE, RECT_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)
    
    return screen

def calculate_position(pos) -> tuple:
    x = int(pos[0]/RECT_SIZE)
    y = int(pos[1]/RECT_SIZE)
    return (x, y)

def apply_rules(universe, x, y) -> int:
    num_neighbours = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]
    if universe[x, y] and not 2 <= num_neighbours <= 3:
        return 0
    elif num_neighbours == 3:
        return 1
    else:
        return universe[x, y]

def simulation(universe, screen) -> np.array:
    next_universe = np.copy(universe)
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            next_universe[i, j] = apply_rules(universe, i, j)
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            if next_universe[i, j] == 1 and universe[i, j] == 0:
                rect = pygame.Rect(j*RECT_SIZE, i*RECT_SIZE, RECT_SIZE, RECT_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 0)
                pygame.display.update(rect)
            elif next_universe[i, j] == 0 and universe[i, j] == 1:
                rect = pygame.Rect(j*RECT_SIZE, i*RECT_SIZE, RECT_SIZE, RECT_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 0)
                pygame.draw.rect(screen, BLACK, rect, 1)
                pygame.display.update(rect)
    universe[:] = next_universe[:]
    pygame.time.wait(50)
    return universe

if __name__ == "__main__":
    # argparser
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seed', help="set a seed")
    args = parser.parse_args()
    if seed := args.seed:
        try:
            # make sure seed is available
            if seeds[seed].get('seed') == None:
                raise KeyError
            arr = np.zeros((int(HEIGHT/RECT_SIZE), int(WIDTH/RECT_SIZE)))
            arr[seeds[seed].get('co')[0]:len(seeds[seed].get('seed'))+seeds[seed].get('co')[0],seeds[seed].get('co')[1]:len(seeds[seed].get('seed')[0])+seeds[seed].get('co')[1]] = seeds[seed].get('seed')
            # build the inital board
            screen = build_board(arr)
            pygame.display.update()
        except Exception as e:
            print(e)
            screen = build_board(None)
            pygame.display.update()
            universe = np.zeros((int(HEIGHT/RECT_SIZE), int(WIDTH/RECT_SIZE)))
    else:
        screen = build_board(None)
        pygame.display.update()
        universe = np.zeros((int(HEIGHT/RECT_SIZE), int(WIDTH/RECT_SIZE)))

    # set game status initally to 0
    game_status = 0

    # init numpy array with size of the board
    try:
        universe = np.copy(arr)
    except NameError:
        universe = np.zeros((int(HEIGHT/RECT_SIZE), int(WIDTH/RECT_SIZE)))
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member
    # start main loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                # pylint: disable=no-member
                pygame.quit()
                # pylint: enable=no-member
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    if game_status == 0:
                        game_status = 1
                    else:
                        game_status = 0
                        
            if game_status == 0:
                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    array_pos = calculate_position(pos)
                    color = screen.get_at(pos)
                    if color == WHITE:
                        universe[array_pos[1], array_pos[0]] = 1
                        rect = pygame.Rect(array_pos[0]*RECT_SIZE, array_pos[1]*RECT_SIZE, RECT_SIZE, RECT_SIZE)
                        pygame.draw.rect(screen, BLACK, rect, 0)
                    elif color == BLACK:
                        universe[array_pos[1], array_pos[0]] = 0
                        rect = pygame.Rect(array_pos[0]*RECT_SIZE, array_pos[1]*RECT_SIZE, RECT_SIZE, RECT_SIZE)
                        pygame.draw.rect(screen, WHITE, rect, 0)
                        pygame.draw.rect(screen, BLACK, rect, 1)
                    
        
        if game_status == 1:
            prev_universe = np.copy(universe)
            universe = simulation(universe, screen)
            
            # set game_status automatically to 0 if universe didn't change
            if (prev_universe==universe).all():
                game_status = 0
        
        pygame.display.update()
                