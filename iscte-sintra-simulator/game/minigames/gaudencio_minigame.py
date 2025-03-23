import os
import pygame
from characters.players.gaudencio import Gaudencio


os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

class GaudencioMinigame:
    def __init__(self, screen, player1):
        self.screen = screen
        self.player1 = player1
    
    def load(self):
        pygame.init()

        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        screen.fill((0,0,0))

        start_time = pygame.time.get_ticks()

        #background
        bg_image = pygame.image.load("iscte-sintra-simulator/assets/images/SALA AULA/ISS_Sala_Aula.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, (int(bg_image.get_width() * 3), int(bg_image.get_height() * 3)))
        bg_rect = bg_image.get_rect()  # Set position
        bg_rect.topleft = (200,70)

        gaudencio = Gaudencio(380, 160, "iscte-sintra-simulator/assets/images/characters/gaudencio/gaudencio_front.png", (0,0,0))

        myfont = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 30)
        titleText = myfont.render('Copia BEM!', False, (220, 220, 220))

        maxpoints = 10000

        player1_progress_bar = ProgressBar(x=300, y=675, width=200, height=20, max_points=maxpoints)

        player1_points = 0

        popup_image = pygame.image.load("iscte-sintra-simulator/assets/images/dialogs/gaudencio1.png").convert_alpha()
        popup_image = pygame.transform.scale(popup_image, (int(popup_image.get_width() * .85), int(popup_image.get_height() * .85)))
        popup_rect = popup_image.get_rect()  # Set position
        popup_rect.centerx = 620
        popup_rect.centery = 500

        # Popup timer
        popup_duration = 8000
        popup_start_time = None  # Track when the popup starts


        popup_start_time = pygame.time.get_ticks()  # Record start time

        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                
                if event.type == pygame.QUIT:
                    running = False         

                gaudencio.handle_event(event)  # Handle turning event     
            

            screen.fill((50, 50, 50))

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                if not player1_points >= maxpoints:
                    if gaudencio.orientation == "U":
                        player1_points += 100
                        player1_progress_bar.update(player1_points)
                    else:
                        player1_points -= 25
                        if player1_points < 0: player1_points = 0
                        player1_progress_bar.update(player1_points)

            
            screen.blit(bg_image, bg_rect)
            gaudencio.move(screen)

            gaudencio.draw(screen)

            player1_progress_bar.draw(screen)

            if(player1_points >= maxpoints):
                print('Felicidade')

                end_time = pygame.time.get_ticks()
                elapsed_time = (end_time - start_time) / 1000
                self.player1.score += max(10, int(200 - elapsed_time))

                dialog_image = pygame.image.load("iscte-sintra-simulator/assets/images/dialogs/fimDoDia2.png").convert_alpha()

                dialog_image = pygame.transform.scale(dialog_image, (int(dialog_image.get_width() * .35), int(dialog_image.get_height() * .35)))
                dialog_rect = bg_image.get_rect()  # Set position
                dialog_rect.center = (570, 620/2 + 42)

                play2_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/sair.png").convert_alpha()
                play2_game_image = pygame.transform.scale(play2_game_image, (int(play2_game_image.get_width() * .75), int(play2_game_image.get_height() * .75)))
                play2_game_rect = play2_game_image.get_rect()  # Set position
                play2_game_rect.centerx = 640
                play2_game_rect.centery = 510

                running2 = True
                while running2:
                    mouse_pos = pygame.mouse.get_pos()
                    # # print(mouse_pos)


                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print(event.pos)
                        
                            if play2_game_rect.collidepoint(event.pos):
                                running2 = False
                                return "fim do dia"


                    if play2_game_rect.collidepoint(mouse_pos):
                        play2_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/sair_pressed.png").convert_alpha()
                        play2_game_image = pygame.transform.scale(play2_game_image, (int(play2_game_image.get_width() * .75), int(play2_game_image.get_height() * .75)))
                    else:
                        play2_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/sair.png").convert_alpha()
                        play2_game_image = pygame.transform.scale(play2_game_image, (int(play2_game_image.get_width() * .75), int(play2_game_image.get_height() * .75)))

                    keys = pygame.key.get_pressed()

                    screen.blit(dialog_image, dialog_rect)
                    screen.blit(play2_game_image, play2_game_rect)


                    
                    pygame.display.flip()




            screen.blit(titleText, (525,25))



            if popup_start_time is not None:
                elapsed_time = pygame.time.get_ticks() - popup_start_time
                if elapsed_time < popup_duration:
                    screen.blit(popup_image, popup_rect)  # Draw popup
                else:
                    popup_start_time = None  # Reset after duration
                    dialog_image = pygame.image.load("iscte-sintra-simulator/assets/images/dialogs/gaudencio_minigame_dialog.png").convert_alpha()

                    dialog_image = pygame.transform.scale(dialog_image, (int(dialog_image.get_width() * .35), int(dialog_image.get_height() * .35)))
                    dialog_rect = bg_image.get_rect()  # Set position
                    dialog_rect.center = (570, 620/2 + 42)

                    play2_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/jogar.png").convert_alpha()
                    play2_game_image = pygame.transform.scale(play2_game_image, (int(play2_game_image.get_width() * .75), int(play2_game_image.get_height() * .75)))
                    play2_game_rect = play2_game_image.get_rect()  # Set position
                    play2_game_rect.centerx = 640
                    play2_game_rect.centery = 510

                    running2 = True
                    while running2:
                        mouse_pos = pygame.mouse.get_pos()
                        # # print(mouse_pos)


                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                print(event.pos)
                            
                                if play2_game_rect.collidepoint(event.pos):
                                    running2 = False


                        if play2_game_rect.collidepoint(mouse_pos):
                            play2_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/jogar_pressed.png").convert_alpha()
                            play2_game_image = pygame.transform.scale(play2_game_image, (int(play2_game_image.get_width() * .75), int(play2_game_image.get_height() * .75)))
                        else:
                            play2_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/jogar.png").convert_alpha()
                            play2_game_image = pygame.transform.scale(play2_game_image, (int(play2_game_image.get_width() * .75), int(play2_game_image.get_height() * .75)))

                        keys = pygame.key.get_pressed()

                        screen.blit(dialog_image, dialog_rect)
                        screen.blit(play2_game_image, play2_game_rect)


                        
                        pygame.display.flip()



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



# def load():
#     screen = pygame.display.set_mode((1280, 720))
#     GaudencioMinigame(screen)