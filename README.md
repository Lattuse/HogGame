# HogGame - 2D Shooter Game

## 📌 Description
This is a simple 2D shooter game built with pygame. The player controls a character, shoots enemies, and earns points. If an enemy reaches the bottom of the screen or touches the player, the game ends.

## 🎮 Features

 - Character movement using arrow keys (←, →, ↑, ↓).

- Shooting with the left mouse button (LMB).

- Enemies spawn at the top and move downward.

- Score counter for defeated enemies.

- Background music from the file sabaton.mp3.

- Game loop with the ability to restart after losing.

## 🛠 Installation & Running the Game

🔹 1. Install Dependencies
Ensure you have Python and pygame installed. If not, install it using:

```
pip install pygame

```
🔹 2. Run the Game
Navigate to the project folder and execute:
```
python main.py

```
## 🎮 Controls

| Action | Key / Input                 |
| :-------- | :------------------------- |
| `Move Up` | ↑ (Up Arrow) |
| `Move Down` | ↓ (Down Arrow) |
| `Move Left` | ← (Left Arrow) |
| `Move Right` | → (Right Arrow) |
| `Shoot` | LMB (Left Mouse Button) |

## 📂 Project Structure

📂 HogGame FINAL/

│── 📂 all_sprites/         # Folder containing sprites

│   ├── 🎨 background.png   # Game background

│   ├── 🎨 hog.png   # Enemy Texture

│   ├── 📂 player_left/     # Left movement animation

│   ├── 📂 player_right/    # Right movement animation

│   ├── 📂 player_forward/  # Upward movement animation

│   ├── 📂 player_back/     # Downward movement animation

│── 🎵 audio/

│   ├── 🎶 sabaton.mp3      # Background music

│── 🎮 main.py              # Main game code

│── 📜 README.md            # Documentation

## 🔄 Gameplay
The player starts in the center of the screen.
Enemies spawn randomly at the top and move downward.
The player can shoot enemies by clicking the mouse.
If an enemy reaches the bottom or touches the player, it's Game Over.
The game can be restarted by clicking LMB.

![image](https://github.com/user-attachments/assets/8f67f38d-9d52-4512-beb2-106e06c84b4a)

![image](https://github.com/user-attachments/assets/401ef31e-1ed0-40f7-ac1a-b347fab20943)

