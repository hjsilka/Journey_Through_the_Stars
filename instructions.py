import pygame

from constants import WHITE, BLACK, screen, SCREEN_WIDTH, SCREEN_HEIGHT, clock, FPS


def instructions():
    font = pygame.font.Font("media/fonts/typewriter.ttf", 17)
    image = pygame.image.load('media/images/arrow_keys.png')

    instructions_text = (
        "Follow the little prince as he tells you\n"
        "about his journey through the universe\n"
        "and the different people he met.\n\n"
        "Use the arrow keys to move through\n"
        "the universe and select the planets\n"
        "you want to learn more about.\n"
    )

    # draw multi line text
    def draw_multiline_text(text, x, y, line_height=30):
        screen.blit(image, (50, SCREEN_HEIGHT // 2 - image.get_height() // 2))
        lines = text.split('\n')
        for i, line in enumerate(lines):
            txt_surface = font.render(line, True, WHITE)
            screen.blit(txt_surface, (x, y + i * line_height))

    # esc instructions at the bottom
    def draw_back_instructions():
        back_text = font.render(
            "Press ESC to return to the menu", True, WHITE
        )
    # position of the text
        screen.blit(
            back_text,
            (SCREEN_WIDTH // 2 - back_text.get_width() // 2, SCREEN_HEIGHT -30)
        )

    running = True
    while running:
        screen.fill(BLACK)
        draw_multiline_text(instructions_text, SCREEN_WIDTH // 2 - 280, SCREEN_HEIGHT // 2 - 100, line_height=30)
        draw_back_instructions()
        pygame.display.flip() # update display wth everything drawn

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit program if window is closed
                pygame.quit()
                exit()

            # go back to menu on esc
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        clock.tick(FPS)




