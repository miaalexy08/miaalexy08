# Step 1: Basic Setup for the Game
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up game window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Sleuth: The Threat Within")

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up fonts
font = pygame.font.Font(None, 36)  # Default font with size 36

# Game Variables
current_level = 1
score = 0
lives = 3

# Helper Function to Display Text
def display_text(text, x, y, color=WHITE, font_size=36):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to Handle the Different Screens
def display_screen():
    screen.fill(BLACK)  # Fill the background with black

    if current_level == 1:
        display_text("Welcome to Cyber Sleuth!", WIDTH//2 - 150, HEIGHT//2 - 50)
        display_text("Press SPACE to Start Level 1", WIDTH//2 - 150, HEIGHT//2 + 10)
    elif current_level == 2:
        display_text("Level 2: Malware Maze", WIDTH//2 - 150, HEIGHT//2 - 50)
    # You can add more elif statements for each level's screen

    # Display score and lives
    display_text(f"Score: {score}", 10, 10, GREEN)
    display_text(f"Lives: {lives}", WIDTH - 100, 10, RED)

# Main Game Loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for keypress to move to next level or start game
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_level += 1  # Move to the next level when SPACE is pressed

    # Display the current screen based on the level
    display_screen()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)  # 30 frames per second

