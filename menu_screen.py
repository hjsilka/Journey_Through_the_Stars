import pygame
import math
import sys
from button import Button
from constants import screen, SCREEN_WIDTH, clock, FPS
from universe import universe

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('media/Hans Zimmer, Richard Harvey - Preparation.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.Font('fonts/moonstar.ttf', 30)

def main_menu():
   # buttons
    PLAY_BUTTON = Button(250, 200, 300, 80, "PLAY", font, screen)
    QUIT_BUTTON = Button(250, 320, 300, 80, "QUIT", font, screen)

    while True:
        #load image
        bg =pygame.image.load('background/universe.png').convert()
        bg_width = bg.get_width()
        #  game variables
        scroll = 0
        tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

        #game loop
        run = True
        while run:
            clock.tick(FPS)

            # draw scrolling background
            for i in range(0, tiles):
                screen.blit(bg, (i * bg_width + scroll, 0))
            #scroll background
            scroll -= 3
            # reset scroll
            if abs(scroll) > bg_width:
                scroll = 0

            #event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.rect.collidepoint(event.pos):
                        print("pressed")
                        universe()
                    if QUIT_BUTTON.rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            PLAY_BUTTON.update()
            QUIT_BUTTON.update()

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    main_menu()