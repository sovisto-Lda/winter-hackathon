import pygame
from ..structure import Structure
#from ...minigames.test_minigame import testMinigame


class InteractiveStructure(Structure):

    def __init__(self, x, y, image_path, scale_multiplier, screen):
        super().__init__(x, y, image_path, scale_multiplier)

        self.screen = screen

        self.isInteracting = False

    def checkProximity(self, players):
        for player in players:
            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery

            if (dx*dx + dy*dy < 10000): 
                self.isInteracting = True
                return True
            else: 
                self.isInteracting = False
        return False

    def interact(self):
        active_box = None
        box = pygame.Rect(5, 5, 100, 100)
        print(self.isInteracting)
        if (self.isInteracting == False): return
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and box.collidepoint(event.pos):
                        print('clicking')
                        active_box = box
                        # Calculate the offset from the top-left corner of the box to where the mouse clicked
                        offset_x = event.pos[0] - box.x
                        offset_y = event.pos[1] - box.y

                if event.type == pygame.MOUSEMOTION:
                    if active_box != None:
                        # Update the position of the box based on the mouse's movement
                        box.x = event.pos[0] - offset_x
                        box.y = event.pos[1] - offset_y
                        print('moving')

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        active_box = None

            # fill the screen with a color to wipe away anything from the last frame
            self.screen.fill("white")

            # Draw the box
            pygame.draw.rect(self.screen, (0, 0, 0), box)

            # Check for escape key to stop the interaction
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False

            # flip() the display to put your work on screen
            pygame.display.flip()

        return