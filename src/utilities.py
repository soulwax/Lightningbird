import pygame

def scale_surface(surface, scale_factor):
    return pygame.transform.scale(surface, (int(surface.get_width() * scale_factor), int(surface.get_height() * scale_factor)))
