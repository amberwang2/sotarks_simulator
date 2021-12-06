import pygame
import constants
import assets
import map_generator
from hit_object import HitObject

WIN = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption('sotarks simulator')

def draw():
    WIN.blit(assets.CIRCLE, (0, 0))
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

if __name__ == "__main__":
    main()
