import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1280, 720
WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (119, 221, 119), (255, 105, 97)

FONT = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 16)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testem as vossas memórias!")

# Restricted keys (WASD, Arrows, ENTER, SPACE)
RESTRICTED_KEYS = {
    pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d,
    pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT,
    pygame.K_RETURN, pygame.K_SPACE
}

#Partida 1
sequence_p1 = ""  # Para a sequencia do player 1
player_input_p2 = ""  # Para a tentativa do player 2

#Partida 2g
sequence_p2 = ""  # Para a sequencia do player 2
player_input_p1 = ""  # Para a tentativa do player 1

score_p1, score_p2 = 0, 0 
game_phase = "input_p1"  # "input" → "repeat" → "result"
result_message = ""


def draw_text(text, x, y, color=BLACK):
    screen.blit(FONT.render(text, True, color), (x, y))


def open_dialog(screen, image):
        if image == 0: 
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/minigame2/minigame2_explain.png").convert_alpha()

        if image == 1:
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/minigame2/minigame2_1.png").convert_alpha()
        
        if image == 2:
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/minigame2/minigame2_2.png").convert_alpha()
            
        if image == 3:
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/minigame2/minigame2_3.png").convert_alpha()
            
        if image == 4:
            dialog = pygame.image.load("iscte-sintra-simulator/assets/images/minigame2/minigame2_4.png").convert_alpha()


        # dialog = pygame.transform.scale(dialog, (int(dialog.get_width() * 1.5), int(dialog.get_height() * 1.5)))
        dialog_rect = dialog.get_rect()  # Set position
        dialog_rect.centerx = 620
        dialog_rect.centery = 350
        screen.blit(dialog, dialog_rect)
        
        waiting = True
        while waiting:
            screen.fill(WHITE)
            screen.blit(dialog,dialog_rect)
            
            draw_text("Testem as vossas memórias!", 50, 20)
            draw_text("Pressiona ESPAÇO para continuar...", WIDTH // 2 - 100, HEIGHT - 100, BLACK)

            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False
        
# def close_dialog(self, players, screen):
#     if self.checkProximity(players, screen): self.openDialog = False

def main():
    global game_phase, sequence_p1, sequence_p2, player_input_p1, player_input_p2, score_p1, score_p2, result_message

    clock = pygame.time.Clock()
    running = True
    
    # Show initial explanation dialog before starting
    open_dialog(screen, 0)

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            

            # Player 1 inputs sequence
            if game_phase == "input_p1" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and sequence_p1:  # Press space to end player 1 sequence
                    open_dialog(screen, 1)  # Show dialog **once**
                    game_phase = "repeat_p2"
                    player_input_p2 = ""
                elif event.key not in RESTRICTED_KEYS and event.unicode.isprintable():
                    sequence_p1 += event.unicode
            
            elif game_phase == "repeat_p2" and event.type == pygame.KEYDOWN:
                if event.key not in RESTRICTED_KEYS and event.unicode.isprintable():
                    player_input_p2 += event.unicode
                    
                    # Check if Player 2 made a mistake
                    if player_input_p2 != sequence_p1[:len(player_input_p2)]:
                        score_p1 += 1
                        open_dialog(screen, 2)  # Show dialog **once**
                        game_phase = "input_p2"
                        sequence_p2 = ""
                        
                    elif player_input_p2 == sequence_p1:
                        open_dialog(screen, 2)
                        game_phase = "input_p2"
                        sequence_p2 = ""  # Reset for next round
                  
            elif game_phase == "input_p2" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and sequence_p2:  # End input
                    open_dialog(screen, 3)  # Show dialog **once**
                    game_phase = "repeat_p1"
                    player_input_p1 = ""
                elif event.key not in RESTRICTED_KEYS and event.unicode.isprintable():
                    sequence_p2 += event.unicode  # Store input (but don't display it)

            # Phase 4: Player 1 tries to repeat sequence_p2
            elif game_phase == "repeat_p1" and event.type == pygame.KEYDOWN:
                if event.key not in RESTRICTED_KEYS and event.unicode.isprintable():
                    player_input_p1 += event.unicode

                    # Check if Player 1 made a mistake
                    if player_input_p1 != sequence_p2[:len(player_input_p1)]:
                        score_p2 += 1  # Player 2 wins this round
                        open_dialog(screen, 4)  # Show dialog **once**
                        game_phase = "end"
                    elif player_input_p1 == sequence_p2:
                        open_dialog(screen, 4)  # Show dialog **once**
                        game_phase = "end"

        if game_phase == "end":
            if score_p1 > score_p2:
                result_message = "O jogador 1 ganha! Uma Sweat Iscte-Sintra para ti J1"
            elif score_p1 < score_p1:
                result_message = "O jogador 2 ganha! Uma Sweat Iscte-Sintra para ti J2"
            else:
                result_message = "Empate, ninguem recebe nada..."
        # UI Drawing
        draw_text("Testem as vossas memorias!", 50, 20)

        if game_phase == "input_p1":
            draw_text(sequence_p1, 50, 150)

        elif game_phase == "repeat_p2":
            draw_text(player_input_p2, 50, 150)

        elif game_phase == "input_p2":
            draw_text(sequence_p2, 50, 150)

        elif game_phase == "repeat_p1":
            draw_text(player_input_p1, 50, 150)

        elif game_phase == "end":
            draw_text(result_message, 200, 150, GREEN if "ganha"  in result_message else RED)
            draw_text("Jogo terminado!", 180, 250)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()





if __name__ == "__main__":
    main()