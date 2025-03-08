import pygame
from gaudencio_minigame import GaudencioMinigame
from entrada import Entrada
from multiusos import Multiusos
from main_menu import MainMenu
from uata import UATA
from minigames.minigame2 import Minigame2
from salaLab import LAB


screen = pygame.display.set_mode((1280, 720))

mainMenu = MainMenu(screen)
multiusos = Multiusos(screen)
entrada = Entrada(screen)
gaudencioMinigame = GaudencioMinigame(screen)
uata = UATA(screen)
minigame2 = Minigame2(screen)
lab = LAB(screen)

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
    elif nextCena == "go to memoria":
        nextCena = minigame2.load()
    else: break



