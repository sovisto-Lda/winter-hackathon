import pygame
from minigames.gaudencio_minigame import GaudencioMinigame
from entrada import Entrada
from multiusos import Multiusos
from main_menu import MainMenu
from uata import UATA
from minigames.minigame2 import Minigame2
from minigames.mini_game_1 import Minigame1
from salaLab import LAB
from characters.players.player import Player

pygame.mixer.init()
pygame.mixer.music.load("iscte-sintra-simulator/assets/sound/music/ewigmusic.mp3")  # Load the file
pygame.mixer.music.play(-1)  # Play indefinitely (-1 loops) 

pygame.mixer.music.set_volume(0.03)  # Volume (0.0 to 1.0)

screen = pygame.display.set_mode((1280, 720))
player1 = Player(850, 250, "iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png", (0,0,0), 1)

mainMenu = MainMenu(screen, player1)
multiusos = Multiusos(screen, player1)
entrada = Entrada(screen, player1)
gaudencioMinigame = GaudencioMinigame(screen, player1)
uata = UATA(screen, player1)
minigame2 = Minigame2(screen, player1)
lab = LAB(screen, player1)
minigame1 = Minigame1(screen, player1)

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