import pygame
from .interactive_structure import InteractiveStructure

class Gateway(InteractiveStructure):

    def interact(self, players, screen):
        if not (self.checkProximity(players)): return
        else: print("A tua prima")

    def travel(self):
        print("going to hell")