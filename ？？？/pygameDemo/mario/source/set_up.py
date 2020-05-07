import pygame
from . import constants as c
from . import tools


pygame.init()
SCREEN = pygame.display.set_mode((c.SCREEN_W, c.SCREEN_H))
GRAPHICS = tools.load_graphics('./resources/graphics')