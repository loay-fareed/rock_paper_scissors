import random

class GameLogic:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.wins_required = 1

    def set_rules(self, ruleset):
        if ruleset == "bo1":
            self.wins_required = 1
        elif ruleset == "bo3":
            self.wins_required = 2
        elif ruleset == "bo5":
            self.wins_required = 3

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            self.ties += 1
            return "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            self.player_score += 1
            return "player"
        else:
            self.computer_score += 1
            return "computer"

    def is_game_over(self):
        return self.player_score == self.wins_required or self.computer_score == self.wins_required

    def get_winner(self):
        if self.player_score == self.wins_required:
            return "player"
        elif self.computer_score == self.wins_required:
            return "computer"
        else:
            return "none"
