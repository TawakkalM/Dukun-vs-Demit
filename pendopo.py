import pygame

pygame.init()

class Pendopo():
    def __init__(self, image100, image50, image25, bg, x, y, scale):
        self.__kesehatan = 1000
        self.__maks_kesehatan = self.get_kesehatan()
        self.ditembak = False
        self.__uang = 0
        self.__skor = 0

        width = image100.get_width()
        height = image100.get_height()

        self.gambar100 = pygame.transform.scale(image100, (int(width * scale), int(height * scale)))
        self.gambar50 = pygame.transform.scale(image50, (int(width * scale), int(height * scale)))
        self.gambar25 = pygame.transform.scale(image25, (int(width * scale), int(height * scale)))
        self.bg = bg
        self.rect = self.gambar100.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.screen = pygame.display.set_mode((900, 650))
        pygame.display.set_caption("DVD")
    
    # Method getter untuk mendapatkan info kesehatan pendopo
    def get_kesehatan(self):
        return self.__kesehatan
    # Method getter untuk mendapatkan info maks kesehatan pendopo
    def get_maks_kesehatan(self):
        return self.__maks_kesehatan
    # Method getter untuk mendapatkan info uang
    def get_uang(self):
        return self.__uang
    # Method getter untuk mendapatkan info skor
    def get_skor(self):
        return self.__skor
    
    # Method setter untuk mengset nilai kesehatan
    def set_kesehatan(self, value):
        self.__kesehatan = value
    # Method setter untuk menambah nilai kesehatan
    def set_tambah_kesehatan(self, value):
        self.__kesehatan += value
    # Method setter untuk mengurang nilai kesehatan
    def set_kurang_kesehatan(self, value):
        self.__kesehatan -= value

    # Method setter untuk mengset nilai maks kesehatan
    def set_maks_kesehatan(self, value):
        self.__maks_kesehatan = value
    # Method setter untuk menambah maks kesehatan
    def set_tambah_maks_kesehatan(self, value):
        self.__maks_kesehatan += value

    # Method setter untuk mengset uang
    def set_uang(self, value):
        self.__uang = value
    # Method setter untuk menambah uang
    def set_tambah_uang(self, value):
        self.__uang += value
    # Method setter untuk mengurang uang
    def set_kurang_uang(self, value):
        self.__uang -= value

    # Method setter untuk mengset skor
    def set_skor(self, value):
        self.__skor = value
    # Method setter untuk menambah skor
    def set_tambah_skor(self, value):
        self.__skor += value

    def render(self):
        # Render latar belakang
        self.screen.blit(self.bg, (0, 0))
        
        # periksa gambar yang sesuai dengan kesehatan saat ini
        if self.get_kesehatan() <= 250:
        if self.kesehatan <= 250:
            self.gambar = self.gambar25
        elif self.get_kesehatan() <= 500:
            self.gambar = self.gambar50
        else:
            self.gambar = self.gambar100

        self.screen.blit(self.gambar, self.rect)

    def perbaiki(self):
        if self.get_uang() >= 1000 and self.get_kesehatan() < self.get_maks_kesehatan():
            self.set_tambah_kesehatan(500)
            self.set_kurang_uang(1000)
            if self.get_kesehatan() > self.get_maks_kesehatan():
                self.set_kesehatan(self.get_maks_kesehatan())

    def pertahanan(self):
        if self.get_uang() >= 500:
            self.set_tambah_maks_kesehatan(250)
            self.set_kurang_uang(500)
