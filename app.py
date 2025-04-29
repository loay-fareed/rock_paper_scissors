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

        # Window Setup
        self.title("Rock, Paper, Scissors")
        self.geometry('800x600')
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