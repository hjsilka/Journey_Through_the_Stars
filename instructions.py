import pygame

from constants import WHITE, BLACK, screen, SCREEN_WIDTH, SCREEN_HEIGHT, clock

def instructions():
    font = pygame.font.Font("media/fonts/typewriter.ttf", 24)

    instructions_text = (
        "Follow the little prince as he tells you\n"
        "about his journey through the universe\n"
        "and the different people he met.\n\n"
        "Use the arrow keys to move through the universe\n"
        "and select the planets you want to learn more about.\n"
    )

    def draw_multiline_text(text, x, y, line_height=30):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            txt_surface = font.render(line, True, WHITE)
            screen.blit(txt_surface, (x, y + i * line_height))


    screen.fill(BLACK)
    draw_multiline_text(instructions_text, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 100, line_height=30)
    pygame.display.flip()
