import pygame

def testMinigame():

    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        pygame.display.fill("white")

        keys = pygame.key.get_pressed()

        if (keys == pygame.K_ESCAPE): running = False

        # flip() the display to put your work on screen
        pygame.display.flip()

    return

