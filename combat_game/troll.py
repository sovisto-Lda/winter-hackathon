# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


character_img = pygame.image.load("..\Trollface.png")
character_img = pygame.transform.scale(character_img, (50, 50))  # Resize if needed


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    screen.blit(character_img, (0, 0))


    clock.tick(60)  # limits FPS to 60

pygame.quit()