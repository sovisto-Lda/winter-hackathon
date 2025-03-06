import pygame
#from ...global_variables import GameVariables as GB



WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PLAYER_SIZE = (100, 100)
VEL = 5
ATTACK_DAMAGE = 10
PROJECTILE_SPEED = 7

class Gaudencio:
    def __init__(self, x, y, image_path, color):
        try:
            self.image = pygame.image.load(image_path).convert_alpha()  # Load image safely
            self.image = pygame.transform.scale(self.image, PLAYER_SIZE)  # Resize
        except pygame.error as e:
            print(f"Error loading image: {e}")
            self.image = pygame.Surface(PLAYER_SIZE)  # Fallback
            self.image.fill(color)  # Fill with player's color
        self.rect = self.image.get_rect(topleft=(x, y))  # Set position
        self.color = color  # Store color for projectile logic
        self.projectiles = []  # Initialize projectiles
        self.health = 100  # Initialize health
        self.orientation = "R"

    def draw(self, screen):
        if self.orientation == "U": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png").convert_alpha()
        if self.orientation == "D": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_right.png").convert_alpha()
        if self.orientation == "L": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_left.png").convert_alpha()
        if self.orientation == "R": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/gaudencio/gaudencio_front.png").convert_alpha()
            
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)  # Resize
        screen.blit(self.image, self.rect)  # Draw player image

       

    def move(self, keys, colidables):

        if keys[pygame.K_a] and self.rect.x - VEL > 0:
            if self.check_collision(pygame.Rect(self.rect.x - VEL, self.rect.y, PLAYER_SIZE[0], PLAYER_SIZE[1]), colidables): return
            self.rect.x -= VEL
            self.orientation = "L"

        if keys[pygame.K_d] and self.rect.x + VEL < 1280 - PLAYER_SIZE[0]:
            if self.check_collision(pygame.Rect(self.rect.x + VEL, self.rect.y, PLAYER_SIZE[0], PLAYER_SIZE[1]), colidables): return
            self.rect.x += VEL
            self.orientation = "R"

        if keys[pygame.K_w] and self.rect.y - VEL > 0:
            if self.check_collision(pygame.Rect(self.rect.x, self.rect.y - VEL, PLAYER_SIZE[0], PLAYER_SIZE[1]), colidables): return
            self.rect.y -= VEL
            self.orientation = "U"
            
        if keys[pygame.K_s] and self.rect.y + VEL < 720 - PLAYER_SIZE[1]:
            if self.check_collision(pygame.Rect(self.rect.x, self.rect.y + VEL, PLAYER_SIZE[0], PLAYER_SIZE[1]), colidables): return
            self.rect.y += VEL
            self.orientation = "D"


    def check_collision(self, new_rect, colidables):
        for structure in colidables:
            if structure == self: continue
            if new_rect.colliderect(structure):
                return True  # Collision detected
        return False  # No collision