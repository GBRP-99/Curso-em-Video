import pygame
pygame.init()
pygame.mixer.music.load('all_workout.mp3.mp3')
# Lil Wayne - All Workout
pygame.mixer_music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
