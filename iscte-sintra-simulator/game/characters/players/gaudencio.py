import pygame
from .player import Player
import random
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

    def __init__(self, x, y, image_path, color):
        super().__init__(x, y, image_path, color, 1)

        self.isTurned = False

        self.turning = False

        self.set_random_turn_time()

    
    def draw(self, screen):
        if self.orientation == "U": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png").convert_alpha()
        if self.orientation == "D": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_front.png").convert_alpha()
        if self.orientation == "L": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_left.png").convert_alpha()
        if self.orientation == "R": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_right.png").convert_alpha()
            
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)  # Resize
        screen.blit(self.image, self.rect)  # Draw player image


    def move(self, screen):
            self.isTurned = self.turning

            if self.isTurned:
                self.orientation = "U"
            else:
                self.orientation = "D"

            self.isTurned = not self.isTurned

            self.draw(screen)


    def set_random_turn_time(self):
        random_time = random.randint(1000, 5000)
        pygame.time.set_timer(pygame.USEREVENT, random_time)
        print('Random time set,', random_time)


    def handle_event(self, event):
        if event.type == pygame.USEREVENT:
            print('Vira o gaudencio!')
            self.turning = not self.turning  # Toggle turning
            self.set_random_turn_time()  # Set new random duration

