import pygame
import math
import sys
from Classes.button import Button
from constants import screen, SCREEN_WIDTH, clock, FPS
from universe import universe
from instructions import instructions

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('media/music/Hans Zimmer, Richard Harvey - Preparation.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.Font('media/fonts/moonstar.ttf', 30)

def main_menu():
   # buttons
    PLAY_BUTTON = Button(250, 150, 300, 80, "PLAY", font, screen)
    QUIT_BUTTON = Button(250, 350, 300, 80, "QUIT", font, screen)
    INSTRUCTIONS_BUTTON = Button(250, 250, 300, 80, "INSTRUCTIONS", font, screen)

    while True:
        #load image
        bg1 = pygame.image.load('media/background/universe.png').convert()
        bg2 = pygame.image.load('media/background/universe2.png').convert()
        bg_width = bg1.get_width()
        #  game variables
        scroll = 0
        tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

        #game loop
        run = True
        while run:
            clock.tick(FPS)

            # draw scrolling background
            for i in range(tiles):
                if i % 2 == 0:
                    screen.blit(bg1, (i * bg_width + scroll, 0))
                else:
                    screen.blit(bg2, (i * bg_width + scroll, 0))

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
                    if INSTRUCTIONS_BUTTON.rect.collidepoint(event.pos):
                        instructions()

            PLAY_BUTTON.update()
            QUIT_BUTTON.update()
            INSTRUCTIONS_BUTTON.update()

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    main_menu()