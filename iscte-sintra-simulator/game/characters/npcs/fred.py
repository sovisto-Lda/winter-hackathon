import pygame
from .npc import NPC

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PLAYER_SIZE = (100, 100)
VEL = 5
ATTACK_DAMAGE = 10
PROJECTILE_SPEED = 7

class Fred(NPC):
<<<<<<< Updated upstream

    def interact(self, players, screen):
        if not (self.checkProximity(players, screen)): return False

        if self.openDialog:
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/dialogs/fred dialog.png").convert_alpha()
=======
    def interact(self, players, screen):
        if not (self.checkProximity(players, screen)): return

        if self.openDialog:
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/dialog_box.png").convert_alpha()
            dialog = pygame.transform.scale(dialog, (int(dialog.get_width() * .85), int(dialog.get_height() * .85)))
            dialog_rect = dialog.get_rect()  # Set position
            dialog_rect.centerx = 620
            dialog_rect.centery = 500
            screen.blit(dialog, dialog_rect)
            
            
    def draw(self, screen):
        if self.orientation == "U": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/fred/Fred_back.png").convert_alpha()
        if self.orientation == "D": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/fred/Fred_front.png").convert_alpha()
        if self.orientation == "L": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/fred/FredOnThePhone_left.png").convert_alpha()
        if self.orientation == "R": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/fred/FredOnThePhone_right.png").convert_alpha()
            
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)  # Resize
        screen.blit(self.image, self.rect)  # Draw player image


    def interact(self, players, screen):
        if not (self.checkProximity(players, screen)): return

        if self.openDialog:
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/dialogs/dialog fred.png").convert_alpha()
>>>>>>> Stashed changes
            dialog = pygame.transform.scale(dialog, (int(dialog.get_width() * .85), int(dialog.get_height() * .85)))
            dialog_rect = dialog.get_rect()  # Set position
            dialog_rect.centerx = 620
            dialog_rect.centery = 500
            screen.blit(dialog, dialog_rect)

        print(self.isInteracting)
<<<<<<< Updated upstream
        if (self.isInteracting == False): return False
    
        return True
=======
        if (self.isInteracting == False): return
    
        return
    
    def open_dialog(self, players, screen):
        if self.checkProximity(players, screen): self.openDialog = True

    def close_dialog(self, players, screen):
        if self.checkProximity(players, screen): self.openDialog = False
>>>>>>> Stashed changes
