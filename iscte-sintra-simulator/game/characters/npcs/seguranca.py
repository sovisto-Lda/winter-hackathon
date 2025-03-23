import pygame
from .npc import NPC

PLAYER_SIZE = (100, 100)

class Seguranca(NPC):

    def draw(self, screen):
        self.image = pygame.image.load("iscte-sintra-simulator/assets/images/characters/seguranca.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)  # Resize
        screen.blit(self.image, self.rect)  # Draw player image
    


    def interact(self, player, screen):
        if not (self.checkProximity(player, screen)): return

        if self.openDialog:
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/dialogs/seg1.png").convert_alpha()
            dialog = pygame.transform.scale(dialog, (int(dialog.get_width() * .85), int(dialog.get_height() * .85)))
            dialog_rect = dialog.get_rect()  # Set position
            dialog_rect.centerx = 620
            dialog_rect.centery = 500
            screen.blit(dialog, dialog_rect)

        print(self.isInteracting)
        if (self.isInteracting == False): return
    
        return