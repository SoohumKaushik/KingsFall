import pygame

def run_chessboard():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))  # Set window size for chessboard
    pygame.display.set_caption("King's Fall - Chessboard")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    square_size = 100  # Chessboard 8x8, each square is 100x100

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

        # Draw the chessboard
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

        # Draw the back button (as a simple rectangle for now)
        pygame.draw.rect(screen, (255, 0, 0), back_button_rect)
        font = pygame.font.SysFont('Arial', 24)
        text_surface = font.render("Back", True, (255, 255, 255))
        screen.blit(text_surface, (20, 15))  # Adjust the position of the text

        pygame.display.flip()

    pygame.quit()
