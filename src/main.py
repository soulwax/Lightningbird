import pygame
import sys
from constants import *
from spritesheet_handler import SpriteSheetHandler
from random import randint, seed
import random


# Initialize pygame
pygame.init()
seed(a=None, version=2)

# Setup local variables
score = 0
clock = pygame.time.Clock()
PIPE_SPEED = PIPE_INITIAL_SPEED
X_OFFSET = 0.0
x_pos = 0.0
tick_count = 0
bird_x = 10
bird_y = 0
flap_power = -10
score_duration_modifier = 0
random_pipe_height = 0
game_started = False
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE, pygame.RESIZABLE)
pygame.display.set_caption("Lightningbird by Soulwax - Flappedy Fap v0.0.1")

# Scale a given surface by a scale factor defined as SCALE in constants.py for pixel art
def scale_surface(surface, scale_factor):
    """Scale a given surface by a scale factor."""
    return pygame.transform.scale(surface, (surface.get_width() * scale_factor, surface.get_height() * scale_factor))

sprite_sheet_path = "res/sprites/sprite_sheet.png"
game_icon = pygame.image.load("res/sprites/icon_detailed.png")
sprite_sheet = scale_surface(pygame.image.load(sprite_sheet_path), SCALE)
spritesheet_handler = SpriteSheetHandler(sprite_sheet_path)

# Set the window icon
pygame.display.set_icon(game_icon)

if not REINIT_SPRITESHEET:
    spritesheet_handler.load_metadata("res/sprites/sprite_sheet_metadata.json")

# Dictionary to store all sprites
# How to access them: sprites["sprite_name"]
sprites = {
    "background_day": "0, 0, 144, 256",
    "background_night": "146, 0, 144, 256",
    "bird_one": "3, 491, 17, 12",
    "bird_two": "31, 491, 17, 12",
    "bird_three": "59, 491, 17, 12",
    "bird_blue": "87, 491, 17, 12",
    "base": "292, 0, 168, 56",
    "red_pipe": "0, 323, 26, 160",
    "red_pipe2": "28, 323, 26, 160",
    "green_pipe_down": "56, 323, 26, 160",
    "green_pipe_up": "84, 323, 26, 160",
    "get_ready": "295, 59, 92, 25",
    "game_over": "395, 59, 96, 21",
    "zero": "496, 60, 12, 18",
    "one": "346, 160, 12, 18",
    "two": "292, 160, 12, 18",
    "three": "306, 160, 12, 18",
    "four": "320, 160, 12, 18",
    "five": "334, 160, 12, 18",
    "six": "292, 184, 12, 18",
    "seven": "306, 184, 12, 18",
    "eight": "320, 184, 12, 18",
    "nine": "334, 184, 12, 18",
    "zero_s": "138, 323, 6, 7",
    "one_s": "138, 332, 6, 7",
    "two_s": "138, 349, 6, 7",
    "three_s": "138, 358, 6, 7",
    "four_s": "138, 375, 6, 7",
    "five_s": "138, 384, 6, 7",
    "six_s": "138, 401, 6, 7",
    "seven_s": "138, 410, 6, 7",
    "eight_s": "138, 427, 6, 7",
    "nine_s": "138, 436, 6, 7",
    'A': "148, 496, 8, 8",
    'B': "156, 496, 8, 8",
    'C': "164, 496, 8, 8",
    'D': "172, 496, 8, 8",
    'E': "180, 496, 8, 8",
    'F': "188, 496, 8, 8",
    'G': "196, 496, 8, 8",
    'H': "204, 496, 8, 8",
    'I': "212, 496, 8, 8",
    'J': "220, 496, 8, 8",
    'K': "228, 496, 8, 8",
    'L': "236, 496, 8, 8",
    'M': "244, 496, 8, 8",
    'N': "252, 496, 8, 8",
    'O': "260, 496, 8, 8",
    'P': "268, 496, 8, 8",
    'Q': "276, 496, 8, 8",
    'R': "284, 496, 8, 8",
    'S': "292, 496, 8, 8",
    'T': "300, 496, 8, 8",
    'U': "308, 496, 8, 8",
    'V': "316, 496, 8, 8",
    'W': "324, 496, 8, 8",
    'X': "332, 496, 8, 8",
    'Y': "340, 496, 8, 8",
    'Z': "348, 496, 8, 8",
    '0': "148, 504, 8, 8",
    '1': "156, 504, 8, 8",
    '2': "164, 504, 8, 8",
    '3': "172, 504, 8, 8",
    '4': "180, 504, 8, 8",
    '5': "188, 504, 8, 8",
    '6': "196, 504, 8, 8",
    '7': "204, 504, 8, 8",
    '8': "212, 504, 8, 8",
    '9': "220, 504, 8, 8",
    '.': "228, 504, 8, 8",
    ',': "236, 504, 8, 8",
    '!': "244, 504, 8, 8",
    '?': "252, 504, 8, 8",
    '\'': "260, 504, 8, 8",
    '"': "268, 504, 8, 8",
    '-': "276, 504, 8, 8",
    '+' : "284, 504, 8, 8",
    '=' : "292, 504, 8, 8",
    '/' : "300, 504, 8, 8",
    '\\' : "308, 504, 8, 8",
    '%': "316, 504, 8, 8",
    '(': "324, 504, 8, 8",
    ')': "332, 504, 8, 8",
    '<': "340, 504, 8, 8",
    '>': "348, 504, 8, 8",
    ':': "148, 504, 8, 8",
    ';': "156, 504, 8, 8",
    '[': "164, 504, 8, 8",
    ']': "172, 504, 8, 8",
    '_': "180, 504, 8, 8"
    # ... add more sprites
}


# Extract and scale sprites from the spritesheet
for sprite_name, coords in sprites.items():
    x, y, w, h = map(int, coords.split(","))
    sprites[sprite_name] = scale_surface(spritesheet_handler.get_sprite(x, y, w, h, sprite_name), SCALE)



# Collection of pipes 
pipes = [sprites['red_pipe'], sprites['red_pipe2'], sprites['green_pipe_down'], sprites['green_pipe_up']]
pipe_rects = [pipe.get_rect() for pipe in pipes]

# Create a dictionary to store the number sprites
number_sprites = {
    '0': sprites['zero'],
    '1': sprites['one'],
    '2': sprites['two'],
    '3': sprites['three'],
    '4': sprites['four'],
    '5': sprites['five'],
    '6': sprites['six'],
    '7': sprites['seven'],
    '8': sprites['eight'],
    '9': sprites['nine'],
}

number_sprites_s = {
    '0': sprites['zero_s'],
    '1': sprites['one_s'],
    '2': sprites['two_s'],
    '3': sprites['three_s'],
    '4': sprites['four_s'],
    '5': sprites['five_s'],
    '6': sprites['six_s'],
    '7': sprites['seven_s'],
    '8': sprites['eight_s'],
    '9': sprites['nine_s'],
}

# alphabet dictionary starting at 148,496, each 8x8, first row on x axis is A-Z, second row is a-z
alphabet_sprites = {
    'A': sprites['A'],
    'B': sprites['B'],
    'C': sprites['C'],
    'D': sprites['D'],
    'E': sprites['E'],
    'F': sprites['F'],
    'G': sprites['G'],
    'H': sprites['H'],
    'I': sprites['I'],
    'J': sprites['J'],
    'K': sprites['K'],
    'L': sprites['L'],
    'M': sprites['M'],
    'N': sprites['N'],
    'O': sprites['O'],
    'P': sprites['P'],
    'Q': sprites['Q'],
    'R': sprites['R'],
    'S': sprites['S'],
    'T': sprites['T'],
    'U': sprites['U'],
    'V': sprites['V'],
    'W': sprites['W'],
    'X': sprites['X'],
    'Y': sprites['Y'],
    'Z': sprites['Z'],
    '0': sprites['0'],
    '1': sprites['1'],
    '2': sprites['2'],
    '3': sprites['3'],
    '4': sprites['4'],
    '5': sprites['5'],
    '6': sprites['6'],
    '7': sprites['7'],
    '8': sprites['8'],
    '9': sprites['9'],
    '.': sprites['.'],
    ',': sprites[','],
    '!': sprites['!'],
    '?': sprites['?'],
    '\'': sprites['\''],
    '"': sprites['"'],
    '-': sprites['-'],
    '+': sprites['+'],
    '=': sprites['='],
    '/': sprites['/'],
    '\\': sprites['\\'],
    '%': sprites['%'],
    '(': sprites['('],
    ')': sprites[')'],
    '<': sprites['<'],
    '>': sprites['>'],
    ':': sprites[':'],
    ';': sprites[';'],
    '[': sprites['['],
    ']': sprites[']'],
    '_': sprites['_'],
}

# Extract the sprites from the spritesheet and save metadata if REINIT_SPRITESHEET is True
if REINIT_SPRITESHEET:
    # Save the metadata
    spritesheet_handler.save_metadata("res/sprites/sprite_sheet_metadata.json")

# Debug
if DEBUG:
    # Print the metadata
    for data in spritesheet_handler.metadata:
        print(data, spritesheet_handler.metadata[data])

# Before Game starts, show start game screen, with bird flapping at the center of the screen above the message
def show_start_game_screen(event):
    center_x = SCREEN_WIDTH // 2 - sprites['get_ready'].get_width() // 2
    center_y = SCREEN_HEIGHT // 2 - sprites['get_ready'].get_height() // 2

    screen.blit(sprites['get_ready'], (center_x, center_y))
    render_background()
    animate_bird(10, 375)
    render_base()
    pygame.display.flip()

def render_fps():
    fps = str(int(clock.get_fps()))
    fps_text = pygame.font.SysFont("Arial", 18).render(fps, True, (0, 0, 0))
    screen.blit(fps_text, (0, 0))

# Define a function to render the score
def render_score(score):
    # Convert score to 4-digit string
    score_str = str(score).zfill(4)

    # Calculate starting x-coordinate to center the score
    total_width = len(score_str) * 12 * SCALE  # 12 is the width of each sprite
    start_x = (SCREEN_WIDTH - total_width) // 2

    # Render each digit
    for i, digit in enumerate(score_str):
        screen.blit(number_sprites[digit], (start_x + i * 12 * SCALE, 10))  # 10 is a small padding from the top

# Bird animation
bird_sprites = [sprites['bird_one'], sprites['bird_two'], sprites['bird_three']]
current_frame = 0

def animate_bird(bird_x, bird_y):
    global current_frame
    bird_position = (bird_x, bird_y)
    screen.blit(bird_sprites[current_frame], bird_position)
    current_frame = (current_frame + 1) % len(bird_sprites)

# Collision detection
def check_collision(bird_rect):
    global score_duration_modifier
    # Check collision with ground
    if bird_rect.bottom > SCREEN_HEIGHT - sprites['base'].get_height():
        return True

    # Check collision with pipes
    pipe_rect = sprites['red_pipe'].get_rect(topleft=(SCREEN_WIDTH / 2 - sprites['red_pipe'].get_width() / 2 + x_pos + X_OFFSET, SCREEN_HEIGHT / 2 - random_pipe_height / 2))
    if bird_rect.colliderect(pipe_rect):
        return True

    return False

def initialize_game_variables():
    global random_pipe_height
    global bird_velocity
    global score
    global bird_y

    random_pipe_height = random.randint(-400, 100)
    bird_velocity = 0
    score = 0
    bird_y = SCREEN_HEIGHT // 2

def handle_events():
    global bird_velocity
    global game_started
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_started:
                    start()
                else:
                    bird_velocity = flap_power

def update_bird_position():
    global bird_velocity
    global bird_y

    bird_velocity += 9.8 / FPS
    bird_y += bird_velocity

def get_random_pipe():
    return pipes[randint(0, len(pipes) - 1)]


def update_pipe_pos_and_increment_score():
    global x_pos
    global random_pipe_height
    global score
    global score_duration_modifier
    # choose random pipe from pipes list

    x_pos -= PIPE_SPEED
    if x_pos < -sprites['red_pipe'].get_width() * SCALE:
        score += 1 + score_duration_modifier
        x_pos = SCREEN_WIDTH
        random_pipe_height = random.randint(-400, 500)

def calculate_score_duration_modifier():
    global score_duration_modifier
    global tick_count

    if tick_count % 100 == 0:
        score_duration_modifier += 1


def render_background():
    screen.fill(BLACK)
    screen.blit(sprites['background_day'], (0, 0))

def render_bird_related_elements():
    global tick_count
    global bird_y
    global bird_x
    global score
    global score_duration_modifier

    tick_count += 1
    bird_rect = bird_sprites[current_frame].get_rect(topleft=(bird_x, bird_y))
    if check_collision(bird_rect) and DEBUG:
        print("Collision detected, score reset to 0")
        score_duration_modifier = 0 # side effect programming, I hate it but it works for now
        score = 0

    render_score(score)
    animate_bird(bird_x, bird_y)

def render_pipe_elements():
    global x_pos

    pipe_sprite = sprites['red_pipe'] # TODO: randomize, double above and below randomly
    screen.blit(pipe_sprite, (SCREEN_WIDTH / 2 - pipe_sprite.get_width() / 2 + x_pos + X_OFFSET, SCREEN_HEIGHT / 2 - random_pipe_height / 2))

def render_base():
    base_x = 0
    base_y = SCREEN_HEIGHT - sprites['base'].get_height()
    screen.blit(sprites['base'], (base_x, base_y))

def draw_game_elements():
    render_background()
    render_bird_related_elements()
    render_pipe_elements()
    render_base()

def start():
    global tick_count
    global game_started
    game_started = True
    tick_count = 0

def main():
    global tick_count
    global bird_x
    global bird_y
    global bird_velocity
    global random_pipe_height
    global score
    global flap_power
    global game_started

    initialize_game_variables()

    while True:
        handle_events()
        if not game_started:
            game_started = show_start_game_screen(pygame.event.Event(pygame.KEYDOWN))
            continue
        update_bird_position()
        calculate_score_duration_modifier()
        update_pipe_pos_and_increment_score()
        draw_game_elements()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
