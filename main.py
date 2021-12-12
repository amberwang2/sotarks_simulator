import pygame
import os
import random
from constants import *
import load_assets
from map_tools import *

# setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CURSOR_RECT = load_assets.CURSOR.get_rect()
pygame.display.set_caption('sotarks simulator')
pygame.mouse.set_visible(False)
game_status = False
results_screen = False
font_48 = pygame.font.Font(os.path.join('assets', 'FiraCode-Regular.ttf'), 48)
welcome_text = font_48.render("Press enter to start", True, WHITE)

def change_status():
    global game_status, current_map, current_time
    game_status = not game_status
    current_time = 0
    if game_status:
        current_map = new_map(40)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not game_status:
                    change_status()

        if game_status:
            game()
        else:
            start_screen()

    pygame.quit()

def start_screen():
    WIN.fill(BLACK)
    WIN.blit(welcome_text, (0, 0))
    CURSOR_RECT.center = pygame.mouse.get_pos()
    WIN.blit(load_assets.CURSOR, CURSOR_RECT)
    pygame.display.update()

def game():
    global current_time
    WIN.fill(BLACK)
    # stuff
    update_objects(current_map, current_time)
    for i in current_map:
        if i.field:
            copy = load_assets.CIRCLE.copy()
            copy.set_alpha(i.opacity*255)
            WIN.blit(copy, (i.x - 64, i.y - 64))
            if i.field_time < 600:
                scaled = pygame.transform.scale(load_assets.A_CIRCLE, (i.approach_mult, i.approach_mult))
                scaled.set_alpha(i.opacity*255)
                WIN.blit(scaled, (i.x - (scaled.get_width()//2), i.y - (scaled.get_height()//2)))
    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_z or event.key == pygame.K_x:
    #             print("keypress", event.key)
    #             pos = pygame.mouse.get_pos()
    #             for i in current_map:
    #                 if i.hit_window:
    #                     if (i.x - pos[0])**2 + (i.y - pos[1])**2 < 64**2:
    #                         precision = abs(i.timing_point - current_time)
    #                         if precision <= 30:
    #                             i.score = 300
    #                         elif precision <= 75:
    #                             i.score = 100
    #                         elif precision <= 120:
    #                             i.score = 50
    #                         print("HIT ", i.score)
    #                         i.field = False
    current_time += 10
    # end stuff
    CURSOR_RECT.center = pygame.mouse.get_pos()
    WIN.blit(load_assets.CURSOR, CURSOR_RECT)
    pygame.display.update()

def results_screen():
    WIN.fill(BLACK)
    CURSOR_RECT.center = pygame.mouse.get_pos()
    WIN.blit(load_assets.CURSOR, CURSOR_RECT)
    pygame.display.update()


if __name__ == "__main__":
    main()
