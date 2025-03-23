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

class Player:
    def __init__(self, x, y, image_path, color):

        self.score = 0
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
        self.orientation = "D"
        self.curso = ""
        self.personagem = ""
        self.nome = ""
    

    def draw(self, screen):
        self.setImage()
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)  # Resize
        screen.blit(self.image, self.rect)  # Draw player image

    def change_rect(self, x, y):
        self.rect = self.image.get_rect(topleft=(x, y))

    def setImage(self):
        if self.orientation == "U": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/characters/Default1/Default1_back.png").convert_alpha()
        elif self.orientation == "D": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/characters/Default1/Default1_front.png").convert_alpha()
        elif self.orientation == "L": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/characters/Default1/Default1_left.png").convert_alpha()
        elif self.orientation == "R": self.image = pygame.image.load("iscte-sintra-simulator/assets/images/characters/Default1/Default1_right.png").convert_alpha()
        
    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
        
    def get_personagem(self):
        return self.personagem
    
    def set_personagem(self, nova_persona):
        self.personagem = nova_persona
        
    def get_curso(self):
        return self.curso
    
    def set_curso(self,novo_curso):
        self.curso = novo_curso
        
        
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
            
            if isinstance(structure, pygame.Rect):
                if structure.collidepoint(new_rect.midbottom): return True
            elif structure.rect.collidepoint(new_rect.midbottom): return True

            # if new_rect.colliderect(structure):
            #     return True  # Collision detected
        return False  # No collision
    
    def add_score(self, amount):
        self.score += amount

    def get_score(self):
        return self.score
    
    def reset_score(self):
        self.score = 0
        

    @staticmethod
    def draw_score(player1, screen):
        font = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 30)
        coin_image = pygame.image.load("iscte-sintra-simulator/assets/images/coin.png").convert_alpha()
        coin_image = pygame.transform.scale(coin_image, (30, 30))
        score_text = font.render(f"{player1.get_score()}", True, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        screen.blit(coin_image, (score_text.get_width() + 30, 20))
        
    def draw_score_end_day(player1,screen):
        font = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 30)

        score_text = font.render(f"{player1.get_score()}", True, (0, 0, 0))
        screen.blit(score_text, (600, 350))
