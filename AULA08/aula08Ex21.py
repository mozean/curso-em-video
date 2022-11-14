# REPRODUZA UM ARQUIVO .mp3

import pygame
pygame.mixer.init()
pygame.mixer.music.load(/home/runner/curso-em-video/aula08Ex21/audio.mp3)
pygame.mixer.music.play()
pygame.event.wait()
