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


    image = pygame.image.load("iscte-sintra-simulator/assets/images/menu_title.png").convert_alpha()  # Load image safely
    image = pygame.transform.scale(image, (int(image.get_width() * 2), int(image.get_height() * 2)))
    rect = image.get_rect()  # Set position
    rect.centerx = 640
    rect.centery = 120


    play_button = myfont.render('Play Game', False, (0, 0, 0))
    play_rect = play_button.get_rect()
    play_rect.centerx = 640
    play_rect.centery = 350

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if play_rect.collidepoint(event.pos):
                    print("cenas")

            if event.type == pygame.QUIT:
                running = False              

        screen.fill("white")

        keys = pygame.key.get_pressed()

        screen.blit(image, rect)  # Draw player image
        screen.blit(play_button, play_rect)

     
        pygame.display.flip()

        dt = clock.tick(60) / 1000




    pygame.quit()