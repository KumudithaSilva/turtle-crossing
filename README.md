# 🐢🚗 Turtle Crossing Game

Turtle Crossing is a structured arcade-style game developed using Python’s standard `turtle` graphics module. This project serves as an academic demonstration of foundational programming concepts including object-oriented programming (OOP), real-time input handling, collision detection, and dynamic difficulty scaling—all implemented using Python's built-in libraries.

In this simulation, the user controls a turtle character that must navigate a traffic-heavy roadway. With each successful crossing to the top of the screen, the player levels up, which increases the game's difficulty by accelerating the speed of incoming vehicles. A single collision results in the end of the game, reinforcing reflex-based interaction and decision-making.

This project is designed for students, educators, and entry-level developers seeking to apply software design principles in a graphical, interactive environment.

---

## 🎯 Objective

The goal of the game is to guide the turtle from the bottom to the top of the screen while avoiding collisions with cars that traverse horizontally across the field. Each successful crossing results in:

- A level increase
- An increase in vehicle speed
- An updated scoreboard display

This progressive difficulty system encourages precise timing and rapid decision making.

---

## 🌟 Development Milestones

The project was developed incrementally to reflect best practices in modular software engineering. Key milestones are outlined below:

| Step | Feature                                  | Status |
|------|------------------------------------------|--------|
| 1    | Implement player (turtle) with movement  | ✅     |
| 2    | Generate randomized vehicles across lanes| ✅     |
| 3    | Animate vehicles moving leftward         | ✅     |
| 4    | Detect collisions between turtle and cars| ✅     |
| 5    | Implement level-up system and scaling    | ✅     |
| 6    | Design scoreboard with live updates      | ✅     |

---

## 🎨 Gameplay  Output

Below are sample outputs of Turtle crossing Game:

<img width="400" alt="pong_game" src="https://github.com/user-attachments/assets/ce5a71f7-2d7e-4ea4-88c6-01bac6725b93"/>

---

## 🐢 Player Class

The `Player` class encapsulates all functionality related to the turtle avatar.

### 🔹 Responsibilities:
- Move upward using the `↑` Arrow key.
- Move downward using the `↓` Arrow key.
- Reset to starting position after a successful crossing.
- Respond to collisions by triggering game-over state.

---

## 🚗 CarManager Class

The `CarManager` class manages all logic for vehicle generation and animation.

### 🔹 Responsibilities:
- Randomly generate car objects from the right boundary of the screen.
- Move cars horizontally across the screen at level-dependent speeds.
- Remove off-screen vehicles to optimize performance.

---

## 🧠 Collision Detection

Collision handling occurs during each iteration of the main game loop. The turtle's position is continuously compared to all active cars:

```python
for car in car_manager.all_cars:
    if player.distance(car) < 25:
        game_is_on = False
        scoreboard.game_over()
```

---

## 📈 Level-Up & Scoreboard

The `Scoreboard` class is responsible for tracking and displaying the player's current level, and for handling the game-over display logic.

### 🔹 Key Features:
- Increments the level each time the turtle successfully reaches the top.
- Dynamically increases the car movement speed with each level.
- Displays a “Game Over” message upon collision with a car.

```python
if player.ycor() > 280:
    player.reset_position()
    car_manager.increase_speed()
    scoreboard.level_up()
```
---

## 📁 Project Structure

```text
📁 turtle-crossing/
│
├── main.py           # Main game loop and input bindings
├── player.py         # Logic for player avatar behavior
├── car_manager.py    # Vehicle creation, animation, and removal
├── scoreboard.py     # Level tracking and game-over display
