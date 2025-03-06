import os
import pygame
from global_variables import GameVariables as GB
from characters.players.player import Player
from structures.static_structures.static_structure import StaticStructure
from structures.interactive_structures.interactive_structure import InteractiveStructure
from structures.interactive_structures.gateway import Gateway
from main_menu import MainMenu
from multiusos import Multiusos

os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

# pygame setup
pygame.init()
GB = GB()

pygame.font.init() 
myfont = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 30)
text_surface = myfont.render('Some Text', False, (0, 0, 0))



screen = pygame.display.set_mode((GB.screen_width, GB.screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

interactibles = []
colidables = []
players = []

player1 = Player(100, 50//2, "iscte-sintra-simulator/assets/images/player1_PH.png", (0,0,0))
player2 = Player(200, 50//2, "iscte-sintra-simulator/assets/images/player1_PH.png", (0,0,0))

players.append(player1)
players.append(player2)


struc1 = StaticStructure(500, 20, "iscte-sintra-simulator/assets/images/static_structure_PH.png")
struc2 = InteractiveStructure(700, 20, "iscte-sintra-simulator/assets/images/interactive_structure_PH.png", screen)
gate1 = Gateway(100, 400, "iscte-sintra-simulator/assets/images/gateway.png", screen)

colidables.append(player1)
colidables.append(player2)
colidables.append(struc1)
colidables.append(struc2)
colidables.append(gate1)

interactibles.append(struc2)
interactibles.append(gate1)


#MainMenu(screen)
Multiusos(screen)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_e]):
        for interactible in interactibles:
            if(interactible.checkProximity(players)):
                interactible.interact()

        for interactible in interactibles:
            interactible.checkProximity(players)

    player1.move(keys, colidables)

    player1.draw(screen)
    player2.draw(screen)

    struc1.draw(screen)
    struc2.draw(screen)
    gate1.draw(screen)




    screen.blit(text_surface, (0,0))


    # flip() the display to put your work on screen
    pygame.display.flip()



    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()