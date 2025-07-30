import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

#game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Journey Through the Stars')

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
    scroll -= 5

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

