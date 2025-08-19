import pygame
from Classes.planet_class import PlanetScreen
from constants import screen, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class VainPlanet(PlanetScreen):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/images/IMG_2391.png')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.font = pygame.font.Font('media/fonts/typewriter.ttf', 10)
        self.description = (
            "The second planet I visited was inhabited by a vain man.\n"
            "To him, all men were admirers. Vain people hear nothing\n"
            "but praise, and anything that was not a compliment or\n"
            "applause received no response. Because of this, my visit\n"
            "was only a short stop.\n"
        )
# picture and text
    def draw(self):
        screen.fill(BLACK)
        screen.blit(self.image, (50, SCREEN_HEIGHT // 2 - self.image.get_height()// 2))
        self.draw_multiline_text(self.description, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, line_height=25)
# split into lines
    def draw_multiline_text(self, text, x, y, line_height=30):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            txt_surface = self.font.render(line, True, WHITE)
            screen.blit(txt_surface, (x, y + i * line_height))