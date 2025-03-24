import pygame
import time
class Frame:
    def __init__(self, path, speechBubble):
        self.path = path
        self.speechBubble = speechBubble
        
    def get_image(self):
        image = pygame.image.load(self.path).convert_alpha()
        image = pygame.transform.scale(image, (1280,720))
        return image
    
    def get_time(self):
        if self.speechBubble:
            return 5
        else:
            return 0.3
        
        
        
        
class Cutscene:
    def __init__(self, screen, sceneNumber):
        self.screen = screen
        self.sceneNumber = sceneNumber
        self.current_frame = 0
        self.images = []
        
    def get_images(self):
        filme1_1 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_1.png", False)
        
        filme1_2 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_2.png", False)
        
        filme1_3 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_3.png", False)
        
        filme1_4 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_4.png", False)

        filme1_5 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_5.png", False)

        filme1_6 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_6.png", False)

        filme1_7 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_7.png", True)

        filme1_8 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_8.png", True)

        filme1_9 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_9.png", True)

        filme1_10 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_10.png", False)

        filme1_11 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_11.png", False)

        filme1_12 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_12.png", False)

        filme1_13 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_13.png", False)

        filme1_14 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_14.png", False)

        filme1_15 = Frame("iscte-sintra-simulator/assets/images/filmes/filme1/filme1_15.png", False)
        
        # Filme 2
        filme2_1 = Frame("iscte-sintra-simulator/assets/images/filmes/filme2/filme2_1.png", False)
        
        filme2_2 = Frame("iscte-sintra-simulator/assets/images/filmes/filme2/filme2_2.png", False)
        
        filme2_3 = Frame("iscte-sintra-simulator/assets/images/filmes/filme2/filme2_3.png", False)
        
        filme2_4 = Frame("iscte-sintra-simulator/assets/images/filmes/filme2/filme2_4.png", False)
        
        filme2_5 = Frame("iscte-sintra-simulator/assets/images/filmes/filme2/filme2_5.png", False)
        
        filme2_6 = Frame("iscte-sintra-simulator/assets/images/filmes/filme2/filme2_6.png", True)
        
        filme2_7 = Frame("iscte-sintra-simulator/assets/images/filmes/filme2/filme2_7.png", True)

        #Filme 3
        filme3_1 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_1.png", False)

        filme3_2 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_2.png", False)

        filme3_3 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_3.png", False)

        filme3_4 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_4.png", False)

        filme3_5 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_5.png", False)

        filme3_6 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_6.png", False)

        filme3_7 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_7.png", True)

        filme3_8 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_8.png", False)

        filme3_9 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_9.png", False)

        filme3_10 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_10.png", False)

        filme3_11 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_11.png", False)

        filme3_12 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_12.png", False)

        filme3_13 = Frame("iscte-sintra-simulator/assets/images/filmes/filme3/filme3_13.png", False)

        #Filme 4
        filme4_1 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_1.png", False)

        filme4_2 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_2.png", False)

        filme4_3 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_3.png", False)

        filme4_4 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_4.png", True)

        filme4_5 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_5.png", True)

        filme4_6 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_6.png", False)

        filme4_7 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_7.png", True)

        filme4_8 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_8.png", True)

        filme4_9 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_9.png", False)

        filme4_10 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_10.png", True)

        filme4_11 = Frame("iscte-sintra-simulator/assets/images/filmes/filme4/filme4_11.png", False)
        
        #Filme 5
        filme5_1 = Frame("iscte-sintra-simulator/assets/images/filmes/filme5/filme5_1.png", False)

        filme5_2 = Frame("iscte-sintra-simulator/assets/images/filmes/filme5/filme5_2.png", False)

        filme5_3 = Frame("iscte-sintra-simulator/assets/images/filmes/filme5/filme5_3.png", True)

        filme5_4 = Frame("iscte-sintra-simulator/assets/images/filmes/filme5/filme5_4.png", True)

        filme5_5 = Frame("iscte-sintra-simulator/assets/images/filmes/filme5/filme5_5.png", False)
        
        filme5_6 = Frame("iscte-sintra-simulator/assets/images/filmes/filme5/filme5_6.png", False)

        filme5_7 = Frame("iscte-sintra-simulator/assets/images/filmes/filme5/filme5_7.png", False)

        filme5_8 = Frame("iscte-sintra-simulator/assets/images/filmes/filme5/filme5_8.png", False)

        filme5_9 = Frame("iscte-sintra-simulator/assets/images/filmes/filme5/filme5_9.png", False)
        
        if self.sceneNumber == 1:
            self.images = [
                filme1_1,
                filme1_2,
                filme1_3,
                filme1_4,
                filme1_5,
                filme1_6,
                filme1_7,
                filme1_8,
                filme1_9,
                filme1_10,
                filme1_11,
                filme1_12,
                filme1_13,
                filme1_14,
                filme1_15
            ]
        elif self.sceneNumber == 2:
            self.images = [
                filme2_1,
                filme2_2,
                filme2_3,
                filme2_4,
                filme2_5,
                filme2_6,
                filme2_7
            ]

        elif self.sceneNumber == 3:
            self.images = [
                filme3_1,
                filme3_2,
                filme3_3,
                filme3_4,
                filme3_5,
                filme3_6,
                filme3_7,
                filme3_8,
                filme3_9,
                filme3_10,
                filme3_11,
                filme3_12,
                filme3_13
            ]

        elif self.sceneNumber == 4:
            self.images = [
                filme4_1,
                filme4_2,
                filme4_3,
                filme4_4,
                filme4_5,
                filme4_6,
                filme4_7,
                filme4_8,
                filme4_9,
                filme4_10,
                filme4_11
            ]
            
        elif self.sceneNumber == 5:
            self.images = [
                filme5_1,
                filme5_2,
                filme5_3,
                filme5_4,
                filme5_5,
                filme5_6,
                filme5_7,
                filme5_8
            ]

        return self.images
    
    def load(self):
        running = True
                
        self.get_images()
        
        self.screen.fill((0, 0, 0))
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.sceneNumber == 1:
                        return "go to entrada"    
                    elif self.sceneNumber == 2:
                        return "fim do dia"
                    elif self.sceneNumber == 3:
                        return "go to entrada"
                    elif self.sceneNumber == 4:
                        return "go to uata"
                    elif self.sceneNumber == 5:
                        return "fim do dia"
            
            if self.current_frame < len(self.images):
                frame = self.images[self.current_frame]
                
                self.screen.blit(frame.get_image(), (0,0))
                pygame.display.flip()
                
                pygame.time.wait(int(frame.get_time() * 1000))  # Convert seconds to milliseconds

                self.current_frame += 1 
                
            else:
            
                if self.sceneNumber == 1:
                    return "go to entrada - day begin"
                
                elif self.sceneNumber == 2:
                    return "fim do dia"
                
                elif self.sceneNumber == 3:
                    return "go to entrada - day begin"
                
                elif self.sceneNumber == 4:
                    return "go to uata"
                
                elif self.sceneNumber == 5:
                    return "fim do dia"