import os
import pygame
from characters.players.player import Player
from characters.players.gaudencio import Gaudencio
from characters.npcs.npc import NPC
from structures.static_structures.table_multiusos import TableMultiusos



os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

def GaudencioMinigame(screen):
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    screen.fill((0,0,0))


    gaudencio = Gaudencio(100, 50//2, "iscte-sintra-simulator/assets/images/gaudencio.png", (0,0,0))

    player1 = Player(100, 50//2, "iscte-sintra-simulator/assets/images/player1_PH.png", (0,0,0))

    colidables = []

    player1_progress_bar = ProgressBar(x=50, y=350, width=200, height=20, max_points=10000)
    player2_progress_bar = ProgressBar(x=1050, y=350, width=200, height=20, max_points=10000)

    player1_points = 0
    player2_points = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
               
            if event.type == pygame.QUIT:
                running = False         

            gaudencio.handle_event(event)  # Handle turning event     

        screen.fill("white")

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if gaudencio.orientation == "U":
                player1_points += 10
                player1_progress_bar.update(player1_points)
            else:
                player1_points -= 50
                if player1_points < 0: player1_points = 0
                player1_progress_bar.update(player1_points)

        if keys[pygame.K_RETURN]:
            if gaudencio.orientation == "U":
                player2_points += 10
                player2_progress_bar.update(player2_points)
            else:
                player2_points -= 50
                if player2_points < 0: player2_points = 0
                player2_progress_bar.update(player2_points)


        
        player1.move(keys, colidables)

        gaudencio.move(screen)

        gaudencio.draw(screen)
        player1.draw(screen)

        player1_progress_bar.draw(screen)
        player2_progress_bar.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


    pygame.quit()


class ProgressBar:
    def __init__(self, x, y, width, height, max_points):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_points = max_points  # Maximum value
        self.current_points = 0  # Start at 0

    def update(self, new_points):
        """Update progress based on new points"""
        self.current_points = max(0, min(new_points, self.max_points))  # Clamp value

    def draw(self, screen):
        """Draw the progress bar"""
        # Background bar (gray)
        pygame.draw.rect(screen, (100, 100, 100), (self.x, self.y, self.width, self.height))

        # Foreground bar (green)
        fill_width = (self.current_points / self.max_points) * self.width
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, fill_width, self.height))

        # Optional: Border
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)




screen = pygame.display.set_mode((1280, 720))
GaudencioMinigame(screen)