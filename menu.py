import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Class Button
class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)

        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


# Class Menu
class Menu:
    def __init__(self, width, height, bg_img, font_path):
        self.width = width
        self.height = height
        self.bg_img = bg_img
        self.font_path = font_path

        self.SCREEN = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Menu")
    
    def get_font(self, font_path, size):
        return pygame.font.Font(font_path, size)

    def play(self):
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("black")

            PLAY_TEXT = self.get_font(self.font_path, 28).render("This is the PLAY screen.", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(450,260))
            self.SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(450, 460), text_input="Back", 
                               font=self.get_font(self.font_path, 45), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.main_menu()
            
            pygame.display.update()
    
    def main_menu(self):
        img_btn = pygame.image.load("assets/menu/button.png")
        font_jdl_up = self.get_font("assets/menu/lava_pro.ttf", 100)
        font_jdl_lw = self.get_font("assets/menu/shlop.ttf", 80)
        font_btn = self.get_font(self.font_path, 28)
        base_clr = "#d7fcd4"
        hover_clr = "White"

        while True:
            self.SCREEN.blit(self.bg_img, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            JUDUL_UPPER = font_jdl_up.render("DVD", True, "black")
            JUDUL_LOWER = font_jdl_lw.render("DUKUN VS DEMIT", True, "black" )
            UPPER_RECT = JUDUL_UPPER.get_rect(center=(450, 98))
            LOWER_RECT = JUDUL_LOWER.get_rect(center=(450, 190))

            PLAY_BUTTON = Button(image=img_btn, pos=(445, 380), text_input="PLAY",
                                 font=font_btn, base_color=base_clr, hovering_color=hover_clr)
            QUIT_BUTTON = Button(image=img_btn, pos=(445, 470), text_input="QUIT",
                                 font=font_btn, base_color=base_clr, hovering_color=hover_clr)
            
            self.SCREEN.blit(JUDUL_UPPER, UPPER_RECT)
            self.SCREEN.blit(JUDUL_LOWER, LOWER_RECT)

            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
        
            pygame.display.update()