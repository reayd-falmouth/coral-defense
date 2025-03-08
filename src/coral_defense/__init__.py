import os
import sys

from pygame import display, image

# ✅ Define ASSETS_DIR for both Pygbag and PyInstaller compatibility
def get_assets_dir():
    """Returns the correct path for assets, whether running as a script or PyInstaller package."""
    if getattr(
        sys, "frozen", False
    ):  # PyInstaller sets `sys.frozen` when running from .exe
        return os.path.join(sys._MEIPASS, "assets")
    else:
        return os.path.join(os.path.dirname(__file__), "assets")


BASE_PATH = get_assets_dir()

FONT_PATH = BASE_PATH + "/fonts/"
IMAGE_PATH = BASE_PATH + "/img/"
SOUND_PATH = BASE_PATH + "/sounds/"

# Colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

SCREEN = display.set_mode((800, 600))
FONT = FONT_PATH + "space_invaders.ttf"
IMG_NAMES = [
    "ship",
    "mystery",
    "enemy1_1",
    "enemy1_2",
    "enemy2_1",
    "enemy2_2",
    "enemy3_1",
    "enemy3_2",
    "explosionblue",
    "explosiongreen",
    "explosionpurple",
    "laser",
    "enemylaser",
]
IMAGES = {
    name: image.load(IMAGE_PATH + "{}.png".format(name)).convert_alpha()
    for name in IMG_NAMES
}

BLOCKERS_POSITION = 450
ENEMY_DEFAULT_POSITION = 65  # Initial value for a new game
ENEMY_MOVE_DOWN = 35
