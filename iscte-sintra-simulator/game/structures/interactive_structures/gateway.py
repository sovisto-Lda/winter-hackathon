import pygame
from .interactive_structure import InteractiveStructure

class Gateway(InteractiveStructure):

    def can_interact(self, players, screen):
        if not (self.checkProximity(players)): return False
        else: return True
