import sys
import pygame
import random
import time
from constants import screen, FPS, BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, clock

# constants
GRID_SIZE = 3
CELL_SIZE = 100
GRID_SPACING = 20
BAOBAB_SIZE = 80
HOLE_COLOR = (100, 100, 100)

GAME_TIME = 30
BAOBAB_TIME = 0.7

GRID_PIXEL_WIDTH = GRID_SIZE * CELL_SIZE + (GRID_SIZE - 1) * GRID_SPACING
GRID_PIXEL_HEIGHT = GRID_SIZE * CELL_SIZE + (GRID_SIZE - 1) * GRID_SPACING

GRID_OFFSET_X = (SCREEN_WIDTH - GRID_PIXEL_WIDTH) // 2
GRID_OFFSET_Y = (SCREEN_HEIGHT - GRID_PIXEL_HEIGHT) // 2

# load and scale images
baobab_image = pygame.image.load('media/images/baobab.png')
baobab_image = pygame.transform.scale(baobab_image, (BAOBAB_SIZE, BAOBAB_SIZE))
hammer_image = pygame.image.load('media/images/hammer.png')
hammer_image = pygame.transform.scale(hammer_image, (50, 50))

class MiniGame:
    def __init__(self, return_home=None):
        self.running = False
        self.return_home = return_home
        self.font = pygame.font.Font('media/fonts/typewriter.ttf', 20)

        self.score = 0 # number of successful hits
        self.start_time = None
        self.last_baobab_time = 0
        self.baobab_position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)) # random starting cell for baobab
        self.baobab_visible = True # is baobab visible

    def start_screen(self):
        intro_text = [
            "Every morning the little prince cultivates his garden",
            "by pulling up baobab seedlings,",
            "as they could destroy his planet if they grow too big.",
            "",
            "Please help him and get rid of all baobab seedlings you see,",
            "",
            "Press ENTER to start"
        ]

        waiting = True # loop
        while waiting:
            clock.tick(FPS)
            screen.fill(BLACK)

            # center text
            y_offset = SCREEN_HEIGHT // 4
            for line in intro_text:
                text_surface = self.font.render(line, True, WHITE)
                text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
                screen.blit(text_surface, text_rect)
                y_offset += 30

            pygame.display.flip()

            for event in pygame.event.get(): # handle events
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False

    def end_screen(self):
        end_text = [
            f"Thank you for helping the little prince. You got rid of {self.score} baobabs",
            "",
            "Press ENTER to play again",
            "Press ESC to go back"
        ]

        waiting = True  # loop
        while waiting:
            clock.tick(FPS)
            screen.fill(BLACK)

            # center text
            y_offset = SCREEN_HEIGHT // 4
            for line in end_text:
                text_surface = self.font.render(line, True, WHITE)
                text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
                screen.blit(text_surface, text_rect)
                y_offset += 30

            pygame.display.flip()

            for event in pygame.event.get(): # handle events
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False
                        self.run()
                    elif event.key == pygame.K_ESCAPE:
                        waiting = False
                        return


    def draw_grid(self): # draw grid of holes
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = GRID_OFFSET_X + col * (CELL_SIZE + GRID_SPACING)
                y = GRID_OFFSET_Y + row * (CELL_SIZE + GRID_SPACING)
                pygame.draw.rect(screen, HOLE_COLOR, (x, y, CELL_SIZE, CELL_SIZE)) # draw rectangle (hole)

    def draw_baobab(self): # draw baobab at given position
        row, col = self.baobab_position
        # center baobab inside the cell
        x = GRID_OFFSET_X + col * (CELL_SIZE + GRID_SPACING) + (CELL_SIZE - BAOBAB_SIZE) // 2
        y = GRID_OFFSET_Y + row * (CELL_SIZE + GRID_SPACING) + (CELL_SIZE - BAOBAB_SIZE) // 2
        screen.blit(baobab_image, (x, y))

    def get_cell_from_mouse(self, pos): # converts mouse position to grid cell coordinates
        x, y = pos # x and y coordinates of mouse position
        x -= GRID_OFFSET_X
        y -= GRID_OFFSET_Y
        if x < 0 or y < 0:
            return None
        col = x // (CELL_SIZE + GRID_SPACING)
        row = y // (CELL_SIZE + GRID_SPACING)
        if row >= GRID_SIZE or col >= GRID_SIZE:
            return None
        return row, col

    def run(self):
        self.start_screen() # show intro before game starts

        self.running = True
        self.start_time = time.time() # start time
        self.last_baobab_time = time.time() # last baobab spawn

        while self.running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # esc to go back
                        self.running = False
                        if self.return_home:
                            return self.return_home()

                if event.type == pygame.MOUSEBUTTONDOWN: # handle mouse click
                    if self.baobab_visible:
                        mouse_pos = pygame.mouse.get_pos() # get mouse coordinates
                        clicked_cell = self.get_cell_from_mouse(mouse_pos) # convert to cell
                        if clicked_cell == self.baobab_position:
                            self.score += 1 # increase score
                            self.baobab_visible = False # baobab disappears after hit

            # timer
            current_time = time.time()
            elapsed_time = current_time - self.start_time # time passed
            remaining_time = GAME_TIME - elapsed_time # calculates remaining time
            if remaining_time <= 0: # checks if the time is up
                self.running = False  # game over
                continue

            # baobab
            if current_time - self.last_baobab_time > BAOBAB_TIME: # time to move baobab
                self.baobab_position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)) # new random position
                self.last_baobab_time = current_time
                self.baobab_visible = True

            screen.fill(BLACK)
            self.draw_grid()
            if self.baobab_visible:
                self.draw_baobab() # draw baobab if visible

            # display remaining time
            time_text = self.font.render(f"Time: {int(remaining_time)}s", True, WHITE)
            screen.blit(time_text, (10, SCREEN_HEIGHT - 100))

            # display score
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            screen.blit(score_text, (10, SCREEN_HEIGHT - 50))

            # hammer cursor
            mouse_pos = pygame.mouse.get_pos()
            hammer_rect = hammer_image.get_rect(center=mouse_pos)
            screen.blit(hammer_image, hammer_rect.topleft)

            pygame.display.flip()

        self.end_screen()