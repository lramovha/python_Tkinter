import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the title and size
root.title("Grid Layout Example")
root.geometry("400x300")

# Create and place labels and entry widgets using grid layout
tk.Label(root, text="First Name").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Last Name").grid(row=1, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column=1, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Function to display the input
def display_input():
    first_name = entry1.get()
    last_name = entry2.get()
    print(f"Full Name: {first_name} {last_name}")

# Button to trigger display
tk.Button(root, text="Submit", command=display_input).grid(row=2, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()
