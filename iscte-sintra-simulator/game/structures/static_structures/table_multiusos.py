import pygame
from ..static_structures.static_structure import StaticStructure

class TableMultiusos:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (185, 15))  # Scale image

        self.rect = self.image.get_rect()  # Get updated rect
        self.rect.topleft = (x, y)  # Set correct position

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)