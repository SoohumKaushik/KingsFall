import pygame
import sys
from chessboard import run_chessboard

# Initialize Pygame
pygame.init()

# Load the background image for the main menu (relative path to the image folder)
background_image = pygame.image.load("images/kingsfall.webp")

# Set up colors for the play mode screen
RED_THEME_COLOR = (150, 0, 0)
HOVER_COLOR = (200, 0, 0)
DEFAULT_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("King's Fall")

# Font setup
font = pygame.font.Font(None, 36)

# Button setup
button_width, button_height = 200, 50
play_ai_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 3, button_width, button_height)
play_player_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 3 + 100, button_width, button_height)

# Function to maintain aspect ratio for main menu image
def maintain_aspect_ratio(window_width, window_height, image_width, image_height):
    aspect_ratio = image_width / image_height
    if window_width / window_height > aspect_ratio:
        new_width = int(window_height * aspect_ratio)
        new_height = window_height
    else:
        new_width = window_width
        new_height = int(window_width / aspect_ratio)
    return new_width, new_height

# Main Menu Loop
def main_menu_screen():
    image_width, image_height = background_image.get_width(), background_image.get_height()
    running = True
    while running:
        screen.fill((0, 0, 0))  # Black background
        window_width, window_height = screen.get_size()
        new_width, new_height = maintain_aspect_ratio(window_width, window_height, image_width, image_height)
        scaled_background = pygame.transform.scale(background_image, (new_width, new_height))
        screen.blit(scaled_background, (0, 0))

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Simulating a Play Button click to go to the Play Mode screen
                if event.button == 1:
                    play_mode_screen()

        pygame.display.flip()

# Function to draw buttons on play mode screen
def draw_buttons():
    pygame.draw.rect(screen, DEFAULT_COLOR, play_ai_button_rect, 2)
    pygame.draw.rect(screen, DEFAULT_COLOR, play_player_button_rect, 2)

    # Render text
    ai_text = font.render("Play Against AI", True, TEXT_COLOR)
    player_text = font.render("Play Against Player", True, TEXT_COLOR)

    # Blit text to screen
    screen.blit(ai_text, (play_ai_button_rect.x + (button_width - ai_text.get_width()) // 2, play_ai_button_rect.y + (button_height - ai_text.get_height()) // 2))
    screen.blit(player_text, (play_player_button_rect.x + (button_width - player_text.get_width()) // 2, play_player_button_rect.y + (button_height - player_text.get_height()) // 2))

# Play Mode Screen Loop
def play_mode_screen():
    running = True
    while running:
        screen.fill(RED_THEME_COLOR)  # Fill with red theme color
        mouse_pos = pygame.mouse.get_pos()

        # Button hover effect
        if play_ai_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HOVER_COLOR, play_ai_button_rect, 2)
        else:
            pygame.draw.rect(screen, DEFAULT_COLOR, play_ai_button_rect, 2)

        if play_player_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HOVER_COLOR, play_player_button_rect, 2)
        else:
            pygame.draw.rect(screen, DEFAULT_COLOR, play_player_button_rect, 2)

        draw_buttons()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if buttons are clicked
                if play_ai_button_rect.collidepoint(mouse_pos):
                    print("Play against AI clicked!")
                    run_chessboard(ai=True)  # Start chessboard with AI opponent
                    running = False

                elif play_player_button_rect.collidepoint(mouse_pos):
                    print("Play against Player clicked!")
                    run_chessboard(ai=False)  # Start chessboard without AI
                    running = False

        pygame.display.flip()

# Main loop
def main():
    main_menu_screen()

if __name__ == "__main__":
    main()
