from mutagen.mp3 import MP3 as mp3
import pygame
import time

class SoundController():
    def __init__(self, mp3_file):
        filename = mp3_file
        self.pygame = pygame
        self.pygame.mixer.init()
        self.pygame.mixer.music.load(filename)
        self.mp3_length = mp3(filename).info.length

    def play(self):
        self.pygame.mixer.music.play(1)

    def stop(self):
        self.pygame.mixer.music.stop()

