import os
import pygame
from multiusos import Multiusos


os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

def MainMenu(screen):
    pygame.init()

    pygame.font.init() 
    myfont = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 30)

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    #background
    bg_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/background.png").convert_alpha()
    bg_image = pygame.transform.scale(bg_image, (int(bg_image.get_width() * .45), int(bg_image.get_height() * .45)))
    bg_rect = bg_image.get_rect()  # Set position
    bg_rect.topleft = (0,0)

    #title
    image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/title.png").convert_alpha()
    image = pygame.transform.scale(image, (int(image.get_width() * .9), int(image.get_height() * .9)))
    rect = image.get_rect()  # Set position
    rect.centerx = 640
    rect.centery = 275

    #play button
    play_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/jogar.png").convert_alpha()
    play_game_image = pygame.transform.scale(play_game_image, (int(play_game_image.get_width() * .75), int(play_game_image.get_height() * .75)))
    play_game_rect = play_game_image.get_rect()  # Set position
    play_game_rect.centerx = 640 - int(play_game_image.get_width()/2) - 25
    play_game_rect.centery = 450


    #load button
    exit_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/sair.png").convert_alpha()
    exit_game_image = pygame.transform.scale(exit_game_image, (int(exit_game_image.get_width() * .75), int(exit_game_image.get_height() * .75)))
    exit_game_rect = exit_game_image.get_rect()  # Set position
    exit_game_rect.centerx = 640 + int(exit_game_image.get_width()/2) + 25
    exit_game_rect.centery = 450



    while running:
        mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if play_game_rect.collidepoint(event.pos):
                    print("jogar")
                    Multiusos(screen)
                    return
                if exit_game_rect.collidepoint(event.pos):
                    print("sair")
                    exit()
                    return

            if event.type == pygame.QUIT:
                running = False   



        if play_game_rect.collidepoint(mouse_pos):
            play_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/jogar_pressed.png").convert_alpha()
            play_game_image = pygame.transform.scale(play_game_image, (int(play_game_image.get_width() * .75), int(play_game_image.get_height() * .75)))

        else:
            play_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/jogar.png").convert_alpha()
            play_game_image = pygame.transform.scale(play_game_image, (int(play_game_image.get_width() * .75), int(play_game_image.get_height() * .75)))


        if exit_game_rect.collidepoint(mouse_pos):
            exit_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/sair_pressed.png").convert_alpha()
            exit_game_image = pygame.transform.scale(exit_game_image, (int(exit_game_image.get_width() * .75), int(exit_game_image.get_height() * .75)))
        else:
            exit_game_image = pygame.image.load("iscte-sintra-simulator/assets/images/menu/sair.png").convert_alpha()
            exit_game_image = pygame.transform.scale(exit_game_image, (int(exit_game_image.get_width() * .75), int(exit_game_image.get_height() * .75)))
           

        screen.fill("white")

        keys = pygame.key.get_pressed()

        screen.blit(bg_image, bg_rect)

        screen.blit(image, rect)  # Draw player image
        screen.blit(play_game_image, play_game_rect)
        screen.blit(exit_game_image, exit_game_rect)


     
        pygame.display.flip()

        dt = clock.tick(60) / 1000




    pygame.quit()

screen = pygame.display.set_mode((1280, 720))

MainMenu(screen)