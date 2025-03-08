import pygame
from pygame import sprite, time


class Crab(sprite.Sprite):
    def __init__(self, sprite_sheet_path, frame_width, frame_height, num_frames, animation_speed=100):
        super().__init__()

        # Load the sprite sheet
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()

        # Extract animations (4 rows, each with num_frames)
        self.animations = self.load_crab_frames(frame_width, frame_height, num_frames)

        self.current_animation = 0  # Default animation (row 0)
        self.frame_index = 0
        self.animation_speed = animation_speed  # Milliseconds per frame
        self.last_update = time.get_ticks()

        # Set initial image and position
        self.image = self.animations[self.current_animation][self.frame_index]
        self.rect = self.image.get_rect(topleft=(300, 300))

    def update(self):
        """Handle animation and frame switching."""
        now = time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_animation])
            self.image = self.animations[self.current_animation][self.frame_index]

    def set_animation(self, animation_index):
        """Switch to a different animation row."""
        if 0 <= animation_index < len(self.animations):
            self.current_animation = animation_index
            self.frame_index = 0  # Reset to the first frame

    def load_crab_frames(self, frame_width, frame_height, num_frames):
        """Extract frames from each animation row."""
        animations = []
        for row in range(4):  # 4 animation types (rows)
            frames = [
                self.sprite_sheet.subsurface(
                    pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height))
                for col in range(num_frames)
            ]
            animations.append(frames)
        return animations
