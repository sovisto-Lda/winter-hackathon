import pygame
import random

# Initialize pygame
pygame.init()

WIDTH, HEIGHT = 600, 400
WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0)
FONT = pygame.font.Font(None, 40)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Challenge")

# Key options
KEY_OPTIONS = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_w]  # Allowed keys

def minigame2:
    