import os
import pygame
from characters.players.player import Player
from characters.players.gaudencio import Gaudencio
from characters.npcs.npc import NPC
from structures.static_structures.table_multiusos import TableMultiusos



os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

def Multiusos(screen):
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    screen.fill((0,0,0))

    image = pygame.image.load("iscte-sintra-simulator/assets/images/SALA MULTIUSOS/ISS_Sala_Multiusos s col_UATA escura.png").convert_alpha()  # Load image safely
    image = pygame.transform.scale(image, (1280, 720))

    rect = image.get_rect()  # Set position
    rect.topleft = (0, 0)  # Position at the top-left corner

    table1 = TableMultiusos(900, 500, "iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Mesa_Multiusos_cpessoa_corte.png")

    player1 = Gaudencio(100, 50//2, "iscte-sintra-simulator/assets/images/gaudencio.png", (0,0,0))

    npc1 = NPC(150, 450, "iscte-sintra-simulator/assets/images/Fred.png", (0,0,0))

    colidables = [table1]



    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
               
            if event.type == pygame.QUIT:
                running = False              

        screen.fill("white")

        keys = pygame.key.get_pressed()
        
        player1.move(keys, colidables)

        screen.blit(image, rect)  # Draw player image

        table1.draw(screen)
        npc1.draw(screen)
        player1.draw(screen)

     
        pygame.display.flip()

        dt = clock.tick(60) / 1000




    pygame.quit()