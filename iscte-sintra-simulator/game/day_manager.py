import pygame

class DayManager:
    def __init__(self, start_day=1):
        self.current_day = start_day
        self.max_days = 3  # For example, the game lasts 7 days
        
    def next_day(self):
        """Advances to the next day, wrapping around after max_days."""
        self.current_day += 1
        if self.current_day > self.max_days:
            return "end game" # Wrap around back to day 1

    def get_current_day(self):
        return self.current_day

    def is_activity_allowed(self, activity_day):
        """Check if a specific activity can happen on the current day."""
        return self.current_day == activity_day
    
    def show_end_day(self):
        
        pygame.init()
        
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((1280, 720))
        running = True

        screen.fill((0,0,0))

        #fundos de final de dia
        fim_dia1 = pygame.image.load("iscte-sintra-simulator/assets/images/dias/fim do dia 1.png").convert_alpha()
        fim_dia1 = pygame.transform.scale(fim_dia1, (1280, 720))
        
        
        #nextday button
        nextday_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/dia seguinte.png").convert_alpha()
        nextday_image = pygame.transform.scale(nextday_image, (int(nextday_image.get_width() * .75), int(nextday_image.get_height() * .75)))
        nextday_rect = nextday_image.get_rect()  # Set position
        nextday_rect.centerx = 640
        nextday_rect.centery = 512
        
        if self.get_current_day() == 1:
            screen.blit(fim_dia1,(0,0))
            screen.blit(nextday_image, nextday_rect)

            
        pygame.display.flip()
    
        
            
        while running:
            mouse_pos = pygame.mouse.get_pos()

            if nextday_rect.collidepoint(mouse_pos):
                nextday_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/dia seguinte_pressed.png").convert_alpha()
                nextday_image = pygame.transform.scale(nextday_image, (int(nextday_image.get_width() * .75), int(nextday_image.get_height() * .75)))
            else:
                nextday_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/dia seguinte.png").convert_alpha()
                nextday_image = pygame.transform.scale(nextday_image, (int(nextday_image.get_width() * .75), int(nextday_image.get_height() * .75)))
                clock.tick(30)
                
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if nextday_rect.collidepoint(event.pos):
                            print("Dia Seguinte")
                            self.next_day()
                            return "inicio do dia"  # Transition to the next scene
                
        
    def show_begin_day(self):
        pygame.init()
        
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((1280, 720))
        running = True

        screen.fill((0,0,0))

        #imagens dos dias
        inicio_dia1 = pygame.image.load("iscte-sintra-simulator/assets/images/dias/inicio dia 1.png").convert_alpha()
        inicio_dia1 = pygame.transform.scale(inicio_dia1, (1280, 720))
        
        inicio_dia2 = pygame.image.load("iscte-sintra-simulator/assets/images/dias/inicio dia 2.png").convert_alpha()
        inicio_dia2 = pygame.transform.scale(inicio_dia2, (1280, 720))
        
        
        #start button
        start_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/comecar.png").convert_alpha()
        start_game_image = pygame.transform.scale(start_game_image, (int(start_game_image.get_width() * .75), int(start_game_image.get_height() * .75)))
        start_game_rect = start_game_image.get_rect()  # Set position
        start_game_rect.centerx = 640
        start_game_rect.centery = 512
    
    
        
                
        while running:
            # Clear the skin
            screen.fill((0,0,0))
            if self.get_current_day() == 1:
                screen.blit(inicio_dia1,(0,0))
                screen.blit(start_game_image, start_game_rect)
            elif self.get_current_day() == 2:
                screen.blit(inicio_dia2,(0,0))
                screen.blit(start_game_image, start_game_rect)
                
    
                
            pygame.display.flip()
            mouse_pos = pygame.mouse.get_pos()
        
            if start_game_rect.collidepoint(mouse_pos):
                start_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/comecar_pressed.png").convert_alpha()
                start_game_image = pygame.transform.scale(start_game_image, (int(start_game_image.get_width() * .75), int(start_game_image.get_height() * .75)))
            else:
                start_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/botoes/comecar.png").convert_alpha()
                start_game_image = pygame.transform.scale(start_game_image, (int(start_game_image.get_width() * .75), int(start_game_image.get_height() * .75)))
                clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if start_game_rect.collidepoint(event.pos):
                        print("Comecar")
                        print(self.get_current_day())
                        if self.get_current_day() == 1:
                            return "play cutscene 1"  # Transition to the next scene
                        else:
                            return "go to entrada - day begin"
        