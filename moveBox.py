import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Tkinter App with Buttons and Animation")
root.geometry("500x400")

# Create a canvas where we can draw shapes
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=20)

# Create a rectangle (moving shape)
rect = canvas.create_rectangle(20, 20, 70, 70, fill="blue")

# Modify these global variables
is_moving = False
x_velocity = 0
y_velocity = 0

# New functions to control movement
def move_left():
    global x_velocity, y_velocity
    x_velocity = -2
    y_velocity = 0
    move_rectangle()

def move_right():
    global x_velocity, y_velocity
    x_velocity = 2
    y_velocity = 0
    move_rectangle()

def move_up():
    global x_velocity, y_velocity
    x_velocity = 0
    y_velocity = -2
    move_rectangle()

def move_down():
    global x_velocity, y_velocity
    x_velocity = 0
    y_velocity = 2
    move_rectangle()

def stop_movement():
    global x_velocity, y_velocity
    x_velocity = 0
    y_velocity = 0

# Modify the move_rectangle function
def move_rectangle():
    global x_velocity, y_velocity
    # Move the rectangle by the current velocity
    canvas.move(rect, x_velocity, y_velocity)

    # Get the current coordinates of the rectangle
    pos = canvas.coords(rect)

    # If the rectangle hits the boundary of the canvas, stop it
    if pos[2] >= 400 or pos[0] <= 0:  # Right and Left bounds
        x_velocity = 0
    if pos[3] >= 300 or pos[1] <= 0:  # Bottom and Top bounds
        y_velocity = 0

    # Schedule the next move
    canvas.after(20, move_rectangle)

# Function to handle button click event
def on_button_click():
    label.config(text="Button Clicked!", fg="green")

# Replace the existing buttons with new movement control buttons
left_button = tk.Button(root, text="Left", command=move_left)
left_button.pack(side=tk.LEFT, padx=5)

right_button = tk.Button(root, text="Right", command=move_right)
right_button.pack(side=tk.LEFT, padx=5)

up_button = tk.Button(root, text="Up", command=move_up)
up_button.pack(side=tk.LEFT, padx=5)

down_button = tk.Button(root, text="Down", command=move_down)
down_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(root, text="Stop", command=stop_movement)
stop_button.pack(side=tk.LEFT, padx=5)

# Add a label to display messages
label = tk.Label(root, text="Click the Button!", font=("Helvetica", 14))
label.pack(pady=10)

# Start the main loop
root.mainloop()
