import pygame
from planet_class import PlanetScreen
from constants import screen, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class GeoPlanet(PlanetScreen):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/geographer.PNG')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.font = pygame.font.Font('fonts/typewriter.ttf', 10)
        self.description = (
            "The sixth planet I visited was home to a geographer. At first,\n"
            "I was excited, thinking he might finally be a wise adult.\n"
            "But he couldn’t even tell me if his own planet had seas, mountains,\n"
            "or rivers - he never left his desk. He relied on explorers to bring\n"
            "him knowledge, but there were none.\n"
            "It was he who taught me the word ephemeral. For the first time,\n"
            "I understood that my rose would not last forever, and I felt regret\n"
            "for leaving her. Still, I gathered my courage and continued\n"
            "on my journey to Earth.\n"
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