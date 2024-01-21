import pygame
import sys
from bird import Bird
from pipe import Pipe
from sprite_manager import SpriteManager
from spritesheet_handler import SpriteSheetHandler
from constants import *
from utilities import scale_surface

class Game:
    def __init__(self):
        self.initialize_pygame()
        self.initialize_game_variables()
        self.sprite_sheet_handler = SpriteSheetHandler("res/sprites/sprite_sheet.png")
        if REINIT_SPRITESHEET:
            self.sprite_sheet_handler.load_metadata("res/sprites/sprite_sheet_metadata.json")
        self.bird = Bird(self.sprite_sheet_handler)
        self.pipe = Pipe(self.sprite_sheet_handler)
        # Other initialization code...

    def initialize_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE, pygame.RESIZABLE)
        pygame.display.set_caption("Lightningbird by Soulwax - Flappedy Fap v0.0.1")
        self.clock = pygame.time.Clock()

    def initialize_game_variables(self):
        self.score = 0
        self.game_started = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_started:
                        self.start_game()
                    else:
                        self.bird.flap()

    def start_game(self):
        self.game_started = True
        self.score = 0
        self.bird.reset_position()
        self.pipe.reset_position()

    def update_game(self):
        if self.game_started:
            self.bird.update_position()
            self.pipe.update_position()
            self.check_collisions()
            self.update_score()

    def check_collisions(self):
        if self.bird.check_collision(self.pipe.get_rects()):
            self.game_started = False  # Reset the game or implement a game over state

    def update_score(self):
    # Increment score when the bird passes a pipe
        if self.pipe.x + self.pipe.get_width() < self.bird.x and not self.pipe.score_counted:
            self.score += 1
            self.pipe.score_counted = True  # Mark this pipe as scored
            # Reset for the next pipe
            if self.pipe.x < 0:
                self.pipe.reset_position()
        

    def render_game(self):
        self.screen.fill(BLACK)  # Or use a background image
        self.pipe.render(self.screen)
        self.bird.render(self.screen)
        # Render other elements like score, etc.

    def main_loop(self):
        while True:
            self.handle_events()
            self.update_game()
            self.render_game()
            pygame.display.flip()
            self.clock.tick(60)

    def render_score(self):
        score_surface = self.font.render(str(self.score), True, WHITE)  # Using a default font for now
        score_x = SCREEN_WIDTH // 2 - score_surface.get_width() // 2
        score_y = 30  # 30 pixels from the top
        self.screen.blit(score_surface, (score_x, score_y))

    def check_collisions(self):
        if self.bird.check_collision(self.pipe.get_rects()) or self.bird.y > SCREEN_HEIGHT - BASE_HEIGHT:
            self.game_over()

    def game_over(self):
        self.game_started = False