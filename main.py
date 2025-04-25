from tkinter import *
from tkinter import ttk
import pygame
import os

WHITE = "#FFFFFF"
GREEN = "#90EE90"
YELLOW = "#FFDA00"
RED = "#7d1211"
BLUE = "#ADD8E6"

# Pygame mixer
pygame.mixer.init()
click_sound = pygame.mixer.Sound("assets/click.mp3")
bg_image_sound = pygame.mixer.Sound("assets/woosh.mp3")

# Functions
def on_button_click():
    click_sound.play()

def slide_in_image(step=0):
    if step == 0:
        bg_image_sound.play()
    if step <= 20:
        rps_label.place(x=x_position, y=y_position - 100 + step * 5)
        screen.after(15, lambda: slide_in_image(step + 1))

# Screen
screen = Tk()
screen.title("Rock, Paper, Scissors")
screen.geometry('800x600')
screen.resizable(width=False, height=False)
screen.configure(bg=BLUE)

# Icon
icon_path = os.path.join("assets", "icon.png")
icon_image = PhotoImage(file=icon_path)
screen.iconphoto(False, icon_image)

# Background Image
rps_path = os.path.join("assets", "rock-paper-scissors.png")
rps_image = PhotoImage(file=rps_path)
rps_label = Label(screen, image=rps_image, bg=BLUE)
rps_label.image = rps_image

window_width = 800
window_height = 600
image_width = rps_image.width()
image_height = rps_image.height()

x_position = (window_width - image_width) // 2
y_position = (window_height - image_height) // 2

rps_label.place(x=x_position, y=y_position)
slide_in_image()

# Row and Column setup for Grid
screen.columnconfigure(0, weight=1)
screen.columnconfigure(1, weight=1)
screen.columnconfigure(2, weight=1)

screen.rowconfigure(0, weight=0)
screen.rowconfigure(1, weight=1)
screen.rowconfigure(2, weight=0)


# Welcome Text
welcome = Label(screen, text="Welcome to Rock, Paper, Scissors", font=("Helvetica", 18, "bold"), bg=BLUE, anchor="center")
welcome.grid(row=0, column=0, columnspan=3, pady=5, sticky="ew")

# Frame to hold the buttons together (can be organzied using Pack, and only the Frame is added to grid)
button_frame = Frame(screen, bg=BLUE)
button_frame.grid(row=2, column=0, sticky="w", padx=0)

# Buttons
bo1 = ttk.Button(button_frame, text="Best of 1", width=20, command=on_button_click)
bo1.pack(anchor="w", fill="x")
bo3 = ttk.Button(button_frame, text="Best of 3", width=20)
bo3.pack(anchor="w", fill="x")
bo5 = ttk.Button(button_frame, text="Best of 5", width=20)
bo5.pack(anchor="w", fill="x")

screen.mainloop()



