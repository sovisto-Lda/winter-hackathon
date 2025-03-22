import pygame
from minigames.gaudencio_minigame import GaudencioMinigame
from entrada import Entrada
from multiusos import Multiusos
from main_menu import MainMenu
from uata import UATA
from minigames.minigame2 import Minigame2
from minigames.mini_game_1 import Minigame
from salaLab import LAB

pygame.mixer.init()
pygame.mixer.music.load("iscte-sintra-simulator/assets/sound/music/ewigmusic.mp3")  # Load the file
pygame.mixer.music.play(-1)  # Play indefinitely (-1 loops) 

pygame.mixer.music.set_volume(1)  # Volume (0.0 to 1.0)

screen = pygame.display.set_mode((1280, 720))

mainMenu = MainMenu(screen)
multiusos = Multiusos(screen)
entrada = Entrada(screen)
gaudencioMinigame = GaudencioMinigame(screen)
uata = UATA(screen)
minigame2 = Minigame2(screen)
lab = LAB(screen)
minigame1 = Minigame1(screen)

mainMenu.load()
nextCena = entrada.load()

while True:
    if nextCena == "go to gaudencio":
        nextCena = gaudencioMinigame.load()
    elif nextCena ==  "go to multiusos":
        nextCena = multiusos.load(False)
    elif nextCena ==  "go to multiusos - lab":
        nextCena = multiusos.load(True)
    elif nextCena == "go to entrada":
        nextCena = entrada.load()
    elif nextCena == "go to uata":
        nextCena = uata.load()
    elif nextCena == "go to lab":
        nextCena = lab.load()
    elif nextCena == "go to memoria":
        nextCena = minigame2.load()
    elif nextCena == "go to minigame1":
        nextCena = minigame1.load()
    else: break



