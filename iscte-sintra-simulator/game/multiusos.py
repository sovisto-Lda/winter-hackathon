import os
import pygame
from characters.players.player import Player
from characters.players.gaudencio import Gaudencio
from characters.npcs.npc import NPC
from structures.static_structures.table_multiusos import TableMultiusos
from structures.interactive_structures.gateway import Gateway
from entrada import Entrada


class Multiusos:
    def __init__(self, screen, player1):
        self.screen = screen
        self.player1 = player1

    def load(self, fromLab, fromUata):

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

        if (fromLab):
            self.player1.x = 170
            self.player1.y = 500
        elif (fromUata):
            self.player1.x = 600
            self.player1.y = 200
        else:
            self.player1.x = 1000
            self.player1.y = 150

        self.player1.change_rect(self.player1.x, self.player1.y)

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
            if keys[pygame.K_e]:
                if door1.can_interact(self.player1, screen):
                    return "go to entrada"
                
                if door2.can_interact(self.player1, screen):
                    print("UATA")
                    return "go to uata"
                
                if door3.can_interact(self.player1, screen):
                    return "go to minigame1"

                    

        
            self.player1.move(keys, colidables)

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
            
            self.player1.draw(self.screen)
            Player.draw_score(self.player1, self.screen)


            pygame.display.flip()

            dt = clock.tick(60) / 1000




        pygame.quit()