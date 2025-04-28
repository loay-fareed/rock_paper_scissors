import tkinter as tk
from tkinter import ttk
import os
from constants import BLUE, BASE_PATH

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Set up background image
        self.setup_background()


        # Set up widgets
        self.setup_widgets()


    def setup_background(self):
        self.configure(bg=BLUE, width=800, height=600)

        self.canvas = tk.Canvas(self, width=800, height=600, bg=BLUE, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.rps_path = os.path.join(BASE_PATH, "assets", "rock-paper-scissors.png")
        self.rps_image = tk.PhotoImage(file=self.rps_path)

        self.image_id = self.canvas.create_image(400, -self.rps_image.height()//2, image=self.rps_image)

        self.slide_in_image()


    def setup_widgets(self):
        # Welcome Text
        welcome_text = self.canvas.create_text(400, 20, text="Welcome to Rock, Paper, Scissors", font=("Helvetica", 18, "bold"), fill="black")

        # Buttons
        bo1 = ttk.Button(self, text="Best of 1", width=20, command=lambda: self.set_rules_and_go("bo1"))
        bo1.place(x=0, y=520)
        bo3 = ttk.Button(self, text="Best of 3", width=20, command=lambda: self.set_rules_and_go("bo3"))
        bo3.place(x=0, y=540)
        bo5 = ttk.Button(self, text="Best of 5", width=20, command=lambda: self.set_rules_and_go("bo5"))
        bo5.place(x=0, y=560)

    def slide_in_image(self, step=0):
        if step == 0:
            self.controller.sound_manager.play_sound("woosh")

        total_steps = 30

        if step <= total_steps:
            start_y = -self.rps_image.height()//2
            final_y = 300

            distance = final_y - start_y
            new_y = start_y + (distance * (step / total_steps))

            self.canvas.coords(self.image_id, 400, new_y)

            self.after(15, lambda: self.slide_in_image(step + 1))

    def set_rules_and_go(self, ruleset):
        self.controller.sound_manager.play_sound("click")
        self.controller.ruleset = ruleset
        self.controller.show_frame("GameplayPage")
