import tkinter as tk
import os
from PIL import Image, ImageTk
from constants import BASE_PATH, BLUE
from game import GameLogic
import random

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

        self.cpu_rock_label = tk.Label(self, image=self.rock_image)
        self.cpu_rock_label.place(x=200, y=50)

        self.original_paper_path = os.path.join(BASE_PATH, "assets", "hand-paper.png")
        self.original_paper_image = Image.open(self.original_paper_path)
        
        self.new_paper_image = self.original_paper_image.resize((100, 100))
        self.paper_image = ImageTk.PhotoImage(self.new_paper_image)

        self.paper_button = tk.Button(self, image=self.paper_image, command=lambda: self.on_button_click("paper", self.paper_button))
        self.paper_button.place(x=350, y=450)

        self.cpu_paper_label = tk.Label(self, image=self.paper_image)
        self.cpu_paper_label.place(x=350, y=50)

        self.original_scissors_path = os.path.join(BASE_PATH, "assets", "scissors.png")
        self.original_scissors_image = Image.open(self.original_scissors_path)
        
        self.new_scissors_image = self.original_scissors_image.resize((100, 100))
        self.scissors_image = ImageTk.PhotoImage(self.new_scissors_image)

        self.scissors_button = tk.Button(self, image=self.scissors_image, command=lambda: self.on_button_click("scissors", self.scissors_button))
        self.scissors_button.place(x=500, y=450)

        self.cpu_scissors_label = tk.Label(self, image=self.scissors_image)
        self.cpu_scissors_label.place(x=500, y=50)

        # Misc. Labels
        self.player_label = tk.Label(text="Player")

        
        
    def setup_scoreboard(self):
    # Scoreboard
        self.game_logic = GameLogic()

        # Scoreboard labels
        self.player_score_label = tk.Label(self, text=f"{self.controller.player_name}: 0", font=("Helvetica", 18), bg=BLUE)
        self.player_score_label.place(x=30, y=100)

        self.computer_score_label = tk.Label(self, text="Computer: 0", font=("Helvetica", 18), bg=BLUE)
        self.computer_score_label.place(x=30, y=150)

        self.tie_score_label = tk.Label(self, text="Ties: 0", font=("Helvetica", 18), bg=BLUE)
        self.tie_score_label.place(x=30, y=200)

    def on_button_click(self, player_choice, button, step=0, computer_choice=None):
        if computer_choice is None:
            computer_choice = random.choice(["rock", "paper", "scissors"])
        if step == 0:
            self.controller.sound_manager.play_sound("click")
            
        if computer_choice == "rock":
            label = self.cpu_rock_label
        elif computer_choice == "paper":
            label = self.cpu_paper_label
        else:
            label = self.cpu_scissors_label

        total_steps = 150

        if step < total_steps:
            final_y = button.winfo_y() - 1
            button.place(x=button.winfo_x(), y=final_y)
            cpu_final_y = label.winfo_y() + 1
            label.place(x=label.winfo_x(), y= cpu_final_y)
            self.after(5, lambda: self.on_button_click(player_choice, button, step + 1, computer_choice))

        elif step == total_steps:
           
            result = self.game_logic.determine_winner(player_choice, computer_choice)
            self.update_scoreboard()

            self.after(1000, lambda: [self.move_back(button), self.cpu_move_back(label)])

            if self.game_logic.is_game_over():
                self.show_game_over()

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
        popup.configure(bg=BLUE)
        pop_width = 300
        pop_height = 150
        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()
        x = (window_width / 2) - (pop_width / 2)
        y = (window_height / 2) - (pop_height / 2)
        popup.geometry(f'{pop_width}x{pop_height}+{int(x)}+{int(y)}')

        tk.Label(popup, text=winner_text, font=("Helvetica", 18), bg=BLUE).pack(pady=20)
        tk.Button(popup, text="OK", command=lambda: [popup.destroy(), self.reset_game()]).pack(pady=10)

        popup.bind("<Return>", lambda event: [popup.destroy(), self.reset_game()])

        popup.transient(self)
        popup.grab_set()
        popup.focus_set()

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
        self.player_score_label.config(text=f"{self.controller.player_name}: {self.game_logic.player_score}")

    
    def cpu_move_forward(self, label, step=0):
        total_steps = 150

        if step <= total_steps:
            final_y = label.winfo_y() + 1
            label.place(x=label.winfo_x(), y=final_y)

            self.after(5, lambda: self.cpu_move_forward(label=label, step=step + 1))

    def cpu_move_back(self, label, step=0):
        total_steps = 150

        if step <= total_steps:
            final_y = label.winfo_y() - 1
            label.place(x=label.winfo_x(), y=final_y)

            self.after(5, lambda: self.cpu_move_back(label=label, step=step + 1))
        

    
            

