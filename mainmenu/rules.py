import pygame
import sys

pygame.init()

# Load the background image for the rules screen
background_rules = pygame.image.load("images/rules.png")

# Screen dimensions for the rules screen
RULES_WIDTH, RULES_HEIGHT = 700, 700

# Set up the screen
screen = pygame.display.set_mode((RULES_WIDTH, RULES_HEIGHT))

# Define the back button position and size for the rules screen
back_button_rect = pygame.Rect(422, 635, 110, 55)  # Adjust these values to match the position of the embedded button
def run_rules(back_callback=None):
    global screen
    screen = pygame.display.set_mode((RULES_WIDTH, RULES_HEIGHT))
    running = True
    while running:
        screen.blit(background_rules, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button only
                mouse_pos = event.pos
                if back_button_rect.collidepoint(mouse_pos):
                    if back_callback:
                        back_callback()
                    return  # Exit the rules screen

        pygame.display.flip()








