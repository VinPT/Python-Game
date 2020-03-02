# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
import arcade
import tkinter as tk

root = tk.Tk()

# Constants
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
SCREEN_TITLE = "Welcome to Python Game"
RADIUS = 150

# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.BLACK)

# Clear the screen and start drawing
arcade.start_render()

# Draw a blue circle
arcade.draw_circle_filled(
    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE
)

# Finish drawing
arcade.finish_render()

# Display everything
arcade.run()