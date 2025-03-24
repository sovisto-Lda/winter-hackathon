import pygame

class Minigame1:
    def __init__(self, screen, player1):
        self.screen = screen
        self.player1 = player1

    def load(self):

        pygame.init()
        pygame.font.init() 
        myfont = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 30)

        WIDTH = 1280
        HEIGHT = 720

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        running = True

        BOXES_WIDTH = 100
        BOXES_HEIGHT = 50
        DRAGGABLE_POSITIONX = 250

        start_time = pygame.time.get_ticks()

        # Carregar o fundo
        bg_image = pygame.image.load("iscte-sintra-simulator/assets/images/Minigame1/minigame1.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
        bg_rect = bg_image.get_rect()
        bg_rect.topleft = (0, 0)

        submeterBox_image = pygame.image.load("iscte-sintra-simulator/assets/images/Minigame1/submeterBox.png").convert_alpha()
        submeterBox_image = pygame.transform.scale(submeterBox_image, (150, 50))
        submeterBox_rect = submeterBox_image.get_rect()
        submeterBox_rect.topleft = (970, 560)

        # Carregar imagens das caixas arrastáveis (baralhadas)
        draggable_images = [
            pygame.image.load("iscte-sintra-simulator/assets/images/Minigame1/returnBox.png").convert_alpha(),
            pygame.image.load("iscte-sintra-simulator/assets/images/Minigame1/printBox.png").convert_alpha(),
            pygame.image.load("iscte-sintra-simulator/assets/images/Minigame1/inputBox.png").convert_alpha(),
            pygame.image.load("iscte-sintra-simulator/assets/images/Minigame1/returnBox.png").convert_alpha(),
            pygame.image.load("iscte-sintra-simulator/assets/images/Minigame1/defBox.png").convert_alpha(),
            pygame.image.load("iscte-sintra-simulator/assets/images/Minigame1/defBox.png").convert_alpha(),
        ]

        # Redimensionar imagens
        draggable_images = [pygame.transform.scale(img, (BOXES_WIDTH, BOXES_HEIGHT)) for img in draggable_images]

        # Criar caixas de destino
        spaceBoxes = [
            pygame.Rect(506, 202, BOXES_WIDTH, BOXES_HEIGHT),
            pygame.Rect(562, 262, BOXES_WIDTH, BOXES_HEIGHT),
            pygame.Rect(506, 319, BOXES_WIDTH, BOXES_HEIGHT),
            pygame.Rect(671, 378, BOXES_WIDTH, BOXES_HEIGHT),
            pygame.Rect(563, 440, BOXES_WIDTH, BOXES_HEIGHT),
            pygame.Rect(506, 499, BOXES_WIDTH, BOXES_HEIGHT),
        ]

        # Criar caixas arrastáveis (nova ordem)
        draggableBoxes = [
            pygame.Rect(DRAGGABLE_POSITIONX, 200, BOXES_WIDTH, BOXES_HEIGHT),
            pygame.Rect(DRAGGABLE_POSITIONX, 260, BOXES_WIDTH, BOXES_HEIGHT),
            pygame.Rect(DRAGGABLE_POSITIONX, 320, BOXES_WIDTH, BOXES_HEIGHT),
            pygame.Rect(DRAGGABLE_POSITIONX, 380, BOXES_WIDTH, BOXES_HEIGHT),
            pygame.Rect(DRAGGABLE_POSITIONX, 440, BOXES_WIDTH, BOXES_HEIGHT),
            pygame.Rect(DRAGGABLE_POSITIONX, 500, BOXES_WIDTH, BOXES_HEIGHT),
        ]

        # Matching correto das boxes
        correct_mapping = {
            4: 0,
            0: 1,
            5: 2,
            2: 3,
            3: 4,
            1: 5,
        }

        initial_positions = {i: box.topleft for i, box in enumerate(draggableBoxes)}
        active_draggableBox = None
        all_correct = False

        while running:

            # Desenhar fundo
            screen.blit(bg_image, bg_rect)  

            screen.blit(submeterBox_image, submeterBox_rect.topleft)

            # Desenhar as caixas arrastáveis
            for i, draggableBox in enumerate(draggableBoxes):
                screen.blit(draggable_images[i], draggableBox.topleft)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Clicar para arrastar
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i, draggableBox in enumerate(draggableBoxes):
                        if draggableBox.collidepoint(event.pos):
                            active_draggableBox = i

                # Mover a caixa ativa
                if event.type == pygame.MOUSEMOTION and active_draggableBox is not None:
                    draggableBoxes[active_draggableBox].move_ip(event.rel)

                

                # Soltar a caixa
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if active_draggableBox is not None:
                        correct_space_index = correct_mapping[active_draggableBox]  # Descobrir qual espaço é correto
                        correct_space = spaceBoxes[correct_space_index]

                        # Se soltar no espaço correto, fixa lá
                        if draggableBoxes[active_draggableBox].colliderect(correct_space):
                            draggableBoxes[active_draggableBox].topleft = correct_space.topleft
                        else:
                            draggableBoxes[active_draggableBox].topleft = initial_positions[active_draggableBox]
                        
                        active_draggableBox = None

                    # Verificar se todas as caixas estão no local correto
                    all_correct = all(
                        draggableBoxes[box].topleft == spaceBoxes[correct_mapping[box]].topleft
                        for box in correct_mapping
                    )
                
                # Clicar no Submeter
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if all_correct:
                        end_time = pygame.time.get_ticks()
                        elapsed_time = (end_time - start_time) / 1000
                        self.player1.score += max(10, int(200 - elapsed_time))
                        running = False
                        # return "go to multiusos - lab"
                        return "fim do dia"

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()