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

class NPC:
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

        self.openDialog = False

    def draw(self, screen):
        if self.orientation == "U": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/fred/Fred_front.png").convert_alpha()
        if self.orientation == "D": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/fred/Fred_front.png").convert_alpha()
        if self.orientation == "L": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/fred/Fred_front.png").convert_alpha()
        if self.orientation == "R": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/fred/Fred_front.png").convert_alpha()
            
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)  # Resize
        screen.blit(self.image, self.rect)  # Draw player image


    def move(self, keys, colidables):
        pass

    def check_collision(self, new_rect, colidables):
        for structure in colidables:
            if structure == self: continue
            if new_rect.colliderect(structure):
                return True  # Collision detected
        return False  # No collision
    



    def checkProximity(self, players, screen):
        for player in players:
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery

            if (dx*dx + dy*dy < 10000): 
                print("is close!")
                self.isInteracting = True
                exclamation = pygame.image.load("iscte-sintra-simulator/assets/images/exclamation.png").convert_alpha()
                exclamation = pygame.transform.scale(exclamation, (int(exclamation.get_width() * .25), int(exclamation.get_height() * .25)))
                exclamation_rect = exclamation.get_rect()  # Set position
                exclamation_rect.centerx = self.rect.topright[0] + 5
                exclamation_rect.centery = self.rect.topright[1] + 0
                screen.blit(exclamation, exclamation_rect)

                return True
            else: 
                self.isInteracting = False
        return False

    def interact(self, players, screen):
        if not (self.checkProximity(players, screen)): return

        if self.openDialog:
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/dialog_box.png").convert_alpha()
            dialog = pygame.transform.scale(dialog, (int(dialog.get_width() * .85), int(dialog.get_height() * .85)))
            dialog_rect = dialog.get_rect()  # Set position
            dialog_rect.centerx = 620
            dialog_rect.centery = 500
            screen.blit(dialog, dialog_rect)

        print(self.isInteracting)
        if (self.isInteracting == False): return
    
        return
    
    def open_dialog(self, players, screen):
        if self.checkProximity(players, screen): self.openDialog = True

    def close_dialog(self, players, screen):
        if self.checkProximity(players, screen): self.openDialog = False