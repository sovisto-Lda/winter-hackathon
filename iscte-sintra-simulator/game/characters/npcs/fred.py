import pygame
from .npc import NPC

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PLAYER_SIZE = (100, 100)
VEL = 5
ATTACK_DAMAGE = 10
PROJECTILE_SPEED = 7

class Fred(NPC):

    def interact(self, players, screen):
        if not (self.checkProximity(players, screen)): return False

        if self.openDialog:
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/dialogs/fred dialog.png").convert_alpha()
            dialog = pygame.transform.scale(dialog, (int(dialog.get_width() * .85), int(dialog.get_height() * .85)))
            dialog_rect = dialog.get_rect()  # Set position
            dialog_rect.centerx = 620
            dialog_rect.centery = 500
            screen.blit(dialog, dialog_rect)

        print(self.isInteracting)
        if (self.isInteracting == False): return False
    
        return True