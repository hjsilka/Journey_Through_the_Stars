import sys

import pygame
from constants import screen, FPS, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, clock

class MiniGame:
    def __init__(self):
        self.running = False
        self.font = pygame.font.Font('media/fonts/typewriter.ttf', 10)

    def run(self):
        self.running = True
        while self.running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False

            screen.fill(BLACK)
            pygame.display.flip()

