from constants import *
import pygame

class Bird:
    def __init__(self, sprite_sheet_handler):
        self.sprite_sheet_handler = sprite_sheet_handler
        self.reset_position()

    def reset_position(self):
        self.x = BIRD_START_X
        self.y = BIRD_START_Y
        self.velocity = 0
        self.current_frame = 0

    def flap(self):
        self.velocity = FLAP_POWER

    def update_position(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.current_frame = (self.current_frame + 1) % len(BIRD_SPRITES)

    def render(self, screen):
        bird_sprite = self.sprite_sheet_handler.get_sprite_from_metadata(BIRD_SPRITES[self.current_frame])
        screen.blit(bird_sprite, (self.x, self.y))

    def check_collision(self, pipe_rects):
        bird_rect = pygame.Rect(self.x, self.y, *self.sprite_sheet_handler.get_sprite_size(BIRD_SPRITES[self.current_frame]))
        return any(bird_rect.colliderect(pipe_rect) for pipe_rect in pipe_rects)
