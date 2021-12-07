import pygame
import os
import random
import constants
import assets

WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption('sotarks simulator')
CURSOR_RECT = assets.CURSOR.get_rect()
pygame.mouse.set_visible(False)


def draw():
    WIN.fill(constants.BLACK)
    CURSOR_RECT.center = pygame.mouse.get_pos()
    WIN.blit(assets.CURSOR, CURSOR_RECT)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(constants.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()

def new_points(n):

    points = [(random.randint(150, 1130), random.randint(150, 570))]

    for i in range(n - 1):
        temp = True
        while temp:
            point = (random.randint(150, 1130), random.randint(150, 570))
            dist = ((point[0] - points[-1][0])**2 + (point[1] - points[-1][1])**2)**0.5
            if dist > 532:
                points.append(point)
                temp = False

    return points

def new_map(n):
    return [HitObject(i[0], i[1]) for i in new_points(n)]

'''
Generate n number of random points
Each point is at least 532 pixels from the previous point
points -> list of tuples in (x, y) format
screen margin of 150 pixels on all sides
allowed x [150, 1130]
allowed y [150, 570]
'''

class HitObject: # circle size 128x128
    field = False # is the object on field?
    field_time = 0  # time object has been on field in ms
    opacity = field_time / 400 if field_time <= 400 else 1  # opacity of object
    approach_mult = 2 - field_time / 400  # size of approach circle

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def counter(self):
        self.field_time += 10


if __name__ == "__main__":
    main()
