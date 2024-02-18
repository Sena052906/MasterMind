import pygame

#colours that I am using (r, g, b)

PURPLE = (238, 130, 230)
BLACK = (30, 30, 30)
ORANGE = (255, 127, 0)
DARKGREY = (35, 42, 45)
LIGHTGREY = (211, 211, 211)
YELLOW = (255, 255, 0)
DARKBROWN = (55, 22, 30)
BLUE = (0, 0, 255)
BGCOLOUR = (85, 32, 15)
GREEN = (0,255,0)
WHITE = (240,240,240)
RED = (230,0,0)
COLOURS = (WHITE,RED,GREEN,YELLOW,BLUE,ORANGE,BLACK,PURPLE)

# Settings for the game
ROWS = 5
COLS = 13
TILESIZE = 60
AMOUNT_COLOUR = 8


WIDTH = (ROWS * TILESIZE) + 1
HEIGHT = (COLS * TILESIZE) + 1
FPS = 60
TITLE = "MasterMind"