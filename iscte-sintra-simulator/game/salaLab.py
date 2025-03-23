import pygame
from characters.players.player import Player
from characters.players.gaudencio import Gaudencio
from structures.static_structures.table_multiusos import TableMultiusos
from structures.interactive_structures.gateway import Gateway
from characters.npcs.storasov import StoraSov


class LAB:
    def __init__(self, screen):
        self.screen = screen

    def load(self):

        pygame.init()

        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        screen.fill((0,0,0))

        image = pygame.image.load("iscte-sintra-simulator/assets/images/ISS_Sala_lab.png").convert_alpha()  # Load image safely
        image = pygame.transform.scale(image, (1280, 720))

        rect = image.get_rect()  # Set position
        rect.topleft = (0, 0)  # Position at the top-left corner

        player1 = Player(1003, 537, "iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png", (0,0,0), 1)

        prof = StoraSov(100, 100, "iscte-sintra-simulator/assets/images/StoraSOV.png", (0,0,0))        
        
        door1 = Gateway(540,249, "iscte-sintra-simulator/assets/images/fred/FredOnThePhone_right.png", 0, screen)

        blocker0 = pygame.Rect(546, 0, 546, 600)
        blocker1 = pygame.Rect(0, 0, 1280, (2/8)*720 - 20)

        colidables = [door1, blocker0, blocker1]


        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                
                if event.type == pygame.QUIT:
                    running = False              

            screen.fill("white")

            keys = pygame.key.get_pressed()

            if keys[pygame.K_e] or keys[pygame.K_RSHIFT]:
            
                if door1.can_interact(player1, screen):
                    return "go to multiusos"



            # if keys[pygame.K_x]:

            
            player1.move(keys, colidables)


            pygame.draw.rect(screen, (255, 255, 255), blocker0)
            pygame.draw.rect(screen, (255, 255, 255), blocker1)


            screen.blit(image, rect)  # Draw player image

            door1.draw(screen)
            player1.draw(screen)
            prof.draw(screen)


            pygame.display.flip()

            dt = clock.tick(60) / 1000


        pygame.quit()