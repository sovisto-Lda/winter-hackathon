import pygame
import random

pygame.init()

SCREEN_WIDTH = 288
SCREEN_HEIGHT = 192

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Drag And Drop')

active_box = None
dragableBoxes = []
dragableBox1 = pygame.Rect(24, 24, 48, 24)
dragableBox2 = pygame.Rect(100, 100, 24, 48)

dragableBoxes.append(dragableBox1)
dragableBoxes.append(dragableBox1)

run = True
while run:

    screen.fill("black")

    for dragableBox in dragableBoxes:
        pygame.draw.rect(screen, "pink", dragableBox)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.filp()

pygame.quit()
