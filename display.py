import pygame
import constants
import assets
import map_generator

'''
Each returns what draw() needs to display?
'''
def init():
    pygame.init()
    FONT = pygame.font.Font('FiraCode-Regular.ttf', 32)

def start_screen():
    text = assets.FONT.render('Press enter to begin', True, constants.WHITE, constants.BLACK)

def game(): # return list of objects for which on_field = True
    pygame.mouse.set_visible(False)
    CURSOR_RECT = assets.CURSOR.get_rect()
    WIN.blit(assets.CURSOR, CURSOR_RECT)
     pass

def result_screen():
     pass
