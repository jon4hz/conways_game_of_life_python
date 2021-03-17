#!/usr/bin/env python3
#
# Author: jon4hz
# Date: 02.03.20201
# Desc: Building a board in pygame
#
#######################################################################################################################

import sys, pygame
# pylint: disable=no-name-in-module
from pygame.constants import (
    QUIT,
    MOUSEBUTTONDOWN
)
# CONSTANTS
RECT_SIZE = 20
SIZE = WIDTH, HEIGHT = 500, 500
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
TITLE = "Conways Game of Life"

def build_board() -> pygame.Surface:
    # pylint: enable=no-name-in-module
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member

    

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(TITLE)
    screen.fill(WHITE)
    print(type(screen))
    pygame.mouse.set_visible(1)
    

    for y in range(HEIGHT):
        for x in range(WIDTH):
            rect = pygame.Rect(x*RECT_SIZE, y*RECT_SIZE, RECT_SIZE, RECT_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)
    
    return screen

def calculate_position(pos) -> tuple:
    x = int(pos[0]/RECT_SIZE)
    y = int(pos[1]/RECT_SIZE)
    return (x, y)

if __name__ == "__main__":
    screen = build_board()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                # pylint: disable=no-member
                pygame.quit()
                # pylint: enable=no-member
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos = calculate_position(pos)
                rect = pygame.Rect(pos[0]*RECT_SIZE, pos[1]*RECT_SIZE, RECT_SIZE, RECT_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 0)
        pygame.display.update()