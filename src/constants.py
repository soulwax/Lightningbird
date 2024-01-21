# Screen dimensions and game settings
SCREEN_WIDTH = 432  
SCREEN_HEIGHT = 768
SCALE = 3
BASE_HEIGHT = 600
FLAP_POWER = -10
PIPE_SPEED = 5
PIPE_INITIAL_SPEED = 5
FPS = 60
REINIT_SPRITESHEET = True
DEBUG = True


# Sprite names as constants
BACKGROUND_DAY = "background_day"
BACKGROUND_NIGHT = "background_night"
BIRD_SPRITES = ["bird_one", "bird_two", "bird_three"]
BASE = "base"
PIPE_SPRITES = ["red_pipe", "red_pipe2", "green_pipe_down", "green_pipe_up"]
GET_READY = "get_ready"
GAME_OVER = "game_over"
NUMBER_SPRITES = {str(i): f"{'zero' if i == 0 else str(i)}" for i in range(10)}
NUMBER_SPRITES_S = {str(i): f"{str(i)}_s" for i in range(10)}

# Alphabet sprites (A-Z, 0-9, and symbols)
ALPHABET_SPRITES = {
    letter: letter for letter in 
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!?'\"-+=/\\%()<>:;[]_"
}

# Adding more characters to ALPHABET_SPRITES
extra_chars = {
    '.': '.', ',': ',', '!': '!', '?': '?',
    '\'': '\'', '"': '"', '-': '-', '+': '+',
    '=': '=', '/': '/', '\\': '\\', 
    '%': '%', '(': '(', ')': ')', 
    '<': '<', '>': '>', ':': ':',
    ';': ';', '[': '[', ']': ']', '_': '_'
}
ALPHABET_SPRITES.update(extra_chars)

# Pipe and bird specific settings
PIPE_GAP = 200  # Gap between the upper and lower pipes
BIRD_START_X = 50
BIRD_START_Y = SCREEN_HEIGHT // 2
GRAVITY = 9.8 / FPS

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Other game constants
# Add any additional constants here, such as sound settings, difficulty levels, etc.
