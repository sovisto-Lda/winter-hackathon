import pygame
from characters.players.player import Player
from characters.players.gaudencio import Gaudencio
from characters.npcs.npc import NPC
from characters.npcs.fred import Fred
from structures.static_structures.table_multiusos import TableMultiusos
from structures.interactive_structures.gateway import Gateway
from characters.npcs.fred import Fred


def Multiusos(screen):
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    screen.fill((0,0,0))

    image = pygame.image.load("iscte-sintra-simulator/assets/images/SALA MULTIUSOS/ISS_Sala_Multiusos s col.png").convert_alpha()  # Load image safely
    image = pygame.transform.scale(image, (1280, 720))

    rect = image.get_rect()  # Set position
    rect.topleft = (0, 0)  # Position at the top-left corner

    table1 = TableMultiusos(900, 500, "iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Mesa_Multiusos_cpessoa_corte.png")

    player1 = Player(100, 250, "iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png", (0,0,0))

    npc1 = NPC(150, 450, "iscte-sintra-simulator/assets/images/fred/Fred_front.png", (0,0,0))

<<<<<<< Updated upstream
    door1 = Gateway(875, -8,"iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Porta Multiusos.png", 3.8, screen)

    fred = Fred(0,0,"iscte-sintra-simulator/assets/images/FredOnThePhone_right",(0,0,0))

    colidables = [table1, door1]


    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
               
            if event.type == pygame.QUIT:
                running = False              
=======

        door1 = Gateway(875, -8,"iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Porta Multiusos.png", 3.8, screen)
        door2 = Gateway(548, 257, "iscte-sintra-simulator/assets/images/SALA MULTIUSOS/objetos/ISS_Porta Multiusos.png", 0, screen)

        player1 = Player(1000, 250, "iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png", (0,0,0))
        
        colidables = [table1, door1]
        
        popup_image = pygame.image.load("iscte-sintra-simulator/assets/images/dialogs/gaudencio1.png").convert_alpha()
        popup_image = pygame.transform.scale(popup_image, (int(popup_image.get_width() * .85), int(popup_image.get_height() * .85)))
        popup_rect = popup_image.get_rect()  # Set position
        popup_rect.centerx = 620
        popup_rect.centery = 500

        # Popup timer
        popup_duration = 8000  # 3 seconds
        popup_start_time = None  # Track when the popup starts


        popup_start_time = pygame.time.get_ticks()  # Record start time
>>>>>>> Stashed changes

        screen.fill("white")

        keys = pygame.key.get_pressed()

<<<<<<< Updated upstream
        if keys[pygame.K_e]:
            npc1.open_dialog([player1], screen)
            
            if door1.can_interact([player1], screen):
                Entrada(screen)
                return
            
            


=======
            screen.fill("white")

            keys = pygame.key.get_pressed()

            if keys[pygame.K_e]:
                
                if door1.can_interact([player1], screen):
                    return "go to entrada"
                
                if door2.can_interact([player1], screen):
                    return "go to uata"
            
            player1.move(keys, colidables)

            screen.blit(image, rect)  # Draw player image

            door1.draw(screen)
            table1.draw(screen)
            player1.draw(screen)


            # edoor1.interact([player1], screen)
>>>>>>> Stashed changes

        if keys[pygame.K_x]:
            npc1.close_dialog([player1], screen)
        
        
        
        player1.move(keys, colidables)

        screen.blit(image, rect)  # Draw player image

        door1.draw(screen)
        table1.draw(screen)
        npc1.draw(screen)
        player1.draw(screen)


        npc1.interact([player1], screen)
        # edoor1.interact([player1], screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000




<<<<<<< Updated upstream
    pygame.quit()
screen = pygame.display.set_mode((1280, 720))

Multiusos(screen)
=======
        pygame.quit()
>>>>>>> Stashed changes
