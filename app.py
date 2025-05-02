import tkinter as tk
import os
from welcome_page import WelcomePage
from sound_manager import SoundManager
from gameplay_page import GameplayPage
from constants import BASE_PATH, BLUE

class RockPaperScissorsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.ruleset = "bo1"
        self.player_name = "Player"

        # Window Setup
        self.title("Rock, Paper, Scissors")
        app_width = 800
        app_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.resizable(width=False, height=False)
        self.configure(bg=BLUE)

        # Sound Manager
        self.sound_manager = SoundManager()

        # Load Sounds
        self.sound_manager.load_sound("woosh", os.path.join(BASE_PATH, "assets", "woosh.mp3"))
        self.sound_manager.load_sound("click", os.path.join(BASE_PATH, "assets", "click.mp3"))

        # Page Container
        container = tk.Frame(self)
        self.configure(width=800, height=600, bg=BLUE)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for PageClass in (WelcomePage, GameplayPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

        if hasattr(frame, "refresh"):
            frame.refresh()