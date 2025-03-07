import pygame
from .player import Player
#from ...global_variables import GameVariables as GB

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PLAYER_SIZE = (100, 100)
VEL = 5
ATTACK_DAMAGE = 10
PROJECTILE_SPEED = 7

class Gaudencio(Player):
    
    def draw(self, screen):
        if self.orientation == "U": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png").convert_alpha()
        if self.orientation == "D": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_front.png").convert_alpha()
        if self.orientation == "L": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_left.png").convert_alpha()
        if self.orientation == "R": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_right.png").convert_alpha()
            
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)  # Resize
        screen.blit(self.image, self.rect)  # Draw player image
