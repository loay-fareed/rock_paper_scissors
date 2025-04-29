import tkinter as tk
import os
from PIL import Image, ImageTk
from constants import BASE_PATH, BLUE
from game import GameLogic
import random
import time

class GameplayPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.setup_background()
        self.setup_scoreboard()
        self.setup_widgets()
        


# Setup Background
    def setup_background(self):
        self.configure(bg=BLUE, width=800, height=600)

        self.canvas = tk.Canvas(self, width=800, height=600, bg=BLUE, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

# Setup Widgets

    # RPS Buttons
    def setup_widgets(self):
        self.original_rock_path = os.path.join(BASE_PATH, "assets", "fist.png")
        self.original_rock_image = Image.open(self.original_rock_path)
        
        self.new_rock_image = self.original_rock_image.resize((100, 100))
        self.rock_image = ImageTk.PhotoImage(self.new_rock_image)

        self.rock_button = tk.Button(self, image=self.rock_image, command=lambda: self.on_button_click("rock", self.rock_button))
        self.rock_button.place(x=200, y=450)

        self.original_paper_path = os.path.join(BASE_PATH, "assets", "hand-paper.png")
        self.original_paper_image = Image.open(self.original_paper_path)
        
        self.new_paper_image = self.original_paper_image.resize((100, 100))
        self.paper_image = ImageTk.PhotoImage(self.new_paper_image)

        self.paper_button = tk.Button(self, image=self.paper_image, command=lambda: self.on_button_click("paper", self.paper_button))
        self.paper_button.place(x=350, y=450)

        self.original_scissors_path = os.path.join(BASE_PATH, "assets", "scissors.png")
        self.original_scissors_image = Image.open(self.original_scissors_path)
        
        self.new_scissors_image = self.original_scissors_image.resize((100, 100))
        self.scissors_image = ImageTk.PhotoImage(self.new_scissors_image)

        self.scissors_button = tk.Button(self, image=self.scissors_image, command=lambda: self.on_button_click("scissors", self.scissors_button))
        self.scissors_button.place(x=500, y=450)
        
        
    def setup_scoreboard(self):
    # Scoreboard
        self.game_logic = GameLogic()

        # Scoreboard labels
        self.player_score_label = tk.Label(self, text="Player: 0", font=("Helvetica", 18), bg=BLUE)
        self.player_score_label.place(x=30, y=100)

        self.computer_score_label = tk.Label(self, text="Computer: 0", font=("Helvetica", 18), bg=BLUE)
        self.computer_score_label.place(x=30, y=150)

        self.tie_score_label = tk.Label(self, text="Ties: 0", font=("Helvetica", 18), bg=BLUE)
        self.tie_score_label.place(x=30, y=200)

    def on_button_click(self, player_choice, button, step=0):
        if step == 0:
            self.controller.sound_manager.play_sound("click")

        total_steps = 150

        if step < total_steps:
            final_y = button.winfo_y() - 1
            button.place(x=button.winfo_x(), y=final_y)

            self.after(5, lambda: self.on_button_click(player_choice, button, step + 1))

        elif step == total_steps:
            computer_choice = random.choice(["rock", "paper", "scissors"])

            result = self.game_logic.determine_winner(player_choice, computer_choice)
            self.update_scoreboard()

            if self.game_logic.is_game_over():
                self.show_game_over()

            self.after(360, lambda: self.move_back(button))

    def move_back(self, button, step=0):
        total_steps = 150

        if step < total_steps:
            final_y = button.winfo_y() + 1
            button.place(x=button.winfo_x(), y=final_y)

            self.after(5, lambda: self.move_back(button, step + 1))


    
    
    def update_scoreboard(self):
        self.player_score_label.config(text=f"Player: {self.game_logic.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.game_logic.computer_score}")
        self.tie_score_label.config(text=f"Ties: {self.game_logic.ties}")

    def show_game_over(self):
        winner = self.game_logic.get_winner()
        winner_text = "You win!" if winner == "player" else "Computer wins!"

        popup = tk.Toplevel(self)
        popup.title("Game Over")
        popup.geometry("300x150")
        popup.configure(bg=BLUE)

        tk.Label(popup, text=winner_text, font=("Helvetica", 18), bg=BLUE).pack(pady=20)
        tk.Button(popup, text="OK", command=lambda: [popup.destroy(), self.reset_game()]).pack(pady=10)

    def reset_game(self):
        self.game_logic = GameLogic()
        self.update_scoreboard()
        self.controller.show_frame("WelcomePage")


    def move_forward(self, button, step=0):
        total_steps = 150

        if step <= total_steps:
            final_y = button.winfo_y() - 1
            button.place(x=button.winfo_x(), y=final_y)

            self.after(5, lambda: self.move_forward(button=button, step=step + 1))

    def move_back(self, button, step=0):
            total_steps = 150

            if step <= total_steps:
                final_y = button.winfo_y() + 1
                button.place(x=button.winfo_x(), y=final_y)

                self.after(5, lambda: self.move_back(button=button, step=step + 1))
    
    def refresh(self):
        self.game_logic.set_rules(self.controller.ruleset)

    
            

