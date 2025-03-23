import pygame
from characters.players.player import Player
from characters.players.gaudencio import Gaudencio
from structures.static_structures.table_multiusos import TableMultiusos
from structures.interactive_structures.gateway import Gateway
from characters.npcs.fred import Fred


class UATA:
    def __init__(self, screen, player1):
        self.screen = screen
        self.player1 = player1

    def load(self):

        pygame.init()

        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        screen.fill((0,0,0))

        image = pygame.image.load("iscte-sintra-simulator/assets/images/SALA MULTIUSOS/ISS_Sala_Multiusos col_MULTIUSOS escura.png").convert_alpha()  # Load image safely
        image = pygame.transform.scale(image, (1280, 720))

        rect = image.get_rect()  # Set position
        rect.topleft = (0, 0)  # Position at the top-left corner

        fred = Fred(100, 100, "iscte-sintra-simulator/assets/images/fred/FredOnThePhone_right.png", (0,0,0))        
        self.player1.x = 474
        self.player1.y = 228
        self.player1.change_rect(self.player1.x, self.player1.y)
        door1 = Gateway(540,249, "iscte-sintra-simulator/assets/images/fred/FredOnThePhone_right.png", 0, screen)

        blocker0 = pygame.Rect(546, 0, 546, 600)
        blocker1 = pygame.Rect(0, 0, 1280, (2/8)*720 - 20)

        colidables = [door1, blocker0, blocker1]

        while running:
            keys = pygame.key.get_pressed()
            screen.fill("white")
            
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    # Interaction with Fred
                    if event.key == pygame.K_e and fred.checkProximity(self.player1, screen):
                        print("Talking to Fred")
                        fred.open_dialog(self.player1, screen)        
                    
                    # Interaction with Door
                    elif event.key == pygame.K_e and door1.can_interact(self.player1, screen):
                        print("Going back to Multiusos")
                        return "go to multiusos"
    
                    # Close Dialog with Fred and start waiting mini game
                    elif event.key == pygame.K_x:
                        print("Closing Fred's Dialog")
                        fred.close_dialog(self.player1, screen)
                        return "go to memoria"
                                


            
            
            self.player1.move(keys, colidables)


            pygame.draw.rect(screen, (255, 255, 255), blocker0)
            pygame.draw.rect(screen, (255, 255, 255), blocker1)


            screen.blit(image, rect)  # Draw player image

            door1.draw(screen)
            fred.draw(screen)
            self.player1.draw(self.screen)
            Player.draw_score(self.player1, self.screen)

            fred.interact(self.player1, screen)

            pygame.display.flip()

            dt = clock.tick(60) / 1000


        pygame.quit()