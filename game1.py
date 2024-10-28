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
level1_completed = False  # New variable to track Level 1 completion

# Helper Function to Display Text
def display_text(text, x, y, color=WHITE, font_size=36):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to Handle the Different Screens
def display_screen():
    screen.fill(BLACK)  # Fill the background with black

    if current_level == 1:
        if not level1_completed:
            # Display instructions for Level 1
            display_text("Level 1: Phishing Detection", WIDTH // 2 - 150, HEIGHT // 2 - 100)
            display_text("Press 'P' for Phishing or 'S' for Safe", WIDTH // 2 - 200, HEIGHT // 2)
            display_text("Email: 'Your account is compromised, click here!'", WIDTH // 2 - 250, HEIGHT // 2 + 50)
        else:
            # Display level complete message if Level 1 is done
            display_text("Level 1 Complete! Press SPACE to continue.", WIDTH // 2 - 200, HEIGHT // 2)
    elif current_level == 2:
        display_text("Level 2: Malware Maze", WIDTH // 2 - 150, HEIGHT // 2 - 50)
    
    # Display score and lives
    display_text(f"Score: {score}", 10, 10, GREEN)
    display_text(f"Lives: {lives}", WIDTH - 100, 10, RED)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for keypress events
        elif event.type == pygame.KEYDOWN:
            # Check for level-specific interactions
            if current_level == 1 and not level1_completed:
                if event.key == pygame.K_p:  # P for "Phishing"
                    score += 10  # Award points for correct identification
                    level1_completed = True  # Mark level as completed
                elif event.key == pygame.K_s:  # S for "Safe"
                    lives -= 1  # Deduct a life for incorrect answer

            # Move to the next level when SPACE is pressed if level is completed
            elif event.key == pygame.K_SPACE and level1_completed:
                current_level += 1
                level1_completed = False  # Reset for next level if needed

    # Display the current screen based on the level
    display_screen()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)  # 30 frames per second


