import pygame
import sys
from dukun import Dukun1, Dukun2, Dukun3

# Inisialisasi pygame
pygame.init()

# Class Button
class Input:
    def __init__(self, image, pos, text_input, font_path, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font_path
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
    def __init__(self, width, height, bg_img, btn_img, font_path):
        self.width = width
        self.height = height
        self.bg_img = bg_img
        self.btn_img = btn_img
        self.font = font_path
        self.input = 0

        self.SCREEN = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Menu")
    
    def get_font(self, font_path, size):
        return pygame.font.Font(font_path, size)
    
    def get_pilihan(self, number):
        self.input = number
        return self.input
    
    def update_btn(self, section_pos, button_list):
        for button in button_list:
            button.changeColor(section_pos)
            button.update(self.SCREEN)

    def create_rect(self, objek, posisi_x, posisi_y):
        objek_rect = objek.get_rect(center=(posisi_x, posisi_y))
        self.SCREEN.blit(objek, objek_rect)

    def create_text(self, teks, color, font_path, size):
        font_teks = self.get_font(font_path, size).render(teks, True, color)
        return font_teks

    def play(self):
        base_btn = pygame.image.load("assets/menu/button_1.png")
        new_btn = pygame.transform.scale(base_btn, (190,40))
        font_btn = self.get_font(self.font, 20)
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            self.SCREEN.fill("#050A30")

            PLAY_TEXT = self.create_text("PILIH DUKUN KAMU", "White", self.font, 44)
            self.create_rect(PLAY_TEXT, 450, 120)

            NAMA_1 = self.create_text("Gus", "White", self.font, 20)
            NAMA_2 = self.create_text("Nyai", "White", self.font, 20)
            NAMA_3 = self.create_text("Joko", "White", self.font, 20)

            self.create_rect(NAMA_1, 180, 200)
            self.create_rect(NAMA_2, 450, 200)
            self.create_rect(NAMA_3, 720, 200)
            
            dukun1_img = pygame.image.load("assets/dukun/dukun_1.png").convert_alpha()
            dukun_1 = Dukun1(dukun1_img, 800, 800, 180, 340)
            dukun_1.display(self.SCREEN)

            dukun2_img = pygame.image.load("assets/dukun/dukun_2.png").convert_alpha()
            dukun_2 = Dukun2(dukun2_img, 1000, 1000, 450, 320)
            dukun_2.display(self.SCREEN)

            dukun3_img = pygame.image.load("assets/dukun/dukun_3.png").convert_alpha()
            dukun_3 = Dukun3(dukun3_img, 1000, 1000, 720, 330)
            dukun_3.display(self.SCREEN)
            
            SELECT_1 = Input(image=new_btn, pos=(180,500), text_input="PILIH",
                              font_path=font_btn, base_color="White", hovering_color="Green")
            
            SELECT_2 = Input(image=new_btn, pos=(450,500), text_input="PILIH",
                              font_path=font_btn, base_color="White", hovering_color="Green")
            
            SELECT_3 = Input(image=new_btn, pos=(720,500), text_input="PILIH",
                              font_path=font_btn, base_color="White", hovering_color="Green")
            
            self.update_btn(PLAY_MOUSE_POS, [SELECT_1, SELECT_2, SELECT_3])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SELECT_1.checkForInput(PLAY_MOUSE_POS):
                        return 1
                    elif SELECT_2.checkForInput(PLAY_MOUSE_POS):
                        return 2
                    elif SELECT_3.checkForInput(PLAY_MOUSE_POS):
                        return 3

            pygame.display.update()
    
    def tampil_menu(self):
        font_btn = self.get_font(self.font, 28)
        sound_menu = pygame.mixer.Sound("assets/sound/menu.mp3")
        while True:
            self.SCREEN.blit(self.bg_img, (0, 0))
            sound_menu.play()

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            JUDUL_UPPER = self.create_text("DVD", "Black", "assets/menu/lava_pro.ttf", 100)
            JUDUL_LOWER = self.create_text("DUKUN VS DEMIT", "Black", "assets/menu/shlop.ttf", 80)
            self.create_rect(JUDUL_UPPER, 450, 98)
            self.create_rect(JUDUL_LOWER, 450, 190)

            PLAY_BUTTON = Input(image=self.btn_img, pos=(445, 380), text_input="PLAY",
                                 font_path=font_btn, base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Input(image=self.btn_img, pos=(445, 470), text_input="QUIT",
                                 font_path=font_btn, base_color="#d7fcd4", hovering_color="White")

            self.update_btn(MENU_MOUSE_POS, [PLAY_BUTTON, QUIT_BUTTON])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pilihan = self.play()
                        sound_menu.stop()
                        return pilihan
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()