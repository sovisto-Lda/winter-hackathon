import os
import pygame

os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

def MainMenu(screen):
    pygame.init()

    pygame.font.init() 
    myfont = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 30)

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    #title
    image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/title.png").convert_alpha()  # Load image safely
    image = pygame.transform.scale(image, (int(image.get_width() * 2), int(image.get_height() * 2)))
    rect = image.get_rect()  # Set position
    rect.centerx = 640
    rect.centery = 120

    #play button
    play_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/play_game_button.png").convert_alpha()  # Load image safely
    play_game_image = pygame.transform.scale(play_game_image, (int(play_game_image.get_width() * 0.5), int(play_game_image.get_height() * 0.5)))
    play_game_rect = play_game_image.get_rect()  # Set position
    play_game_rect.centerx = 640
    play_game_rect.centery = 350



    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if play_game_rect.collidepoint(event.pos):
                    print("cenas")

            if event.type == pygame.QUIT:
                running = False              

        screen.fill("white")

        keys = pygame.key.get_pressed()

        screen.blit(image, rect)  # Draw player image
        screen.blit(play_game_image, play_game_rect)

     
        pygame.display.flip()

        dt = clock.tick(60) / 1000




    pygame.quit()

screen = pygame.display.set_mode((1280, 720))

MainMenu(screen)