import os
import pygame

class LeaderBoard:
    def __init__(self, screen):
        self.file = "iscte-sintra-simulator/game/scores/scores.txt"
        self.leaderboard = []
        self.screen = screen
        
        
    def load_leaderboard(self):
        """Load the leaderboard from a text file or create it if it doesn't exist."""
        if not os.path.exists(self.file):
            print("FIle not found")
            return []
        
        # Clear the leaderboard before loading
        self.leaderboard = [] 
        
        with open(self.file, "r") as file:
            lines = file.readlines()
             
        for line in lines:
            if line.strip() == "":
                continue
            name, course, score = line.strip().split(";")
            self.leaderboard.append({"Nome": name, "Curso": course, "Pontuação": int(score)})
        
        return self.leaderboard
    
    def add_to_leaderboard(self, name, course, score):
        """Add a new player's score to the leaderboard file."""
        with open(self.file, "a") as file:
            file.write(f"{name};{course};{score}\n")
    
    def save_leaderboard(self):
        """Sort and print the top 10 players without overwriting the file."""
        # Sort the leaderboard by score in descending order
        self.leaderboard.sort(key=lambda x: x["Pontuação"], reverse=True)
        
        # Print the top 10
        for idx, entry in enumerate(self.leaderboard[:10], start=1):
            print(f"{idx}. {entry['Nome']} ({entry['Curso']}) — {entry['Pontuação']} pontos")
    
    def draw_text(self, text, x, y, color = (0,0,0)):
        FONT = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 16)
        self.screen.blit(FONT.render(text, True, color), (x, y))
                
    def show_leaderboard(self):
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        dt = 0

        self.screen.fill((0, 0, 0))

        image = pygame.image.load("iscte-sintra-simulator/assets/images/dias/leaderboard.png").convert_alpha()  # Load image safely
        image = pygame.transform.scale(image, (1280, 720))

        rect = image.get_rect()  # Set position
        rect.topleft = (0, 0)  # Position at the top-left corner
        
        # Load the leaderboard
        self.load_leaderboard()
        if not self.leaderboard:
            print("Leaderboard is empty!")
        
        self.save_leaderboard()


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Close the window if quit event happens
                # Add an exit condition on SPACE key or ESC key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                        running = False  # Exit on space or escape key

                self.screen.fill((0, 0, 0))  # Clear the screen
                self.screen.blit(image, rect)  # Draw the background image
                y_offset = 300  # Initialize y_offset for text placement

                # Draw top 10 leaderboard entries
                for idx, entry in enumerate(self.leaderboard[:10], start=1):
                    self.draw_text(f"{idx}. {entry['Nome']} ({entry['Curso']}) — {entry['Pontuação']} pontos", 350, y_offset)
                    y_offset += 30  # Space between entries

                pygame.display.flip()  # Update the display
                dt = clock.tick(60) / 1000  # Maintain frame rate

    pygame.quit()  # Cleanly exit pygame