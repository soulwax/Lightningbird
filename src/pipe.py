import pygame
from constants import PIPE_SPEED, SCREEN_WIDTH, PIPE_SPRITES as PIPES

class Pipe:
    def __init__(self, sprite_sheet_handler):
        self.sprite_sheet_handler = sprite_sheet_handler
        self.reset_position()
        self.score_counted = False

    def reset_position(self):
        self.x = SCREEN_WIDTH
        self.pipe_sprite_name = PIPES[0]  # Example, randomize as needed
        self.score_counted = False

    def update_position(self):
        self.x -= PIPE_SPEED

    def render(self, screen):
        pipe_sprite = self.sprite_sheet_handler.get_sprite_from_metadata(self.pipe_sprite_name)
        screen.blit(pipe_sprite, (self.x, 0))  # Modify y-coordinate as needed for pipe positioning

    def get_rects(self):
        pipe_sprite_size = self.sprite_sheet_handler.get_sprite_size(self.pipe_sprite_name)
        return [pygame.Rect(self.x, 0, *pipe_sprite_size)]  # Modify for multiple pipes or different positions

    def get_width(self):
        return self.sprite_sheet_handler.get_sprite_size(self.pipe_sprite_name)[0]