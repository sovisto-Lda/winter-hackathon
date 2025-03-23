import pygame
from characters.players.player import Player
from costum_panel import CostumPanel

screen = pygame.display.set_mode((1280, 720))
player1 = Player(850, 250, "iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png", (0,0,0), 1)
costum_panel = CostumPanel(screen, player1)
costum_panel.load()