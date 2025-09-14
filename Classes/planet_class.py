import pygame
import sys
from constants import BLACK, WHITE, FPS, screen, SCREEN_WIDTH, SCREEN_HEIGHT, clock

# base class for the different planet screens

class PlanetScreen:
    def __init__(self):
        self.running = False

# main loop
    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.draw()
            self.draw_back_instructions()
            pygame.display.flip()
            clock.tick(FPS)

# handles events (subclasses can extend this)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

# default draw method (subclasses override this)
    def draw(self):
        screen.fill(BLACK)

# instructions (self.font needs to be defined in subclass)
    def draw_back_instructions(self):
        back_text = self.font.render(
            "Press ESC to return to the star map", True, WHITE
        )
        screen.blit(
            back_text,
            (SCREEN_WIDTH // 2 - back_text.get_width() // 2, SCREEN_HEIGHT -30)
        )
