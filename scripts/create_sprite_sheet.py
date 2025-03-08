import os
import math
from PIL import Image

def create_sprite_sheet(input_dir, output_file="spritesheet.png", sprite_size=None):
    # Recursively find all PNG files, grouped by parent directory
    animations = {}
    for root, _, files in os.walk(input_dir):
        png_files = sorted([os.path.join(root, f) for f in files if f.endswith(".png")])
        if png_files:
            animations[root] = png_files  # Group by directory

    if not animations:
        print("No PNG files found in the directory or its subdirectories.")
        return

    # Determine the max number of frames in any animation
    max_frames = max(len(files) for files in animations.values())

    # Load images and determine sprite size
    loaded_animations = {}
    for folder, files in animations.items():
        images = [Image.open(f) for f in files]
        if sprite_size is None:
            sprite_size = images[0].size  # Use the first image size if not specified
        images = [img.resize(sprite_size) for img in images]

        # Pad with blank frames if needed
        while len(images) < max_frames:
            images.append(Image.new("RGBA", sprite_size, (0, 0, 0, 0)))  # Transparent blank frame

        loaded_animations[folder] = images

    # Determine sheet size (rows = number of animations, columns = max frames per animation)
    num_animations = len(loaded_animations)
    sprite_sheet_width = max_frames * sprite_size[0]
    sprite_sheet_height = num_animations * sprite_size[1]
    sprite_sheet = Image.new("RGBA", (sprite_sheet_width, sprite_sheet_height))

    # Paste each animation's frames into the sheet row by row
    for row_idx, (folder, images) in enumerate(loaded_animations.items()):
        for col_idx, img in enumerate(images):
            x = col_idx * sprite_size[0]
            y = row_idx * sprite_size[1]
            sprite_sheet.paste(img, (x, y))

    # Save the sprite sheet
    sprite_sheet.save(output_file)
    print(f"Sprite sheet saved as {output_file}")

# Example usage
create_sprite_sheet("src/coral_defense/assets/sprites/crab")
