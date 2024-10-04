import chess
import chess.engine
import pygame
import sys

# Path to Stockfish
STOCKFISH_PATH = "C:\\Users\\Soohum Kaushik\\Desktop\\stockfish-windows-x86-64-avx2\\stockfish\\stockfish-windows-x86-64-avx2.exe"

# Try to initialize Stockfish engine
try:
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
except FileNotFoundError:
    print(f"Stockfish engine not found at {STOCKFISH_PATH}. Please check the path.")
    sys.exit()

LIGHT_SQUARE_COLOR = (240, 217, 181)
DARK_SQUARE_COLOR = (181, 136, 99)
HIGHLIGHT_COLOR = (255, 0, 0)

def load_piece_images():
    pieces = {}
    for piece in ['p', 'n', 'b', 'r', 'q', 'k', 'pp', 'nn', 'bb', 'rr', 'qq', 'kk']:
        pieces[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (80, 80))
    return pieces

piece_images = load_piece_images()

board = chess.Board()

def draw_board(screen):
    for row in range(8):
        for col in range(8):
            color = LIGHT_SQUARE_COLOR if (row + col) % 2 == 0 else DARK_SQUARE_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(col * 80, row * 80, 80, 80))

def draw_pieces(screen):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_str = piece.symbol()
            piece_img = piece_images[piece_str.lower() if piece_str.islower() else piece_str.lower() + piece_str.lower()]
            col, row = chess.square_file(square), chess.square_rank(square)
            screen.blit(piece_img, pygame.Rect(col * 80, (7 - row) * 80, 80, 80))

# Function to get the AI move in reverse chess
def get_reverse_ai_move(board):
    legal_moves = list(board.legal_moves)
    capture_moves = [move for move in legal_moves if board.is_capture(move)]
    
    if capture_moves:
        return capture_moves[0]
    else:
        result = engine.play(board, chess.engine.Limit(time=2.0))
        return result.move

# Function to handle player moves
def handle_player_move(selected_square, target_square):
    move = chess.Move(selected_square, target_square)
    if move in board.legal_moves:
        board.push(move)
        return True
    return False

def run_chessboard(ai=False):
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("King's Fall - Reverse Chess")
    
    running = True
    selected_square = None

    while running:
        draw_board(screen)
        draw_pieces(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = mouse_x // 80
                row = 7 - (mouse_y // 80)
                square = chess.square(col, row)

                if selected_square is None:
                    selected_square = square
                else:
                    if handle_player_move(selected_square, square):
                        selected_square = None
                        if ai and not board.is_game_over():
                            ai_move = get_reverse_ai_move(board)
                            if ai_move:
                                board.push(ai_move)
                            else:
                                print("AI failed to move")
                    else:
                        selected_square = None

        if board.is_game_over():
            result = "Game over: " + board.result()
            print(result)
            break

        if selected_square is not None:
            col, row = chess.square_file(selected_square), chess.square_rank(selected_square)
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, pygame.Rect(col * 80, (7 - row) * 80, 80, 80), 3)

        pygame.display.flip()

