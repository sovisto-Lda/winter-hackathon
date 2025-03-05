import pygame
from player import Player
import os

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PLAYER_SIZE = (50, 50)
VEL = 5
ATTACK_DAMAGE = 10
PROJECTILE_SPEED = 7
FONT = pygame.font.Font(None, 50)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Combat Game")

# Player class

# Game over screen
def game_over(winner):
    screen.fill(WHITE)
    text = FONT.render(f"{winner} Wins! Press R to Restart", True, BLACK)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False

# Main game function
def main():
    clock = pygame.time.Clock()
    run = True

    # Initialize players with images
    player1 = Player(100, HEIGHT//2, "images/bat.png", RED)
    player2 = Player(WIDTH-150, HEIGHT//2, "images/bat.png", BLUE)

    while run:
        clock.tick(60)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        player1.move(keys, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        player2.move(keys, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        
        # Throw projectiles
        if keys[pygame.K_SPACE]:
            player1.throw_projectile('right')
        if keys[pygame.K_RETURN]:
            player2.throw_projectile('left')
        
        # Update projectiles
        player1.update_projectiles(player2)
        player2.update_projectiles(player1)
        
        # Draw players and projectiles
        player1.draw(screen)
        player2.draw(screen)
        
        # Draw health bars
        pygame.draw.rect(screen, RED, (50, 50, player1.health * 2, 20))
        pygame.draw.rect(screen, BLUE, (WIDTH - 250, 50, player2.health * 2, 20))
        
        # Check win condition
        if player1.health <= 0:
            game_over("Blue Player")
            return main()
        if player2.health <= 0:
            game_over("Red Player")
            return main()
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()