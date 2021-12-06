import pygame
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

if __name__ == "__main__":
    main()
