import sys
import os
import pygame
from characters.players.player import Player

# Add the parent directory of the 'characters' module to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1280, 720
WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (119, 221, 119), (255, 105, 97)
FONT = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 16)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Relações Sociais em PGP")


class Minigame4:
    def __init__(self, screen, player1):
        self.screen = screen
        self.player1 = player1
        
    def draw_text(self, text, x, y, color=BLACK):
        screen.blit(FONT.render(text, True, color), (x, y))
    
    def load_images(self, folder):
        image_files = [img for img in os.listdir(folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
        images = [pygame.image.load(os.path.join(folder, img)).convert_alpha() for img in image_files]
        images = [pygame.transform.scale(img, (WIDTH, HEIGHT)) for img in images]
        return images, image_files
    
    def display_images(self, images, display_times):
        image_index = 0
        last_image_change_time = pygame.time.get_ticks()
        running = True
        
        while running:
            current_time = pygame.time.get_ticks()
            
            # Clear the screen
            screen.fill(WHITE)
            
            # Display the current image
            screen.blit(images[image_index], (0, 0))
            
            # Check if it's time to change the image
            if current_time - last_image_change_time > display_times[image_index]:
                image_index += 1
                if image_index >= len(images):
                    running = False
                    break
                last_image_change_time = current_time
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            pygame.time.Clock().tick(30)
        
        # Display the last image as the background screen
        screen.blit(images[-1], (0, 0))
        pygame.display.flip()
        
        # Keep the last image displayed
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.time.Clock().tick(30)
    
    def load(self):
        # Display initial set of images
        filme_folder = "C:/Users/vasco/Desktop/hackathon/iscte-sintra-simulador-clone/winter-hackathon/iscte-sintra-simulator/assets/images/minigame4/filme"
        filme_images, _ = self.load_images(filme_folder)
        filme_display_times = [1000, 1000] + [1000] * (len(filme_images) - 2)
        self.display_images(filme_images, filme_display_times)

screen = pygame.display.set_mode((1280, 720))
player1 = Player(800, 160, "iscte-sintra-simulator/assets/images/characters/Default1/Default1_front 1.png", (0,0,0))
mg4 = Minigame4(screen, player1)
mg4.load()