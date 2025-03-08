from pygame import font

class Text(object):
    def __init__(self, textFont, size, message, color, xpos=None, ypos=None, center=False, screen_width=800):
        self.font = font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect()

        if center:
            self.rect.center = (screen_width // 2, ypos)
        else:
            self.rect.topleft = (xpos, ypos)

    def draw(self, surface):
        surface.blit(self.surface, self.rect)
