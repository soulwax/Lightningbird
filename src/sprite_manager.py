import pygame
from constants import SCALE
from utilities import scale_surface

class SpriteManager:
    def __init__(self, sprite_sheet_path):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path)
        self.sprites = {}

    def load_sprite(self, name, rect):
        if name not in self.sprites:
            sprite = self.sprite_sheet.subsurface(rect)
            self.sprites[name] = scale_surface(sprite, SCALE)
        return self.sprites[name]

    def get_sprite(self, name):
        return self.sprites.get(name)

    def get_sprite_size(self, name):
        sprite = self.get_sprite(name)
        return sprite.get_width(), sprite.get_height() if sprite else (0, 0)
