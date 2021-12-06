import pygame
import constants
import assets

pygame.display.set_caption('sotarks simulator')

game_status = 'start_screen'

def draw(WIN):
    WIN.fill(constants.BLACK)
    if game_status == 'start_screen':
        display.start_screen()
    elif game_status == 'game':
        display.game()
    elif game_status == 'end_screen':
        display.end_screen()
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(constants.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(constants.WIN)

    pygame.quit()

if __name__ == "__main__":
    main()
