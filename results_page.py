import tkinter as tk
from constants import BLUE

class ResultsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(bg=BLUE)

        # Temporary placeholder
        label = tk.Label(self, text="Results Page", font=("Helvetica", 24), bg=BLUE)
        label.pack(pady=100)
