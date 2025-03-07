import os
import pygame
from global_variables import GameVariables as GB
from characters.players.player import Player
from characters.npcs.npc import NPC
from structures.static_structures.static_structure import StaticStructure
from structures.static_structures.table_multiusos import TableMultiusos
from structures.interactive_structures.interactive_structure import InteractiveStructure
from structures.interactive_structures.gateway import Gateway
from gaudencio_minigame import GaudencioMinigame
from entrada import Entrada
from multiusos import Multiusos
from main_menu import MainMenu

screen = pygame.display.set_mode((1280, 720))

mainMenu = MainMenu(screen)
multiusos = Multiusos(screen)
entrada = Entrada(screen)
gaudencioMinigame = GaudencioMinigame(screen)


mainMenu.load()
nextCena = entrada.load()

while True:
    if nextCena == "go to gaudencio":
        nextCena = gaudencioMinigame.load()
    elif nextCena ==  "go to multiusos":
        nextCena = multiusos.load()
    elif nextCena == "go to entrada":
        nextCena = entrada.load()
    elif nextCena == "go to uata":
        nextCena = uata.load()
    elif nextCena == "go to lab":
        nextCena = lab.load()



