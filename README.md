# Lightning Bird

This README will guide you hopefully lmao through setting up the project on your local machine.

## Table of Contents

- [Lightning Bird](#lightning-bird)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Windows (Using Powershell)](#windows-using-powershell)
    - [Linux / Mac](#linux--mac)
  - [Usage](#usage)
  - [How Lightningbird Works](#how-lightningbird-works)
    - [Initialization](#initialization)
    - [Image Scaling](#image-scaling)
    - [Loading Sprites](#loading-sprites)
    - [Main Game Loop](#main-game-loop)
    - [How to Run](#how-to-run)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Prerequisites

- Miniconda3

## Installation

### Windows (Using Powershell)

1. **Install Miniconda3**:
   - Download Miniconda3 from the [official website](https://docs.conda.io/en/latest/miniconda.html).
   - Run the installer and follow the on-screen instructions.

2. **Set up a virtual environment**:

   ```powershell
   conda create --name lightning_env python=3.11.5
   ```

3. **Activate the virtual environment**:

   ```powershell
   conda activate lightning_env
   ```

4. **Navigate to the project directory**:

   ```powershell
   cd path\to\LightningBird
   ```

5. **Install the required packages**:

   ```powershell
   pip install -r requirements.txt
   ```

### Linux / Mac

1. **Install Miniconda3**:

   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh
   ```

2. **Set up a virtual environment**:

   ```bash
   conda create --name lightning_env python=3.10
   ```

3. **Activate the virtual environment**:

   ```bash
   conda activate lightning_env
   ```

4. **Navigate to the project directory**:

   ```bash
   cd path/to/LightningBird
   ```

5. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

After setting up, you can run the project using:

```bash
python src/main.py
```

---

## How Lightningbird Works

### Initialization

1. **Pygame Initialization**: The program starts by initializing the Pygame library.
2. **Display Setup**: A display window is set up with the specified width and height. The window is also set to be resizable.
3. **Caption**: The window's caption is set to "Lightningbird by Soulwax - Flappedy Fap v0.0.1".

### Image Scaling

The program provides a function `scale_surface` to scale any given surface (like an image) by a specified scale factor. This is particularly useful for adjusting the size of sprites based on the desired scale factor.

### Loading Sprites

1. **Paths**: The program specifies paths for sprites, constants, window icons, and sprite sheets.
2. **Loading Images**: The game icon and the sprite sheet are loaded into the program.
3. **Sprite Sheet Scaling**: The sprite sheet is scaled based on the `SCALE` factor.
4. **SpriteSheetHandler**: An instance of the `SpriteSheetHandler` class is created to handle sprite sheet operations.
5. **Extracting Sprites**: Specific sprites are extracted from the sprite sheet using the `spritesheet_handler.get_sprite` method. These sprites include the day and night backgrounds, and various bird sprites.
6. **Metadata Handling**: If the `REINIT_SPRITESHEET` flag is set to `True`, the program saves the metadata of the sprite sheet. Otherwise, it loads the existing metadata. If the `DEBUG` flag is set to `True`, the metadata is printed.

### Main Game Loop

1. **Event Handling**: The program continuously checks for events. If the `QUIT` event is detected (like closing the window), the program exits.
2. **Drawing**: The screen is filled with a black color, and then the background and bird sprites are drawn/blitted onto the screen.
3. **Display Update**: The display is updated to reflect the drawn sprites.
4. **Frame Rate**: The program runs at a specified frames per second (FPS) rate, ensuring smooth animation.

---

### How to Run

To run the program, simply execute the `main.py` script within the `src` folder. E.g. `python src\main.py` The game window will open, displaying the game.

---

This section provides a high-level overview of the program's functionality. If there are specific parts of the code or features you'd like to delve deeper into, please let me know!

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT or none idk

## Contact

Dsicord lmao
