import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Snake Game")
root.geometry("500x550")  # Increased height to accommodate buttons

# Create the canvas
canvas = tk.Canvas(root, width=500, height=500, bg="black")
canvas.pack()

# Snake properties
snake_size = 20  # Size of each square segment
snake_speed = 100  # Speed of the snake (in ms)

# Create the initial snake body (a list of rectangle IDs)
snake_body = [canvas.create_rectangle(100, 100, 100 + snake_size, 100 + snake_size, fill="green")]

# Initial direction of the snake
snake_direction = "Right"

# Game state
is_game_running = False
food = None

# Function to create food
def create_food():
    global food
    x = random.randint(0, 24) * snake_size
    y = random.randint(0, 24) * snake_size
    food = canvas.create_rectangle(x, y, x + snake_size, y + snake_size, fill="red")

# Function to update the snake's position
def move_snake():
    global is_game_running, food
    if not is_game_running:
        return

    head_coords = canvas.coords(snake_body[0])  # Get the current position of the head

    # Determine the new position of the snake's head
    if snake_direction == "Left":
        new_coords = [head_coords[0] - snake_size, head_coords[1], head_coords[2] - snake_size, head_coords[3]]
    elif snake_direction == "Right":
        new_coords = [head_coords[0] + snake_size, head_coords[1], head_coords[2] + snake_size, head_coords[3]]
    elif snake_direction == "Up":
        new_coords = [head_coords[0], head_coords[1] - snake_size, head_coords[2], head_coords[3] - snake_size]
    elif snake_direction == "Down":
        new_coords = [head_coords[0], head_coords[1] + snake_size, head_coords[2], head_coords[3] + snake_size]

    # Check if the snake has hit the boundary
    if (new_coords[0] < 0 or new_coords[2] > 500 or 
        new_coords[1] < 0 or new_coords[3] > 500):
        stop_game()
        return

    # Move the snake's head (create a new head and remove the last segment)
    new_head = canvas.create_rectangle(*new_coords, fill="green")
    snake_body.insert(0, new_head)  # Insert new head at the front of the snake

    # Check for collision with food
    if canvas.coords(new_head) == canvas.coords(food):
        # Eat food
        canvas.delete(food)
        create_food()
    else:
        # Remove tail
        old_segment = snake_body.pop()  # Remove the last segment
        canvas.delete(old_segment)  # Delete the last segment from the canvas

    # Schedule the next move
    root.after(snake_speed, move_snake)

# Function to change the snake's direction based on key presses
def change_direction(event):
    global snake_direction
    key = event.keysym
    # Prevent the snake from reversing direction
    if key == "Left" and snake_direction != "Right":
        snake_direction = "Left"
    elif key == "Right" and snake_direction != "Left":
        snake_direction = "Right"
    elif key == "Up" and snake_direction != "Down":
        snake_direction = "Up"
    elif key == "Down" and snake_direction != "Up":
        snake_direction = "Down"

# Function to start the game
def start_game():
    global is_game_running, food
    if not is_game_running:
        is_game_running = True
        if food is None:
            create_food()
        move_snake()

# Function to stop the game
def stop_game():
    global is_game_running
    is_game_running = False

# Bind the arrow keys to the change_direction function
root.bind("<KeyPress-Left>", change_direction)
root.bind("<KeyPress-Right>", change_direction)
root.bind("<KeyPress-Up>", change_direction)
root.bind("<KeyPress-Down>", change_direction)

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=10)

# Create start and stop buttons
start_button = tk.Button(button_frame, text="Start", command=start_game)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(button_frame, text="Stop", command=stop_game)
stop_button.pack(side=tk.LEFT, padx=5)

# Start moving the snake
move_snake()

# Start the Tkinter event loop
root.mainloop()