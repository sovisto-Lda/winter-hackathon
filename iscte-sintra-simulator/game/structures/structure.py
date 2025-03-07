import pygame
#from ...global_variables import GameVariables as GB


class Structure:
    def __init__(self, x, y, image_path, scale_multiplier,):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale_multiplier, self.image.get_height() * scale_multiplier))

        self.rect = self.image.get_rect(topleft=(x, y))  # Set position

    def draw(self, screen):
        screen.blit(self.image, self.rect)