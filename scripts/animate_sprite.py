import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FRAME_RATE = 10  # Speed of animation (frames per second)

# Load sprite sheet
sprite_sheet = pygame.image.load("src/coral_defense/assets/sprites/crab.png")  # Change to your sprite sheet file

# Sprite settings
SPRITE_WIDTH = 18  # Change to match your sprite size
SPRITE_HEIGHT = 18
FRAMES_PER_ANIMATION = 5  # Adjust to your animation frame count
TOTAL_ANIMATIONS = 4  # How many rows of animations in your sheet?

# Extract frames from sprite sheet
def extract_frames(sprite_sheet, frames_per_animation, sprite_width, sprite_height):
    frames = []
    for row in range(TOTAL_ANIMATIONS):  # Each row is one animation
        row_frames = []
        for col in range(frames_per_animation):
            frame = sprite_sheet.subsurface(pygame.Rect(
                col * sprite_width,  # X position in sheet
                row * sprite_height,  # Y position in sheet (each row is a new animation)
                sprite_width,
                sprite_height
            ))
            row_frames.append(frame)
        frames.append(row_frames)  # Store frames per animation
    return frames

# Get extracted frames
animations = extract_frames(sprite_sheet, FRAMES_PER_ANIMATION, SPRITE_WIDTH, SPRITE_HEIGHT)

# Pygame setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Animation state
current_animation = 0  # Which row (e.g., walking, attacking)
frame_index = 0  # Which frame in the animation
animation_timer = 0  # Timer to control frame speed

running = True
while running:
    screen.fill((30, 30, 30))  # Clear screen with dark background

    # Event handling (quit game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation frame
    animation_timer += 1
    if animation_timer >= FRAME_RATE:
        animation_timer = 0
        frame_index = (frame_index + 1) % FRAMES_PER_ANIMATION  # Loop through frames

    # Draw current frame
    screen.blit(animations[current_animation][frame_index], (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Update display
    pygame.display.flip()
    clock.tick(60)  # Keep at 60 FPS

pygame.quit()
