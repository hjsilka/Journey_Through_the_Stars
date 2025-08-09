import pygame
import sys
from constants import BLACK, WHITE, FPS, PRINCE_COLOR, screen, SCREEN_WIDTH, SCREEN_HEIGHT

def universe():

    font = pygame.font.SysFont(None, 24)

    clock = pygame.time.Clock()

    background = pygame.image.load('background/universe.png')
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    planet_images = {
        "King's Planet": pygame.transform.scale(pygame.image.load("planets/planet_king.png"), (60, 60)),
        "Conceited Man's Planet": pygame.transform.scale(pygame.image.load("planets/planet_sun.png"), (60, 60)),
        "Drunkard's Planet": pygame.transform.scale(pygame.image.load("planets/planet_drunk.png"), (60, 60)),
        "Businessman's Planet": pygame.transform.scale(pygame.image.load("planets/planet_business.png"), (60, 60)),
        "Lamplighters's Planet": pygame.transform.scale(pygame.image.load("planets/planet_lamp.png"), (60, 60)),
        "Geographer's Planet": pygame.transform.scale(pygame.image.load("planets/planet_geo.png"), (60, 60)),
        "Home Planet": pygame.transform.scale(pygame.image.load("planets/planet_earth.png"), (60, 60))
    }

    # Little Prince (replace with image)
    prince_pos = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    PRINCE_RADIUS = 15
    prince_speed = 5

    # Planets
    planets = [
        (150, 150, 30, "King's Planet"),
        (650, 100, 30, "Businessman's Planet"),
        (400, 300, 30, "Lamplighters's Planet"),
        (200, 450, 30, "Geographer's Planet"),
        (600, 450, 30, "Home Planet"),
        (300, 200, 30, "Drunkard's Planet"),
    ]

    def draw_planet(x, y, radius, name):
        image = planet_images[name]
        rect = image.get_rect(center=(x, y))
        screen.blit(image, rect)
        label = font.render(name, True, WHITE)
        screen.blit(label, (x - label.get_width() / 2, y + radius + 40))

    # check prince and planet collision
    def prince_planet_collision(prince_pos, planet):
        px, py = prince_pos.x, prince_pos.y
        x, y, r, _ = planet
        distance = ((px - x) ** 2 + (py - y) ** 2) ** 0.5
        return distance <= PRINCE_RADIUS + r

    def star_map():
        prince_pos = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        PRINCE_RADIUS = 15
        prince_speed = 5
        running = True
        selected_planet = None

        while running:
            screen.blit(background, (0, 0))

            for planet in planets:
                draw_planet(*planet)

            pygame.draw.circle(screen, PRINCE_COLOR, (int(prince_pos.x), int(prince_pos.y)), PRINCE_RADIUS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and selected_planet:
                        return selected_planet

            # Movement keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                prince_pos.x -= prince_speed
            if keys[pygame.K_RIGHT]:
                prince_pos.x += prince_speed
            if keys[pygame.K_UP]:
                prince_pos.y -= prince_speed
            if keys[pygame.K_DOWN]:
                prince_pos.y += prince_speed

            # Keep prince on screen
            prince_pos.x = max(PRINCE_RADIUS, min(SCREEN_WIDTH - PRINCE_RADIUS, prince_pos.x))
            prince_pos.y = max(PRINCE_RADIUS, min(SCREEN_HEIGHT - PRINCE_RADIUS, prince_pos.y))

            # Check if Prince is on any planet
            selected_planet = None
            for planet in planets:
                if prince_planet_collision(prince_pos, planet):
                    selected_planet = planet
                    # highlight the planet
                    pygame.draw.circle(screen, WHITE, (planet[0], planet[1]), planet[2] + 5, 3)

            # Instructions
            if selected_planet:
                info_text = f"Press ENTER to visit {selected_planet[3]}"
                info_label = font.render(info_text, True, WHITE)
                screen.blit(info_label, (SCREEN_WIDTH // 2 - info_label.get_width() // 2, SCREEN_HEIGHT - 40))

            pygame.display.flip()
            clock.tick(60)



    def main():
        while True:
            selected_planet = star_map()
            if selected_planet:
                pass

    main()


