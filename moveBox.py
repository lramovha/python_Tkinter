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

# Global variables to control the animation
is_moving = False
x_velocity = 2  # Speed of movement along the x-axis
y_velocity = 1  # Speed of movement along the y-axis

# Function to start the animation
def start_animation():
    global is_moving
    is_moving = True
    move_rectangle()

# Function to stop the animation
def stop_animation():
    global is_moving
    is_moving = False

# Function to move the rectangle (animation)
def move_rectangle():
    global is_moving, x_velocity, y_velocity
    if is_moving:
        # Move the rectangle by a small increment
        canvas.move(rect, x_velocity, y_velocity)

        # Get the current coordinates of the rectangle
        pos = canvas.coords(rect)

        # If the rectangle hits the boundary of the canvas, reverse direction
        if pos[2] >= 400 or pos[0] <= 0:  # Right and Left bounds
            x_velocity = -x_velocity
        if pos[3] >= 300 or pos[1] <= 0:  # Bottom and Top bounds
            y_velocity = -y_velocity

        # Schedule the next move
        canvas.after(20, move_rectangle)  # 20ms delay for smooth animation

# Function to handle button click event
def on_button_click():
    label.config(text="Button Clicked!", fg="green")

# Add buttons to control animation
start_button = tk.Button(root, text="Start Animation", command=start_animation)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Animation", command=stop_animation)
stop_button.pack(pady=10)

# Add a label to display messages
label = tk.Label(root, text="Click the Button!", font=("Helvetica", 14))
label.pack(pady=10)

# Add another button that triggers an event handler
click_button = tk.Button(root, text="Click Me", command=on_button_click)
click_button.pack(pady=10)

# Start the main loop
root.mainloop()
