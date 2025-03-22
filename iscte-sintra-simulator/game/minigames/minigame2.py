import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1280, 720
WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (119, 221, 119), (255, 105, 97)
FONT = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 16)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testem as vossas memórias!")

def generate_sequence(length=5):
    return "".join(random.choices("ABCDEFG12345", k=length))




class Minigame2:
    def __init__(self, screen, player1):
        self.screen = screen
        self.player1 = player1
        
    def draw_text(self, text, x, y, color=BLACK):
        screen.blit(FONT.render(text, True, color), (x, y))
    
    def load(self):
        sequence = "" 
        player_input = ""
        game_phase = "rules"
        score = 0
        result_message = ""
        
        
        clock = pygame.time.Clock()
        running = True
        
        sequence = generate_sequence()
        
        image0 = pygame.image.load("iscte-sintra-simulator/assets/images/minigame2/minigame2_explain.png").convert_alpha()
        image1 = pygame.image.load("iscte-sintra-simulator/assets/images/minigame2/minigame2_1.png").convert_alpha()
        image2 = pygame.image.load("iscte-sintra-simulator/assets/images/minigame2/minigame2_2.png").convert_alpha()
        image3 = pygame.image.load("iscte-sintra-simulator/assets/images/minigame2/minigame2_3.png").convert_alpha()
        
        # Scale images to fit the screen
        image0 = pygame.transform.scale(image0, (WIDTH, HEIGHT))
        image1 = pygame.transform.scale(image1, (WIDTH, HEIGHT))
        image2 = pygame.transform.scale(image2, (WIDTH, HEIGHT))
        image3 = pygame.transform.scale(image3, (WIDTH, HEIGHT))
        
        # #background
        # bg_image = pygame.image.load("iscte-sintra-simulator/assets/images/SALA MULTIUSOS/ISS_Sala_Multiusos col_MULTIUSOS escura.png").convert_alpha()
        # bg_image = pygame.transform.scale(bg_image, (int(bg_image.get_width() * 3), int(bg_image.get_height() * 3)))
        # bg_rect = bg_image.get_rect()  # Set position
        # bg_rect.topleft = (200,70)
        
        #play button
        play_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/jogar.png").convert_alpha()
        play_game_image = pygame.transform.scale(play_game_image, (int(play_game_image.get_width() * .75), int(play_game_image.get_height() * .75)))
        play_game_rect = play_game_image.get_rect()  # Set position
        play_game_rect.centerx = 636
        play_game_rect.centery = 512
        
        #Submit button
        avancar_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/avancar_bota.png").convert_alpha()
        avancar_game_image = pygame.transform.scale(avancar_game_image, (int(avancar_game_image.get_width() * .75), int(avancar_game_image.get_height() * .75)))
        avancar_game_rect = avancar_game_image.get_rect()  # Set position
        avancar_game_rect.centerx = 636
        avancar_game_rect.centery = 512
        
        
        # Sair button
        exit_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/sair.png").convert_alpha()
        exit_game_image = pygame.transform.scale(exit_game_image, (int(exit_game_image.get_width() * .75), int(exit_game_image.get_height() * .75)))
        exit_game_rect = exit_game_image.get_rect()  # Set position
        exit_game_rect.centerx = 636
        exit_game_rect.centery = 512
        
        
        while running:
            # Clear the skin
            screen.fill(WHITE)
            if game_phase == "rules":
                screen.blit(image0,(0,0))
                screen.blit(play_game_image, play_game_rect)
                pygame.display.flip()
        
            elif game_phase == "repeat":
                screen.blit(image2, (0,0))
                screen.blit(avancar_game_image, avancar_game_rect)
                pygame.display.flip()
                
                
            elif game_phase == "results":
                screen.blit(image3, (0,0))
                screen.blit(exit_game_image, exit_game_rect)
                pygame.display.flip()


            mouse_pos = pygame.mouse.get_pos()
        
            if play_game_rect.collidepoint(mouse_pos):
                play_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/jogar_pressed.png").convert_alpha()
                play_game_image = pygame.transform.scale(play_game_image, (int(play_game_image.get_width() * .75), int(play_game_image.get_height() * .75)))
            else:
                play_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/jogar.png").convert_alpha()
                play_game_image = pygame.transform.scale(play_game_image, (int(play_game_image.get_width() * .75), int(play_game_image.get_height() * .75)))
            
            if avancar_game_rect.collidepoint(mouse_pos):
                avancar_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/avancar_botao_pressed.png").convert_alpha()
                avancar_game_image = pygame.transform.scale(avancar_game_image, (int(avancar_game_image.get_width() * .75), int(avancar_game_image.get_height() * .75)))
            else:
                avancar_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/avancar_bota.png").convert_alpha()
                avancar_game_image = pygame.transform.scale(avancar_game_image, (int(avancar_game_image.get_width() * .75), int(avancar_game_image.get_height() * .75)))
            
            if exit_game_rect.collidepoint(mouse_pos):
                exit_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/sair_pressed.png").convert_alpha()
                exit_game_image = pygame.transform.scale(exit_game_image, (int(exit_game_image.get_width() * .75), int(exit_game_image.get_height() * .75)))
            else:
                exit_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/sair.png").convert_alpha()
                exit_game_image = pygame.transform.scale(exit_game_image, (int(exit_game_image.get_width() * .75), int(exit_game_image.get_height() * .75)))
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                
                if event.type == pygame.QUIT:
                    running = False        
                
                if game_phase == "rules":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if play_game_rect.collidepoint(event.pos):
                            print("Jogar")
                            game_phase = "show_sequence"
                    
                if game_phase == "show_sequence":
                    screen.blit(image1, (0, 0))  # Show the "show sequence" image
                    self.draw_text(sequence, 500, 250)
                    pygame.display.flip()
                    
                    pygame.time.wait(6000)  # Wait for 6 seconds
                    
                    game_phase = "repeat"
                    player_input = ""
                
                elif game_phase == "repeat" and event.type == pygame.KEYDOWN:
                    if event.unicode.isprintable():
                        print(f"Key pressed: {event.unicode}")
                        player_input += event.unicode
                        
                        if player_input == sequence[:len(player_input)]:
                            print("Correct so far!")  # Debugging line
                            
                        else:
                            print("Incorrect input!")
                    
                elif game_phase == "repeat" and event.type == pygame.MOUSEBUTTONDOWN:
                    if avancar_game_rect.collidepoint(event.pos):
                        print("avançar")
                        final_player_input = player_input
                        if final_player_input == sequence:
                            score +=1
                        game_phase = "results"
                            
                elif game_phase == "results" and event.type == pygame.MOUSEBUTTONDOWN:
                    # Wait for the player to press space to go to the "end" phase
                    if exit_game_rect.collidepoint(event.pos):
                            print("Sair")
                            game_phase = "end"
        
            
            if game_phase == "repeat":
                self.draw_text(player_input, 550, 270)
            
            if game_phase == "results":
                if score > 0:
                        result_message = "Ganhaste!"
                else:
                    result_message = "Perdeste... É uma pena!"
                
                self.draw_text(result_message, 300, 270)
                
            if game_phase =="end":
                return "go to uata"

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()
        
