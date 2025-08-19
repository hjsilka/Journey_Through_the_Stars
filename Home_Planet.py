import pygame
from planet_class import PlanetScreen
from constants import screen, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class HomePlanet(PlanetScreen):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/rose.png')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.font = pygame.font.Font('fonts/typewriter.ttf', 10)
        self.description = (
            "This is my home planet. It is very small - so small that I can\n"
            "watch the sunset just by moving my chair a few steps.\n"
            "I live there with my rose, who is proud and demanding but also\n"
            "very precious to me. I also spend much of my time caring for the planet,\n"
            "pulling up dangerous baobab shoots before they grow too large,\n"
            "and tending to my volcanoes.\n"
            "Though my planet is tiny, it is my whole world. Leaving it to explore\n"
            "the stars filled me with both curiosity and sadness, for I carried with\n"
            "me the love - and the worry - I felt for my rose.\n"
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