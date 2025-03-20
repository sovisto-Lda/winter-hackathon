import os
import pygame
from characters.players.player import Player
from characters.players.gaudencio import Gaudencio
from characters.npcs.npc import NPC
from characters.npcs.seguranca import Seguranca
from structures.static_structures.table_multiusos import TableMultiusos
from structures.interactive_structures.gateway import Gateway
from gaudencio_minigame import GaudencioMinigame

os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))



class Entrada:
    def __init__(self, screen):
        self.screen = screen

    def load(self):
        pygame.init()

        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        screen.fill((0,0,0))

        image = pygame.image.load("iscte-sintra-simulator/assets/images/ISS_Entrada.png").convert_alpha()  # Load image safely
        image = pygame.transform.scale(image, (1280, 720))

        rect = image.get_rect()  # Set position
        rect.topleft = (0, 0)  # Position at the top-left corner

        player1 = Player(850, 250, "iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png", (0,0,0), 1)

        npc1 = Seguranca(200, 180, "iscte-sintra-simulator/assets/images/seguranca.png", (0,0,0))

        blocker1 = pygame.Rect(0, 0, 1280, 160)
        blocker2 = pygame.Rect(0, 620, 1280, 150)
        blocker3 = pygame.Rect(106, 205, 110, 350)


        door1 = Gateway(1222, 500,"iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Porta Multiusos.png", 0, screen)

        door2 = Gateway(859,595, "iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Porta Multiusos.png",0,screen)


        colidables = [blocker1, blocker2, blocker3]

        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)

                if event.type == pygame.QUIT:
                    running = False              

            screen.fill("white")

            keys = pygame.key.get_pressed()

            if keys[pygame.K_e] or keys[pygame.K_RSHIFT]:
                npc1.open_dialog(player1, screen)

                if door1.can_interact(player1, screen):
                    return "go to gaudencio"
                
                if door2.can_interact(player1, screen):
                    return "go to multiusos"
                    
                

            if keys[pygame.K_x]:
                npc1.close_dialog(player1, screen)
            
            player1.move(keys, colidables)


            pygame.draw.rect(screen, (255, 255, 255), blocker1)
            pygame.draw.rect(screen, (255, 255, 255), blocker2)
            pygame.draw.rect(screen, (255, 255, 255), blocker3)

            screen.blit(image, rect)  # Draw player image


            npc1.draw(screen)
            player1.draw(screen)


            npc1.interact(player1, screen)

            pygame.display.flip()

            dt = clock.tick(60) / 1000


        pygame.quit()


