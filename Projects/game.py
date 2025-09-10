from tkinter import *
import random

# Constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100  # milliseconds
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.canvas = canvas

        # Initialize snake's starting coordinates
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Draw the snake squares
        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]

        self.food = self.canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR, tag="food"
        )


def next_turn():
    pass


def change_direction(new_direction):
    global direction
    direction = new_direction


def check_collisions():
    pass


def game_over():
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2,
                       text="GAME OVER", fill="red",
                       font=("consolas", 50))


# Main game window
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

# Score label
label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

# Game canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Center window on screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create game objects
snake = Snake(canvas)
food = Food(canvas)

# Start the game
window.mainloop()
