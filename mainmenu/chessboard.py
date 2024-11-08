import chess
import chess.engine
import pygame
import sys

STOCKFISH_PATH = "C:/Users/soohu/OneDrive/Desktop/stockfish-windows-x86-64-avx2/stockfish/stockfish-windows-x86-64-avx2.exe"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

LIGHT_SQUARE_COLOR = (240, 217, 181)
DARK_SQUARE_COLOR = (181, 136, 99)
HIGHLIGHT_COLOR = (255, 0, 0)

# Screen dimensions for the chessboard screen
SCREEN_WIDTH, SCREEN_HEIGHT = 659, 693

# Define button color and font for the "Back" button
BUTTON_COLOR = (150, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Set up Pygame and screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("King's Fall - Reverse Chess")

# Load piece images and scale them
def load_piece_images(square_size):
    pieces = {}
    for piece in ['p', 'n', 'b', 'r', 'q', 'k', 'pp', 'nn', 'bb', 'rr', 'qq', 'kk']:
        pieces[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (square_size, square_size))
    return pieces

square_size = min(SCREEN_WIDTH, SCREEN_HEIGHT - 100) // 8  # Adjust for screen size with back button
piece_images = load_piece_images(square_size)

# Draw the chessboard and pieces
def draw_board(screen):
    for row in range(8):
        for col in range(8):
            color = LIGHT_SQUARE_COLOR if (row + col) % 2 == 0 else DARK_SQUARE_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

def draw_pieces(screen, board):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_str = piece.symbol()
            piece_img = piece_images[piece_str.lower() if piece_str.islower() else piece_str.lower() + piece_str.lower()]
            col, row = chess.square_file(square), chess.square_rank(square)
            screen.blit(piece_img, pygame.Rect(col * square_size, (7 - row) * square_size, square_size, square_size))

# Draw a back button at the bottom of the screen
def draw_back_button():
    font = pygame.font.Font(None, 36)
    back_button_rect = pygame.Rect((SCREEN_WIDTH - 100) // 2, SCREEN_HEIGHT - 60, 100, 40)
    pygame.draw.rect(screen, BUTTON_COLOR, back_button_rect)
    back_text = font.render("Back", True, TEXT_COLOR)
    screen.blit(back_text, (back_button_rect.x + (back_button_rect.width - back_text.get_width()) // 2,
                            back_button_rect.y + (back_button_rect.height - back_text.get_height()) // 2))
    return back_button_rect

# Main function to run the chessboard with AI option
def run_chessboard(ai=False, back_callback=None):
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize a new chess board every time run_chessboard is called
    board = chess.Board()  # Reset board to the initial state
    selected_square = None
    running = True

    while running:
        screen.fill((0, 0, 0))  # Fill screen with black background
        draw_board(screen)
        draw_pieces(screen, board)

        # Draw the "Back" button
        back_button_rect = draw_back_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button only
                mouse_x, mouse_y = event.pos

                # Check if the back button was clicked
                if back_button_rect.collidepoint(mouse_x, mouse_y):
                    if back_callback:
                        back_callback()
                    return  # Exit to main menu

                # Convert mouse position to chessboard square
                if mouse_y < 8 * square_size:  # Only detect clicks on the board
                    col = mouse_x // square_size
                    row = 7 - (mouse_y // square_size)
                    square = chess.square(col, row)

                    if selected_square is None:
                        selected_square = square
                    else:
                        move = chess.Move(selected_square, square)
                        if move in board.legal_moves:
                            board.push(move)
                            selected_square = None
                            if ai and not board.is_game_over():
                                ai_move = engine.play(board, chess.engine.Limit(time=2.0)).move
                                board.push(ai_move)
                        else:
                            selected_square = None

        pygame.display.flip()
