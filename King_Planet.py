import pygame
from planet_class import PlanetScreen
from constants import screen, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class KingPlanet(PlanetScreen):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/king.png')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.font = pygame.font.Font('fonts/typewriter.ttf', 10)
        self.description = (
            "After leaving my planet, the first planet I visited on my journey\n"
            "was inhabited by a king. This king was very proud to be king for\n"
            "someone. When I yawned, he got angry, and when I told him I\n"
            "couldn't help but yawn, he ordered me to yawn. When I asked him to\n"
            "sit down, he ordered me to sit down. While the king claimed to have\n"
            "power and absolute authority, he was really all alone with nothing to\n"
            "rule over. Later on earth, I learned that there are many rulers who\n"
            "make a big deal about the power they have, but who, in actuality,\n"
            "are ineffective at enforcing the power they claim to have.\n"
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