import pygame

def run_rules():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))  # Set window size for rules screen
    pygame.display.set_caption("King's Fall - Rules")
    font = pygame.font.SysFont('Arial', 24)
    rules_text = [
        "Rules of King's Fall:",
        "1. The goal is to lose by getting checkmated.",
        "2. You can only move according to chess rules.",
        "3. You win by allowing your opponent to checkmate you.",
        "4. Other rules to be added..."
    ]

    # Define the back button
    back_button_rect = pygame.Rect(10, 10, 100, 40)  # Back button on the top left corner

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check if the back button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_pos):
                    print("Back button clicked!")
                    return  # Return to the main menu

        # Fill screen with white and display rules
        screen.fill((255, 255, 255))
        for i, line in enumerate(rules_text):
            text_surface = font.render(line, True, (0, 0, 0))
            screen.blit(text_surface, (20, 50 + i * 30))

        # Draw the back button (as a simple rectangle for now)
        pygame.draw.rect(screen, (255, 0, 0), back_button_rect)
        text_surface = font.render("Back", True, (255, 255, 255))
        screen.blit(text_surface, (20, 15))  # Adjust the position of the text

        pygame.display.flip()

    pygame.quit()
