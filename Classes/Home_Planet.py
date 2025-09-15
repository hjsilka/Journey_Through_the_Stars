import sys
import pygame
from Classes.planet_class import PlanetScreen
from constants import screen, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, clock
from Classes.button import Button

# this screen shows information about the home planet of the little prince with an
# image of his rose. there is also a mini-game button that leads to
# whack-a-mole inspired mini-game

class HomePlanet(PlanetScreen):
    def __init__(self):
        super().__init__()

        # load a and scale images
        self.image = pygame.image.load('media/images/rose.png')
        self.image = pygame.transform.scale(self.image, (300, 300))

        # font for text and button
        self.font = pygame.font.Font('media/fonts/typewriter.ttf', 10)

        # mini game button
        self.mini_game_button = Button(500, 200, 200, 50, "mini-game", self.font, screen)
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

    # draw background, image, button, description, esc instructions
    # line spacing & alignment calculation was refined with AI assistance
    def draw(self):
        screen.fill(BLACK)
        screen.blit(self.image, (50, SCREEN_HEIGHT // 2 - self.image.get_height() // 2))

        self.mini_game_button.update()
        self.draw_multiline_text(self.description, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, line_height=25)

        super().draw_back_instructions() # esc instructions from base class

    # split description into lines
    def draw_multiline_text(self, text, x, y, line_height=30):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            txt_surface = self.font.render(line, True, WHITE)
            screen.blit(txt_surface, (x, y + i * line_height))

    # main loop (handles events and updates display)
    def run(self):
        self.running = True
        while self.running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # if mini-game button is clicked
                    if self.mini_game_button.rect.collidepoint(event.pos): # mini games button click
                        print("pressed minigame")
                        self.start_mini_game()

            self.draw()
            pygame.display.update()

    def start_mini_game(self):
        from rose_mini_game import MiniGame
        mini_game = MiniGame()
        mini_game.run()

