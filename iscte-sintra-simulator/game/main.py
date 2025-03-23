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
from day_manager import DayManager

pygame.mixer.init()
pygame.mixer.music.load("iscte-sintra-simulator/assets/sound/music/ewigmusic.mp3")  # Load the file
pygame.mixer.music.play(-1)  # Play indefinitely (-1 loops) 

pygame.mixer.music.set_volume(0.03)  # Volume (0.0 to 1.0)

screen = pygame.display.set_mode((1280, 720))
player1 = Player(800, 160, "iscte-sintra-simulator/assets/images/characters/gaudencio/gaudencio_back.png", (0,0,0), 1)

mainMenu = MainMenu(screen, player1)
multiusos = Multiusos(screen, player1)
entrada = Entrada(screen, player1)
gaudencioMinigame = GaudencioMinigame(screen, player1)
uata = UATA(screen, player1)
minigame2 = Minigame2(screen, player1)
lab = LAB(screen, player1)
minigame1 = Minigame1(screen, player1)
day_manager = DayManager(1)


mainMenu.load()
nextCena = day_manager.show_begin_day()


while True:
    if nextCena == "go to gaudencio":
        nextCena = gaudencioMinigame.load()
        
    elif nextCena ==  "go to multiusos":
        nextCena = multiusos.load(False,False, day_manager.get_current_day())
        
    elif nextCena ==  "go to multiusos - lab":
        nextCena = multiusos.load(True, False, day_manager.get_current_day())
        
    elif nextCena == "go to multiusos - uata":
        nextCena = multiusos.load(False,True, day_manager.get_current_day())
        
    elif nextCena == "go to entrada":
        nextCena = entrada.load(day_manager.get_current_day(), False)
        
    elif nextCena == "go to entrada - day begin":
        nextCena = entrada.load(day_manager.get_current_day(), True)
        
    elif nextCena == "go to uata":
         nextCena = uata.load(False)
        
    elif nextCena == "go to uata - minigame2":
        nextCena = uata.load(True)
        
    elif nextCena == "go to lab":
        nextCena = lab.load()
        
    elif nextCena == "go to memoria":
        nextCena = minigame2.load()
        
    elif nextCena == "go to minigame1":
        nextCena = minigame1.load()
        
    elif nextCena == "fim do dia":
        nextCena = day_manager.show_end_day()
        
    elif nextCena == "inicio do dia":
        nextCena = day_manager.show_begin_day()
        
    else: break