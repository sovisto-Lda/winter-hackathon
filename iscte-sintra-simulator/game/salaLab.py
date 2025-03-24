import pygame
from characters.players.player import Player
from characters.players.gaudencio import Gaudencio
from structures.static_structures.table_multiusos import TableMultiusos
from structures.interactive_structures.gateway import Gateway
from characters.npcs.storasov import StoraSOV
from characters.npcs.npc import NPC


class LAB:
    def __init__(self, screen, player1):
        self.screen = screen
        self.player1 = player1
        self.playedCodeGame = False

    def load(self):

        pygame.init()

        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        screen.fill((0,0,0))
        
        self.player1.x = 1178
        self.player1.y = 517
        
        self.player1.change_rect(self.player1.x, self.player1.y)


        image = pygame.image.load("iscte-sintra-simulator/assets/images/ISS_Sala_lab.png").convert_alpha()  # Load image safely
        image = pygame.transform.scale(image, (1280, 720))

        rect = image.get_rect()  # Set position
        rect.topleft = (0, 0)  # Position at the top-left corner

        prof = StoraSOV(100, 100, "iscte-sintra-simulator/assets/images/characters/StoraSOV.png", (0,0,0))        
        
        door1 = Gateway(1128,480, "iscte-sintra-simulator/assets/images/characters/fred/FredOnThePhone_right.png", 0, screen)

        blocker0 = pygame.Rect(1170, 0, 110, 365)
        blocker1 = pygame.Rect(1170, 623, 110, 100)
        blocker2 = pygame.Rect(0, 0, 1280, 155)
        table1 = pygame.Rect(108, 270, 744, 188)
        table2 = pygame.Rect(108, 510, 744, 188)
        desk = pygame.Rect(992, 147, 156, 68)

        colidables = [door1, blocker0, blocker1, blocker2, table1, table2, desk]

        while running:
            keys = pygame.key.get_pressed()
            screen.fill("white")

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                
                if event.type == pygame.QUIT:
                    running = False   
                    
                if event.type == pygame.KEYDOWN:
                    # Interaction with Prof
                    if event.key == pygame.K_e and prof.checkProximity(self.player1, screen):
                        print("Near Stora de SOV")
                        print(f"Player: {self.player1.rect.topleft}, Prof: {prof.rect.topleft}")
                        prof.open_dialog(self.player1, screen)   
                    
                    # Interaction with Door
                    elif event.key == pygame.K_e and door1.can_interact(self.player1, screen):
                        if self.playedCodeGame:
                            print("Going back to Multiusos")
                            return "go to multiusos"
                        else:
                            print("Ainda nao fizeste o exercício da aula")
                    
                    # Close Dialog with Prof and start waiting mini game
                    elif event.key == pygame.K_x:
                        print("Closing Prof's Dialog")
                        prof.close_dialog(self.player1, screen)
                        self.playedCodeGame = True
                        return "go to minigame1"
                           

            screen.fill("white")

            keys = pygame.key.get_pressed()

            if keys[pygame.K_e]:
            
                if door1.can_interact(self.player1, screen):
                    return "go to multiusos - lab"

            
                                

            self.player1.move(keys, colidables)


            pygame.draw.rect(screen, (255, 255, 255), blocker0)
            pygame.draw.rect(screen, (255, 255, 255), blocker1)


            screen.blit(image, rect)  # Draw player image

            door1.draw(screen)
            self.player1.draw(self.screen)
            Player.draw_score(self.player1, self.screen)
            prof.draw(screen)

            prof.interact(self.player1, self.screen)
            
            # TO check where the collidables are
            # pygame.draw.rect(self.screen, (255,0,0), blocker0)
            # pygame.draw.rect(self.screen, (0,255,0), blocker1)
            # pygame.draw.rect(self.screen, (0,255,0), table1)
            # pygame.draw.rect(self.screen, (0,255,0), table2)
            # pygame.draw.rect(self.screen, (0,255,0), desk)

            pygame.display.flip()

            dt = clock.tick(60) / 1000


        pygame.quit()