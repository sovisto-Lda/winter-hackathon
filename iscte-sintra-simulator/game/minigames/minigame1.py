import pygame
import random

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

BOXES_WIDTH = 100
BOXES_HEIGHT = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Drag And Drop')

#Caixas para colocar
spaceBoxes = []
usedSpaceBoxes = []
spaceBox1 = pygame.Rect(400, 500, BOXES_WIDTH, BOXES_HEIGHT)
spaceBox2 = pygame.Rect(550, 500, BOXES_WIDTH, BOXES_HEIGHT)
spaceBox3 = pygame.Rect(700, 500, BOXES_WIDTH, BOXES_HEIGHT)
spaceBox4 = pygame.Rect(850, 500, BOXES_WIDTH, BOXES_HEIGHT)
spaceBox5 = pygame.Rect(1000, 500, BOXES_WIDTH, BOXES_HEIGHT)
spaceBox6 = pygame.Rect(1150, 500, BOXES_WIDTH, BOXES_HEIGHT)

spaceBoxes.append(spaceBox1)
spaceBoxes.append(spaceBox2)
spaceBoxes.append(spaceBox3)
spaceBoxes.append(spaceBox4)
spaceBoxes.append(spaceBox5)
spaceBoxes.append(spaceBox6)



draggableBoxes = []
lockedBoxes = []
draggableBox1 = pygame.Rect(100, 200, BOXES_WIDTH, BOXES_HEIGHT)
draggableBox2 = pygame.Rect(250, 200, BOXES_WIDTH, BOXES_HEIGHT)
draggableBox3 = pygame.Rect(400, 200, BOXES_WIDTH, BOXES_HEIGHT)
draggableBox4 = pygame.Rect(550, 200, BOXES_WIDTH, BOXES_HEIGHT)
draggableBox5 = pygame.Rect(700, 200, BOXES_WIDTH, BOXES_HEIGHT)
draggableBox6 = pygame.Rect(850, 200, BOXES_WIDTH, BOXES_HEIGHT)

draggableBoxes.append(draggableBox1)
draggableBoxes.append(draggableBox2)
draggableBoxes.append(draggableBox3)
draggableBoxes.append(draggableBox4)
draggableBoxes.append(draggableBox5)
draggableBoxes.append(draggableBox6)

initial_positions = {i: box.topleft for i, box in enumerate(draggableBoxes)}
active_draggableBox = None
all_correct = False

run = True

while run:
    screen.fill("black")

    # Desenhar o espaço
    for spaceBox in spaceBoxes:
        pygame.draw.rect(screen, "gray", spaceBox)

    # Desenhar as caixas arrastáveis
    for draggableBox in draggableBoxes:
        pygame.draw.rect(screen, "pink", draggableBox)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Clicar para arrastar
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, draggableBox in enumerate(draggableBoxes):
                if draggableBox.collidepoint(event.pos):
                    active_draggableBox = i

        # Mover a caixa ativa
        if event.type == pygame.MOUSEMOTION and active_draggableBox is not None:
            draggableBoxes[active_draggableBox].move_ip(event.rel)

        # Soltar a caixa
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if active_draggableBox is not None:
                correct_space = spaceBoxes[active_draggableBox]
                
                if draggableBoxes[active_draggableBox].colliderect(correct_space):
                    draggableBoxes[active_draggableBox].topleft = correct_space.topleft
                else:
                    draggableBoxes[active_draggableBox].topleft = initial_positions[active_draggableBox]
                
                active_draggableBox = None

            all_correct = all(draggableBoxes[i].topleft == spaceBoxes[i].topleft for i in range(len(draggableBoxes)))

    if all_correct:
        pygame.draw.rect(screen, "green", (500, 300, 200, 100))

    pygame.display.flip()

pygame.quit()