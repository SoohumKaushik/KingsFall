import pygame
import sys
from chessboard import run_chessboard  # Import from the same directory
from rules import run_rules  # Import from the same directory

# Initialize Pygame
pygame.init()

# Load the background image (replace with your actual image path)
background_image = pygame.image.load("C:/Users/soohu/OneDrive/Desktop/kingsfall.webp")

# Get the original width and height of the image
image_width = background_image.get_width()
image_height = background_image.get_height()

# Set the display mode to include borders and allow resizing, with a minimized start
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # Start minimized
pygame.display.set_caption("King's Fall")

# Function to maintain aspect ratio
def maintain_aspect_ratio(window_width, window_height, image_width, image_height):
    aspect_ratio = image_width / image_height
    if window_width / window_height > aspect_ratio:
        new_width = int(window_height * aspect_ratio)
        new_height = window_height
    else:
        new_width = window_width
        new_height = int(window_width / aspect_ratio)
    return new_width, new_height

# Function to constrain the window size to the image size when maximizing
def limit_maximized_size(window_width, window_height):
    if window_width > image_width:
        window_width = image_width
    if window_height > image_height:
        window_height = image_height
    return window_width, window_height

# Initial scaling of the background image
new_width, new_height = maintain_aspect_ratio(image_width, image_height, image_width, image_height)
scaled_background = pygame.transform.scale(background_image, (new_width, new_height))

# Define the exact button positions and sizes to perfectly overlap the Play and Rules buttons
play_button_rect = pygame.Rect(290, 440, 380, 100)  # Adjust to perfectly overlap the Play button
rules_button_rect = pygame.Rect(290, 560, 380, 100)  # Adjust to perfectly overlap the Rules button

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse click on buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Check if the Play button is clicked
            if play_button_rect.collidepoint(mouse_pos):
                print("Play button clicked!")
                run_chessboard()  # Call the chessboard screen

            # Check if the Rules button is clicked
            if rules_button_rect.collidepoint(mouse_pos):
                print("Rules button clicked!")
                run_rules()  # Call the rules screen

        # Detect if the window has been resized or maximized
        if event.type == pygame.VIDEORESIZE:
            window_width, window_height = event.w, event.h

            # Limit the window size to the image size when maximized
            window_width, window_height = limit_maximized_size(window_width, window_height)

            # Maintain aspect ratio during resizing
            new_width, new_height = maintain_aspect_ratio(window_width, window_height, image_width, image_height)
            screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

            # Scale the background image while maintaining aspect ratio
            scaled_background = pygame.transform.scale(background_image, (new_width, new_height))

    # Draw the scaled background image
    screen.fill((0, 0, 0))  # Fill the screen with black (for padding)
    screen.blit(scaled_background, (0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()
