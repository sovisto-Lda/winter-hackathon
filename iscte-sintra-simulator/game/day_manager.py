import pygame
from characters.players.player import Player

class DayManager:
    def __init__(self, screen, player1, start_day=1):
        self.current_day = start_day
        self.screen = screen
        self.player1 = player1
         # For example, the game lasts 7 days
        
    def next_day(self):
        """Advances to the next day, wrapping around after max_days."""
        self.current_day += 1
        # if self.current_day > self.max_days:
        #     return "end game" # Wrap around back to day 1

    def get_current_day(self):
        return self.current_day

    def is_activity_allowed(self, activity_day):
        """Check if a specific activity can happen on the current day."""
        return self.current_day == activity_day
    
    def show_end_day(self):
        
        pygame.init()
        
        clock = pygame.time.Clock()
        
        running = True

        self.screen.fill((0,0,0))

        #fundos de final de dia
        fim_dia1 = pygame.image.load("iscte-sintra-simulator/assets/images/dias/fim do dia 1.png").convert_alpha()
        fim_dia1 = pygame.transform.scale(fim_dia1, (1280, 720))
        
        fim_dia2 = pygame.image.load("iscte-sintra-simulator/assets/images/dias/fim do dia 2.png").convert_alpha()
        fim_dia2 = pygame.transform.scale(fim_dia2, (1280, 720))
        
        fim_dia3 = pygame.image.load("iscte-sintra-simulator/assets/images/dias/fim do dia 3.png").convert_alpha()
        fim_dia3 = pygame.transform.scale(fim_dia3, (1280, 720))
        
        #nextday button
        nextday_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/dia seguinte.png").convert_alpha()
        nextday_image = pygame.transform.scale(nextday_image, (int(nextday_image.get_width() * .75), int(nextday_image.get_height() * .75)))
        nextday_rect = nextday_image.get_rect()  # Set position
        nextday_rect.centerx = 640
        nextday_rect.centery = 512
        
        #leaderboard button
        leaderboard_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/leaderboard.png").convert_alpha()
        leaderboard_image = pygame.transform.scale(leaderboard_image, (int(leaderboard_image.get_width() * .75), int(leaderboard_image.get_height() * .75)))
        leaderboard_rect = leaderboard_image.get_rect()  # Set position
        leaderboard_rect.centerx = 640
        leaderboard_rect.centery = 512
        
        


            
        pygame.display.flip()
    
        
            
        while running:
            self.screen.fill((0,0,0))
            
            if self.get_current_day() == 1:
                self.screen.blit(fim_dia1,(0,0))
                self.screen.blit(nextday_image, nextday_rect)
                Player.draw_score_end_day(self.player1, self.screen)
            
            elif self.get_current_day() == 2:
                self.screen.blit(fim_dia2, (0,0))
                self.screen.blit(nextday_image, nextday_rect)
                Player.draw_score_end_day(self.player1, self.screen)
                
            elif self.get_current_day() == 3:
                self.screen.blit(fim_dia3, (0,0))
                self.screen.blit(leaderboard_image, leaderboard_rect)


            pygame.display.flip()
        
            mouse_pos = pygame.mouse.get_pos()

            if nextday_rect.collidepoint(mouse_pos):
                nextday_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/dia seguinte_pressed.png").convert_alpha()
                nextday_image = pygame.transform.scale(nextday_image, (int(nextday_image.get_width() * .75), int(nextday_image.get_height() * .75)))
            else:
                nextday_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/dia seguinte.png").convert_alpha()
                nextday_image = pygame.transform.scale(nextday_image, (int(nextday_image.get_width() * .75), int(nextday_image.get_height() * .75)))
                clock.tick(30)
                
            if leaderboard_rect.collidepoint(mouse_pos):
                leaderboard_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/leaderboard_pressed.png").convert_alpha()
                leaderboard_image = pygame.transform.scale(leaderboard_image, (int(leaderboard_image.get_width() * .75), int(leaderboard_image.get_height() * .75)))
            else:
                leaderboard_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/leaderboard.png").convert_alpha()
                leaderboard_image = pygame.transform.scale(leaderboard_image, (int(leaderboard_image.get_width() * .75), int(leaderboard_image.get_height() * .75)))
                clock.tick(30)
                
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if nextday_rect.collidepoint(event.pos):
                        print("Dia Seguinte")
                        
                        self.next_day()

                        return "inicio do dia"  # Transition to the next scene
                    
                    if leaderboard_rect.collidepoint(event.pos):
                        return "leaderboard"
                        
        pygame.display.flip()
       
        
    def show_begin_day(self):
        pygame.init()
        
        clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        running = True

        self.screen.fill((0,0,0))

        #imagens dos dias
        inicio_dia1 = pygame.image.load("iscte-sintra-simulator/assets/images/dias/inicio dia 1.png").convert_alpha()
        inicio_dia1 = pygame.transform.scale(inicio_dia1, (1280, 720))
        
        inicio_dia2 = pygame.image.load("iscte-sintra-simulator/assets/images/dias/inicio dia 2.png").convert_alpha()
        inicio_dia2 = pygame.transform.scale(inicio_dia2, (1280, 720))
        
        inicio_dia3 = pygame.image.load("iscte-sintra-simulator/assets/images/dias/inicio dia 3.png").convert_alpha()
        inicio_dia3 = pygame.transform.scale(inicio_dia3, (1280, 720))
        
        leaderboard_image = pygame.image.load("iscte-sintra-simulator/assets/images/dias/leaderboard.png").convert_alpha()
        leaderboard_image = pygame.transform.scale(leaderboard_image, (1280, 720))

        #start button
        start_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/comecar.png").convert_alpha()
        start_game_image = pygame.transform.scale(start_game_image, (int(start_game_image.get_width() * .75), int(start_game_image.get_height() * .75)))
        start_game_rect = start_game_image.get_rect()  # Set position
        start_game_rect.centerx = 640
        start_game_rect.centery = 512
        
        #exit button
        exit_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/sair.png").convert_alpha()
        exit_game_image = pygame.transform.scale(exit_game_image, (int(exit_game_image.get_width() * .75), int(exit_game_image.get_height() * .75)))
        exit_game_rect = exit_game_image.get_rect()  # Set position
        exit_game_rect.centerx = 1050 
        exit_game_rect.centery = 200
    
    
        
                
        while running:
            # Clear the skin
            self.screen.fill((0,0,0))
            if self.get_current_day() == 1:
                self.screen.blit(inicio_dia1,(0,0))
                self.screen.blit(start_game_image, start_game_rect)
            elif self.get_current_day() == 2:
                self.screen.blit(inicio_dia2,(0,0))
                self.screen.blit(start_game_image, start_game_rect)
                
            elif self.get_current_day() == 3:
                self.screen.blit(inicio_dia3, (0,0))
                self.screen.blit(start_game_image, start_game_rect)
            else:
                self.screen.blit(leaderboard_image, (0,0))
                self.screen.blit(exit_game_image, exit_game_rect)

                
            pygame.display.flip()
            
            mouse_pos = pygame.mouse.get_pos()
        
            if start_game_rect.collidepoint(mouse_pos):
                start_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/comecar_pressed.png").convert_alpha()
                start_game_image = pygame.transform.scale(start_game_image, (int(start_game_image.get_width() * .75), int(start_game_image.get_height() * .75)))
            else:
                start_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/comecar.png").convert_alpha()
                start_game_image = pygame.transform.scale(start_game_image, (int(start_game_image.get_width() * .75), int(start_game_image.get_height() * .75)))
                clock.tick(30)
                
                
            if exit_game_rect.collidepoint(mouse_pos):
                exit_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/sair_pressed.png").convert_alpha()
                exit_game_image = pygame.transform.scale(exit_game_image, (int(exit_game_image.get_width() * .75), int(exit_game_image.get_height() * .75)))
            else:
                exit_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/sair.png").convert_alpha()
                exit_game_image = pygame.transform.scale(exit_game_image, (int(exit_game_image.get_width() * .75), int(exit_game_image.get_height() * .75)))
            
            clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if start_game_rect.collidepoint(event.pos):
                        
                        print("Comecar")
                        
                        print(self.get_current_day())
                        
                        if self.get_current_day() == 1:
                            return "play cutscene 1"  # Transition to the next scene
                        
                        elif self.get_current_day() == 2:
                            return "play cutscene 3"
                        
                        elif self.get_current_day() == 3:
                            return "play cutscene 5"
                        
                    elif exit_game_rect.collidepoint(event.pos):
                        print("Fechar jogo")
                        exit()
                        return
            pygame.display.flip()