import os
import pygame
from characters.players.player import Player
from characters.players.gaudencio import Gaudencio
from characters.npcs.npc import NPC
from structures.static_structures.table_multiusos import TableMultiusos
from structures.interactive_structures.gateway import Gateway
from entrada import Entrada


class Multiusos:
    def __init__(self, screen):
        self.screen = screen

    def load(self):

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

        table1 = TableMultiusos(1070, 455, "iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Mesa_Multiusos_cpessoa_corte.png", 4.5)
        table2 = TableMultiusos(1070, 190, "iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Mesa_Multiusos_cpessoa_corte.png", 4.5)
        table3 = TableMultiusos(755, 455, "iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Mesa_Multiusos_cpessoa_corte.png", 4.5)
        table4 = TableMultiusos(755, 190, "iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Mesa_Multiusos_cpessoa_corte.png", 4.5)

        player1 = Player(1000, 150, "iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png", (0,0,0), 1)
        player2 = Player(900, 150, "iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png", (0,0,0), 2)


        npc1 = NPC(150, 450, "iscte-sintra-simulator/assets/images/fred/Fred_front.png", (0,0,0))

        door1 = Gateway(875, -8,"iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Porta Multiusos.png", 3.8, screen)
        door2 = Gateway(548, 257, "iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Porta Multiusos.png", 0, screen)
        door3 = Gateway(59, 587, "iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Porta Multiusos.png", 0, screen)
        blocker0 = pygame.Rect(0, 0, 546, 300)


        blocker1 = pygame.Rect(0, 0, 1280, (2/8)*720 - 20)
        blocker2 = pygame.Rect((5/12)*1280, 0, 10, (2/8)*720)
        blocker3 = pygame.Rect((5/12)*1280, 265, 10, (2/8)*720)
        blocker4 = pygame.Rect(0, (3/8)*720 + 65, (5/12)*1280, (2/8)*720)

        colidables = [table1, table2, table3, table4, door1, door2, door3, blocker0, blocker1, blocker2, blocker3, blocker4]


        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                
                if event.type == pygame.QUIT:
                    running = False              

            screen.fill("white")

            keys = pygame.key.get_pressed()
            if keys[pygame.K_e] or keys[pygame.K_RSHIFT]:
                npc1.open_dialog([player1, player2], screen)

                if door1.can_interact([player1, player2], screen):
                    return "go to entrada"
                
                if door2.can_interact([player1, player2], screen):
                    return "go to uata"
                
                if door3.can_interact([player1,player2], screen):
                    return "go to lab"

                    

            if keys[pygame.K_x]:
                npc1.close_dialog([player1, player2], screen)
            
            player1.move(keys, colidables)
            player2.move(keys, colidables)

            pygame.draw.rect(screen, (255, 255, 255), blocker0)
            pygame.draw.rect(screen, (255, 255, 255), blocker1)
            pygame.draw.rect(screen, (255, 255, 255), blocker2)
            pygame.draw.rect(screen, (255, 255, 255), blocker3)
            pygame.draw.rect(screen, (255, 255, 255), blocker4)

            screen.blit(image, rect)  # Draw player image

            door1.draw(screen)
            door2.draw(screen)
            table1.draw(screen)
            table2.draw(screen)
            table3.draw(screen)
            table4.draw(screen)
            npc1.draw(screen)
            player1.draw(screen)
            player2.draw(screen)




            npc1.interact([player1, player2], screen)
            # edoor1.interact([player1, player2], screen)

            pygame.display.flip()

            dt = clock.tick(60) / 1000




        pygame.quit()


screen = pygame.display.set_mode((1280, 720))

Multiusos(screen)