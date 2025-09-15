import pygame

# colors
BUTTON_COLOR = (70,130,180)
BUTTON_HOVER = (100, 160, 210)
TEXT_COLOR = "white"
TEXT_HOVER_COLOR = "black"

# this is a reusable button class
# each button can have different text
# the button color changes when the mouse hovers over it

class Button:
    def __init__(self, x, y, width, height, text_input, font, screen):
        self.rect = pygame.Rect(x, y, width, height)
        self.text_input = text_input
        self.font = font
        self.screen = screen
        self.text_color = TEXT_COLOR

        self.text = None
        self.text_rect = None

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        hovering = self.rect.collidepoint(mouse_pos)

        # color based on hovering
        color = BUTTON_HOVER if hovering else BUTTON_COLOR
        self.text_color = TEXT_HOVER_COLOR if hovering else TEXT_COLOR

        # render button text
        self.text = self.font.render(self.text_input, True, self.text_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

        # draw button
        pygame.draw.rect(self.screen, color, self.rect, border_radius=15)
        self.screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if self.rect.collidepoint(position):
            print("pressed")

