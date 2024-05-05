import pygame

pygame.init()

class Pendopo():
    def __init__(self, image100, image50, image25, bg, x, y, scale):
        self.kesehatan = 1000
        self.maks_kesehatan = self.kesehatan
        self.ditembak = False
        self.uang = 0
        self.skor = 0

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

    def render(self):
        # Render latar belakang
        self.screen.blit(self.bg, (0, 0))
        
        if self.kesehatan <= 250:
            self.gambar = self.gambar25
        elif self.kesehatan <= 500:
            self.gambar = self.gambar50
        else:
            self.gambar = self.gambar100

        self.screen.blit(self.gambar, self.rect)

    def perbaiki(self):
        if self.uang >= 1000 and self.kesehatan < self.maks_kesehatan:
            self.kesehatan += 500
            self.uang -= 1000
            if self.kesehatan > self.maks_kesehatan:
                self.kesehatan = self.maks_kesehatan

    def pertahanan(self):
        if self.uang >= 500:
            self.maks_kesehatan += 250
            self.uang -= 500
