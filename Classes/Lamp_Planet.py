import pygame
from Classes.planet_class import PlanetScreen
from constants import screen, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class LampPlanet(PlanetScreen):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('media/images/lamplighter.png')
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.font = pygame.font.Font('media/fonts/typewriter.ttf', 10)
        self.description = (
            "The fifth planet I visited was the smallest of them all,\n"
            "and all it had was a lamppost and a lamplighter.\n"
            "It made no sense to have a lamppost on a planet with no houses\n"
            "or population, but to me, the the blind obedience of the lamplighter\n"
            "was still less absurd than the king, the vain one, the drinker,\n"
            "and the businessman, since at least his work made sense. His work was useful,\n"
            "because it was beautiful. When he lights up his lamp, it is as if he were\n"
            "creating a new star or flower, and when he turns off his street lamp,\n"
            "he puts the star or flower to sleep.\n"
        )
# picture and text
# line spacing & alignment calculation was refined with AI assistance
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