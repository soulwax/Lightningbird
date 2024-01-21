# spritesheet_handler.py

import pygame
import json

class SpriteSheetHandler:
    def __init__(self, sprite_sheet_path):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path)
        self.metadata = {}

    def get_sprite(self, x, y, width, height, name):
        """
        Extracts a sprite from the spritesheet and saves its metadata.
        """
        sprite = self.sprite_sheet.subsurface(pygame.Rect(x, y, width, height))
        self.metadata[name] = {
            'x': x,
            'y': y,
            'width': width,
            'height': height
        }
        return sprite

    def save_metadata(self, file_path):
        """
        Saves the metadata to a JSON file.
        """
        with open(file_path, 'w') as file:
            json.dump(self.metadata, file, indent=2)

    def load_metadata(self, file_path):
        """
        Loads the metadata from a JSON file.
        """
        with open(file_path, 'r') as file:
            self.metadata = json.load(file)

    def get_sprite_from_metadata(self, name):
        """
        Retrieves a sprite using its name from the metadata.
        """
        if name in self.metadata:
            data = self.metadata[name]
            return self.get_sprite(data['x'], data['y'], data['width'], data['height'], name)
        else:
            raise ValueError(f"No sprite with the name {name} found in metadata.")
    
    def get_sprite_size(self, name):
        """
        Returns the size of the sprite with the given name.
        """
        if name in self.metadata:
            data = self.metadata[name]
            return data['width'], data['height']
        else:
            raise ValueError(f"No sprite with the name {name} found in metadata.")