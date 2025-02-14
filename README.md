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

## 🔨 Key Features & Technical Implementation

### ⏳ 1. Delta Time for Smooth Movement

#### Why is it important?
Delta time (dt) ensures that all objects in the game move at a consistent speed, regardless of the frame rate. This prevents issues where objects move too fast or too slow on different systems.

#### Implementation

```python
dt = clock.tick() / 1000  
player.move(dt)
for bullet in bullets:
    bullet.move(dt)
for enemy in enemies:
    enemy.move(dt)
```
- clock.tick(60) / 1000 ensures the game updates at 60 FPS, preventing speed inconsistencies.
- All movement calculations are multiplied by dt, so speed remains constant.

| Without Delta Time ❌ | With Delta Time ✅                 |
| :-------- | :------------------------- |
| 🏃‍♂️ Moves inconsistently | 🏃‍♂️ Moves smoothly |
| 🎮 Game speed depends on FPS | 🎮 Runs at the same speed on all devices |
| 🐌 Slow on laggy PCs, too fast on powerful ones | ⚡ Always stable |

### 🎯 2. Firing in Any Direction (Vector Math)

#### Why is it important?
Instead of shooting in fixed directions (e.g., up, down, left, right), we use vectors to calculate bullet trajectories dynamically. This allows the player to shoot toward the cursor position from any angle.

#### Implementation

```python
import math

class Bullet(Square):
    def __init__(self, pos, speed, height, width, color, targetx, targety):
        super().__init__(pos, height, width, color, speed)
        self.height = 10
        self.width = 10
        x, y = pos
        angle = math.atan2(targety - y, targetx - x)  
        self.dx = math.cos(angle) * speed  
        self.dy = math.sin(angle) * speed  
        self.x, self.y = x, y

    def move(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

```

- When the player clicks, the game captures the target position (targetx, targety).
- Using trigonometry (math.atan2), the game calculates the shooting angle.
- The bullet’s velocity (dx, dy) is determined using cosine and sine functions.
- The move() method updates the bullet’s position each frame.

### 🔄 3. Restarting the Game with a Total Score

#### Why is it important?
When the player loses, the game should:

1️⃣ Display the final score.  
2️⃣ Allow a restart without restarting the entire program.





#### Implementation
```python
if game_over:
    display_game_over_screen(final_score)
    if pygame.mouse.get_pressed()[0]:  # Left-click to restart
        reset_game()
```

- When the player loses, the score is displayed before resetting.
- Clicking the left mouse button instantly restarts the game.

```mermaid
    A[Start Game] --> B[Player is Playing];
    B --> C[Player Loses (Game Over)];
    C --> D[Display Final Score];
    D --> E[Player Clicks to Restart];
    E --> F[Reset All Variables (Except Total Score)];
    F --> A;
```
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

## 📂 Project Structure .

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

