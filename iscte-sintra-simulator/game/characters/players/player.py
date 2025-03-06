import pygame
#from global_variables import GameVariables as GB



WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PLAYER_SIZE = (50, 50)
VEL = 5
ATTACK_DAMAGE = 10
PROJECTILE_SPEED = 7

class Player:
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

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw player image
        for projectile in self.projectiles:
            pygame.draw.rect(screen, BLACK, projectile)  # Draw projectiles

    def move(self, keys, colidables):

        if keys[pygame.K_a] and self.rect.x - VEL > 0:
            if self.check_collision(pygame.Rect(self.rect.x - VEL, self.rect.y, PLAYER_SIZE[0], PLAYER_SIZE[1]), colidables): return
            self.rect.x -= VEL
        if keys[pygame.K_d] and self.rect.x + VEL < 1280 - PLAYER_SIZE[0]:
            if self.check_collision(pygame.Rect(self.rect.x + VEL, self.rect.y, PLAYER_SIZE[0], PLAYER_SIZE[1]), colidables): return
            self.rect.x += VEL
        if keys[pygame.K_w] and self.rect.y - VEL > 0:
            if self.check_collision(pygame.Rect(self.rect.x, self.rect.y - VEL, PLAYER_SIZE[0], PLAYER_SIZE[1]), colidables): return
            self.rect.y -= VEL
        if keys[pygame.K_s] and self.rect.y + VEL < 720 - PLAYER_SIZE[1]:
            if self.check_collision(pygame.Rect(self.rect.x, self.rect.y + VEL, PLAYER_SIZE[0], PLAYER_SIZE[1]), colidables): return
            self.rect.y += VEL

    def check_collision(self, new_rect, colidables):
        for structure in colidables:
            if structure == self: continue
            if new_rect.colliderect(structure):
                return True  # Collision detected
        return False  # No collision

    def throw_projectile(self, direction):
        if direction == 'right':
            self.projectiles.append(pygame.Rect(self.rect.right, self.rect.centery, 10, 5))
        elif direction == 'left':
            self.projectiles.append(pygame.Rect(self.rect.left - 10, self.rect.centery, 10, 5))

    def update_projectiles(self, opponent):
        for projectile in self.projectiles[:]:
            if projectile.x > WIDTH or projectile.x < 0:
                self.projectiles.remove(projectile)
            else:
                if self.color == RED:
                    projectile.x += PROJECTILE_SPEED
                else:
                    projectile.x -= PROJECTILE_SPEED
                
                if projectile.colliderect(opponent.rect):
                    opponent.health -= ATTACK_DAMAGE
                    self.projectiles.remove(projectile)
            if projectile.x > WIDTH or projectile.x < 0:
                self.projectiles.remove(projectile)
            else:
                if self.color == RED:
                    projectile.x += PROJECTILE_SPEED
                else:
                    projectile.x -= PROJECTILE_SPEED
                
                if projectile.colliderect(opponent.rect):
                    opponent.health -= ATTACK_DAMAGE
                    self.projectiles.remove(projectile)