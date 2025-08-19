import pygame

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#game window
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Journey Through the Stars')

clock = pygame.time.Clock()