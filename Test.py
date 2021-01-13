import pygame
import sys
import os

from pygame.locals import *

pygame.init()
Display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Test")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() 
