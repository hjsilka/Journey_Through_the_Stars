import pygame
from planet_class import PlanetScreen
from constants import screen, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class BusinessPlanet(PlanetScreen):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/businessman.PNG')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.font = pygame.font.Font('fonts/typewriter.ttf', 10)
        self.description = (
            "The fourth planet I visited was inhabited by a businessman.\n"
            "He didn't even have time to raise his head when I arrived;\n"
            "that's how busy he was. All he did was mumble numbers,\n"
            "and he did not seem very interested in making conversation with me,\n"
            "as he was too busy counting the stars. He explained to me that\n"
            "he owned to stars, not the king, as kings reign over things but\n"
            "don't have them. Apparently, owning the stars made him rich, so\n"
            "that if someone ever found new stars, he could buy them too.\n"
            "His reasoning reminded me a little of the drunkard.\n"
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