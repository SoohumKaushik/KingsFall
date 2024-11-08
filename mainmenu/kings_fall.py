import pygame
import sys
from chessboard import run_chessboard
from rules import run_rules

pygame.init()

# Load background images
background_main = pygame.image.load("images/loading_page.png")
background_play_against = pygame.image.load("images/play_against.png")

# Screen dimensions for each screen
MAIN_MENU_WIDTH, MAIN_MENU_HEIGHT = 700, 695
PLAY_AGAINST_WIDTH, PLAY_AGAINST_HEIGHT = 700, 700

# Set up the screen
screen = pygame.display.set_mode((MAIN_MENU_WIDTH, MAIN_MENU_HEIGHT))

# Define button positions and sizes based on your adjustments
play_button_rect = pygame.Rect(250, 406, 220, 76)  # Play button on main menu
rules_button_rect = pygame.Rect(250, 500, 220, 76)  # Rules button on main menu

play_ai_button_rect = pygame.Rect(100, 220, 200, 350)  # Play against AI button in play_against
play_player_button_rect = pygame.Rect(420, 220, 200, 350)  # Play against Player button in play_against

# Define the back button for the play_against screen
back_button_rect_play_against = pygame.Rect(555, 620, 160, 90)  # Position and size for the Back button on play_against screen

# Main Menu Loop
def main_menu_screen():
    global screen
    screen = pygame.display.set_mode((MAIN_MENU_WIDTH, MAIN_MENU_HEIGHT))
    running = True
    while running:
        screen.blit(background_main, (0, 0))

        # Event handling for button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check for left mouse button only
                mouse_pos = event.pos
                if play_button_rect.collidepoint(mouse_pos):
                    play_mode_screen()
                elif rules_button_rect.collidepoint(mouse_pos):
                    run_rules(main_menu_screen)  # Pass main_menu_screen as a callback to return to the main menu

        pygame.display.flip()

# Play Mode Screen Loop
def play_mode_screen():
    global screen
    screen = pygame.display.set_mode((PLAY_AGAINST_WIDTH, PLAY_AGAINST_HEIGHT))
    running = True
    while running:
        screen.blit(background_play_against, (0, 0))

        # Event handling for button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check for left mouse button only
                mouse_pos = event.pos
                if play_ai_button_rect.collidepoint(mouse_pos):
                    run_chessboard(ai=True, back_callback=main_menu_screen)  # Go back to loading screen
                elif play_player_button_rect.collidepoint(mouse_pos):
                    run_chessboard(ai=False, back_callback=main_menu_screen)  # Go back to loading screen
                elif back_button_rect_play_against.collidepoint(mouse_pos):
                    main_menu_screen()  # Go back to the loading screen (main menu)

        pygame.display.flip()

# Main loop
def main():
    main_menu_screen()

if __name__ == "__main__":
    main()
