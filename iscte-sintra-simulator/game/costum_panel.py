import pygame
import os
from characters.players.player import Player

class CostumPanel:
    def __init__(self, screen, player1):
        self.screen = screen
        self.player1 = player1
        self.input_text= ""
        self.text_box_active = False
        self.curso_index = 0
        self.curso = None
        self.curso_name = None
        self.personagem_index = 0
        self.personagem = None
        
    
    def load(self):
        print("COSTUM PANEL OPEN")
        pygame.init()
        pygame.font.init() 
        myfont = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogica.ttf", 20)
        bold_font = pygame.font.Font("iscte-sintra-simulator/assets/fonts/dogicabold.ttf", 16)


        WIDTH = 1280
        HEIGHT = 720
        BOXES_WIDTH = 624*0.7
        BOXES_HEIGHT = 192*0.7

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        running = True

        # Placeholder text
        placeholder_text = "Clica para escrever"
        placeholder_surface = myfont.render(placeholder_text, True, (150, 150, 150))


        # Carregar o fundo
        bg_image = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/newpanel.png").convert_alpha()
        bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
        bg_rect = bg_image.get_rect()
        bg_rect.topleft = (0, 0)

        # Imagem da personagem
        player_image = pygame.image.load("iscte-sintra-simulator/assets/images/Default1/Default1_front.png").convert_alpha()
        player_image = pygame.transform.scale(player_image, (int(player_image.get_width() * 5.5), int(player_image.get_height() * 5.5)))
        player_rect = player_image.get_rect()
        player_rect.topleft = (250, 300)

        # Caixa de texto do nome
        txt_image = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/box.png").convert_alpha()
        txt_image = pygame.transform.scale(txt_image, (BOXES_WIDTH, BOXES_HEIGHT))
        txt_rect = txt_image.get_rect()
        txt_rect.bottomleft = (612, 420)

        #Caixa de escolha de cursos
        curso_folder = "iscte-sintra-simulator/assets/images/costum_panel_assets/cursos"
        curso_files = [img for img in os.listdir(curso_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
        curso_images = [(pygame.image.load(os.path.join(curso_folder, img)).convert_alpha(), img) for img in curso_files]
        curso_images = [(pygame.transform.scale(img, (BOXES_WIDTH, BOXES_HEIGHT)), name) for img, name in curso_images]
        curso_rect = curso_images[0][0].get_rect()
        curso_rect.bottomleft = (612, 510)


        #Seta para a esquerda
        seta_esq_image_normal = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/seta-esquerda.png").convert_alpha()
        seta_esq_image_normal = pygame.transform.scale(seta_esq_image_normal, (int(seta_esq_image_normal.get_width() * .7), int(seta_esq_image_normal.get_height() * .7)))
        seta_esq_image_hover = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/setaesquerda_hover.png").convert_alpha()
        seta_esq_image_hover = pygame.transform.scale(seta_esq_image_hover, (int(seta_esq_image_hover.get_width() * .7), int(seta_esq_image_hover.get_height() * .7)))
        seta_esq_image = seta_esq_image_normal
        seta_esq_rec = seta_esq_image.get_rect()
        seta_esq_rec.topleft = (curso_rect.left-25, curso_rect.top + 18)

        # Seta para a direita
        seta_dir_image_normal = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/seta-direita.png").convert_alpha()
        seta_dir_image_normal = pygame.transform.scale(seta_dir_image_normal, (int(seta_dir_image_normal.get_width() * 0.7), int(seta_dir_image_normal.get_height() * 0.7)))
        seta_dir_image_hover = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/setadireita_hover.png").convert_alpha()
        seta_dir_image_hover = pygame.transform.scale(seta_dir_image_hover, (int(seta_dir_image_hover.get_width() * 0.7), int(seta_dir_image_hover.get_height() * 0.7)))
        seta_dir_image = seta_dir_image_normal
        seta_dir_rec = seta_dir_image.get_rect()
        seta_dir_rec.topleft = (curso_rect.left+350, curso_rect.top + 18)


        # Seta personagem para a esquerda
        seta_personagem_esq_image_normal = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/seta-esquerda.png").convert_alpha()
        seta_personagem_esq_image_normal = pygame.transform.scale(seta_personagem_esq_image_normal, (int(seta_personagem_esq_image_normal.get_width() * 0.7), int(seta_personagem_esq_image_normal.get_height() * 0.7)))
        seta_personagem_esq_image_hover = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/setaesquerda_hover.png").convert_alpha()
        seta_personagem_esq_image_hover = pygame.transform.scale(seta_personagem_esq_image_hover, (int(seta_personagem_esq_image_hover.get_width() * 0.7), int(seta_personagem_esq_image_hover.get_height() * 0.7)))
        seta_personagem_esq_image = seta_personagem_esq_image_normal
        seta_personagem_esq_rec = seta_personagem_esq_image.get_rect()
        seta_personagem_esq_rec.topleft = (curso_rect.left - 440, curso_rect.top + 35)

        # Seta personagem para a direita
        seta_personagem_dir_image_normal = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/seta-direita.png").convert_alpha()
        seta_personagem_dir_image_normal = pygame.transform.scale(seta_personagem_dir_image_normal, (int(seta_personagem_dir_image_normal.get_width() * 0.7), int(seta_personagem_dir_image_normal.get_height() * 0.7)))
        seta_personagem_dir_image_hover = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/setadireita_hover.png").convert_alpha()
        seta_personagem_dir_image_hover = pygame.transform.scale(seta_personagem_dir_image_hover, (int(seta_personagem_dir_image_hover.get_width() * 0.7), int(seta_personagem_dir_image_hover.get_height() * 0.7)))
        seta_personagem_dir_image = seta_personagem_dir_image_normal
        seta_personagem_dir_rec = seta_personagem_dir_image.get_rect()
        seta_personagem_dir_rec.topleft = (curso_rect.left -255, curso_rect.top + 35)

        # Texto da designacao da personagem
        personagem_options = ['Aluna', 'Aluno', 'Alune']
        personagem_text = bold_font.render(personagem_options[self.personagem_index], True, (0, 0, 0))
        personagem_rect = personagem_text.get_rect()
        personagem_rect.topleft = (curso_rect.left-330, curso_rect.top - 18) 


        #Botao de avancar
        bt_image_normal = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/avancar.png").convert_alpha()
        bt_image_normal = pygame.transform.scale(bt_image_normal, (int(bt_image_normal.get_width() * .75), int(bt_image_normal.get_height() * .75)))
        bt_image_hover = pygame.image.load("iscte-sintra-simulator/assets/images/costum_panel_assets/avancar_hover.png").convert_alpha()
        bt_image_hover = pygame.transform.scale(bt_image_hover, (int(bt_image_hover.get_width() * .75), int(bt_image_hover.get_height() * .75)))
        bt_image = bt_image_normal
        bt_rec = bt_image.get_rect()
        bt_rec.bottomleft = (560, 550)

    

        while running:
            screen.blit(bg_image, bg_rect)
            screen.blit(player_image, player_rect)
            screen.blit(txt_image, txt_rect)
            screen.blit(curso_images[self.curso_index][0], curso_rect)
            personagem_text = bold_font.render(personagem_options[self.personagem_index], True, (0, 0, 0))
            personagem_rect = personagem_text.get_rect()
            personagem_rect.topleft = (curso_rect.left-333, curso_rect.top + 68)
            screen.blit(personagem_text, personagem_rect)

            # Check if the mouse is hovering over the buttons
            mouse_pos = pygame.mouse.get_pos()
            if bt_rec.collidepoint(mouse_pos):
                bt_image = bt_image_hover
            else:
                bt_image = bt_image_normal

            if seta_esq_rec.collidepoint(mouse_pos):
                seta_esq_image = seta_esq_image_hover
            else:
                seta_esq_image = seta_esq_image_normal

            if seta_dir_rec.collidepoint(mouse_pos):
                seta_dir_image = seta_dir_image_hover
            else:
                seta_dir_image = seta_dir_image_normal

            if seta_personagem_esq_rec.collidepoint(mouse_pos):
                seta_personagem_esq_image = seta_personagem_esq_image_hover
            else:
                seta_personagem_esq_image = seta_personagem_esq_image_normal

            if seta_personagem_dir_rec.collidepoint(mouse_pos):
                seta_personagem_dir_image = seta_personagem_dir_image_hover
            else:
                seta_personagem_dir_image = seta_personagem_dir_image_normal

            screen.blit(bt_image, bt_rec)
            screen.blit(seta_esq_image, seta_esq_rec)
            screen.blit(seta_dir_image, seta_dir_rec)
            screen.blit(seta_personagem_esq_image, seta_personagem_esq_rec)
            screen.blit(seta_personagem_dir_image, seta_personagem_dir_rec)

            # Render the input text or placeholder text
            if self.input_text == "" and not self.text_box_active:
                screen.blit(placeholder_surface, (txt_rect.x + 25, txt_rect.y + 18))
            else:
                text_surface = myfont.render(self.input_text, True, (0, 0, 0))
                screen.blit(text_surface, (txt_rect.x + 25, txt_rect.y + 18))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if txt_rect.collidepoint(event.pos):
                        self.text_box_active = True
                    else:
                        self.text_box_active = False
                    if seta_esq_rec.collidepoint(event.pos):
                        self.curso_index = (self.curso_index - 1) % len(curso_images)
                    if seta_dir_rec.collidepoint(event.pos):
                        self.curso_index = (self.curso_index + 1) % len(curso_images)
                    if seta_personagem_esq_rec.collidepoint(event.pos):
                        self.personagem_index = (self.personagem_index - 1) % len(personagem_options)
                    if seta_personagem_dir_rec.collidepoint(event.pos):
                        self.personagem_index = (self.personagem_index + 1) % len(personagem_options)
                    if bt_rec.collidepoint(event.pos):
                        self.curso = curso_images[self.curso_index][0]
                        self.curso_name = os.path.splitext(curso_images[self.curso_index][1])[0]  # Remove the extension
                        self.personagem = personagem_options[self.personagem_index]
                        running = False
                if event.type == pygame.KEYDOWN and self.text_box_active:
                    if event.key == pygame.K_RETURN:  # Ou qualquer outra tecla que desejas
                        running = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        new_text = self.input_text + event.unicode
                        new_text_surface = myfont.render(new_text, True, (0, 0, 0))
                        if new_text_surface.get_width() < (BOXES_WIDTH - 20):  # Allow some padding
                            self.input_text = new_text



            pygame.display.flip()
            clock.tick(60)
        
        print("COSTUM PANEL CLOSE")

        # Atributos a serem passados para a proxima tela
        print(self.input_text)
        print(self.personagem)
        print(self.curso_name)
        pygame.quit()


screen = pygame.display.set_mode((1280, 720))
player1 = Player(850, 250, "iscte-sintra-simulator/assets/images/gaudencio/gaudencio_back.png", (0,0,0), 1)
costum_panel = CostumPanel(screen, player1)
costum_panel.load()