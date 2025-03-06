import os
import pygame
from global_variables import GameVariables as GB
from characters.players.player import Player
from structures.static_structures.static_structure import StaticStructure

os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

# pygame setup
pygame.init()
GB = GB()

global width
width = 1280


screen = pygame.display.set_mode((GB.screen_width, GB.screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

print("hello world")

print(GB.score)

colidables = []

player1 = Player(100, 50//2, "iscte-sintra-simulator/assets/images/player1_PH.png", (0,0,0))
player2 = Player(200, 50//2, "iscte-sintra-simulator/assets/images/player1_PH.png", (0,0,0))

struc1 = StaticStructure(500, 20, "iscte-sintra-simulator/assets/images/static_structure_PH.png")

colidables.append(player1)
colidables.append(player2)
colidables.append(struc1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()

    player1.move(keys, colidables)

    player1.draw(screen)
    player2.draw(screen)

    struc1.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()



    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()