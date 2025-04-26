import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

    def load_sound(self, name, filepath):
        sound = pygame.mixer.Sound(filepath)
        self.sounds[name] = sound

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()
    
    def stop_sound(self, name):
        if name in self.sounds:
            self.sounds[name].stop()