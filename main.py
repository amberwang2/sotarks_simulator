import pygame
import os
import random
from constants import *
import load_assets

# setup
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CURSOR_RECT = load_assets.CURSOR.get_rect()
pygame.display.set_caption('sotarks simulator')
pygame.mouse.set_visible(False)
game_status = False
font_48 = pygame.font.Font(os.path.join('assets', 'FiraCode-Regular.ttf'), 48)
welcome_text = font_48.render("Press enter to start", True, WHITE)
results_screen = False

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
            WIN.blit(load_assets.CIRCLE, (i.x - 64, i.y - 64))
            if i.field_time < 600:
                scaled = pygame.transform.scale(load_assets.A_CIRCLE, (i.approach_mult, i.approach_mult))
                WIN.blit(scaled, (i.x - (scaled.get_width()//2), i.y - (scaled.get_height()//2)))
    current_time += 10
    # end stuff
    CURSOR_RECT.center = pygame.mouse.get_pos()
    WIN.blit(load_assets.CURSOR, CURSOR_RECT)
    pygame.display.update()

def end_screen():
    WIN.fill(BLACK)
    CURSOR_RECT.center = pygame.mouse.get_pos()
    WIN.blit(load_assets.CURSOR, CURSOR_RECT)
    pygame.display.update()

def new_map(n):
    points = [(random.randint(150, 1130), random.randint(150, 570))]

    for i in range(n - 1):
        temp = True
        while temp:
            point = (random.randint(150, 1130), random.randint(150, 570))
            dist = ((point[0] - points[-1][0])**2 + (point[1] - points[-1][1])**2)**0.5
            if dist > 532:
                points.append(point)
                temp = False

    return [HitObject(points[i][0], points[i][1], i*600 + 3000) for i in range(len(points))]

'''
Generate n number of random points
Each point is at least 532 pixels from the previous point
points -> list of tuples in (x, y) format
screen margin of 150 pixels on all sides
allowed x [150, 1130]
allowed y [150, 570]
'''

def update_objects(objects, time):
    for i in objects:
        if i.timing_point - 600 == time:
            i.field = True
        if i.timing_point + 120 == time:
            i.field = False
        if i.field:
            i.updater()

class HitObject: # circle size 128x128
    field = False # is the object on field?
    hit_window = False # is the hit window for the object active?
    field_time = 0  # time object has been on field in ms
    hit = False
    score = None

    def __init__(self, x, y, timing_point):
        self.x = x
        self.y = y
        self.timing_point = timing_point

    def updater(self):
        self.approach_mult = round(134 * (3 - self.field_time / 200)) if self.field_time <= 400 else 1
        self.opacity = self.field_time / 400 if self.field_time <= 400 else 1
        self.field_time += 10


if __name__ == "__main__":
    main()
