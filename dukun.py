import pygame
import math
from abc import ABC, abstractmethod
from serangan import Serangan, group_serangan

# Inisialisasi pygame
pygame.init()

# Abstrak class dukun
class Dukun(ABC):
    def __init__(self, gambar, lebar, tinggi, x, y):
        self.gambar_dasar = gambar
        self.width = lebar
        self.height = tinggi
        self.pos_x = x
        self.pos_y = y
        self.fired = False

        self.image = pygame.transform.scale(self.gambar_dasar, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    @abstractmethod
    def display(self, screen):
        pass

    @abstractmethod
    def shoot(self):
        pass


class Dukun1(Dukun):
    def __init__(self, gambar, lebar, tinggi, x, y):
        base_sihir = pygame.image.load("assets/dukun/sihir_1.png").convert_alpha()
        self.dukun1_shoot = pygame.image.load("assets/dukun/dukun_1_attack.png").convert_alpha()
        s_w = base_sihir.get_width()
        s_h = base_sihir.get_height()
        self.gambar_sihir = pygame.transform.scale(base_sihir, (int(s_w* 0.080), int(s_h* 0.080)))
        super().__init__(gambar, lebar, tinggi, x, y)
    
    def display(self, screen):
        gambar_rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        screen.blit(self.image, gambar_rect)
    
    def shoot(self, screen):
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect[0]
        y_dist = -(pos[1] - self.rect[1])
        self.angle = math.degrees(math.atan2(y_dist, x_dist))
        # get mouse click
        if pygame.mouse.get_pressed()[0] and self.fired == False and pos[0] < 720 and pos[1] > 70:
            self.fired = True
            self.image = pygame.transform.scale(self.dukun1_shoot, (self.width, self.height))
            self.display(screen)
            sihir = Serangan(self.gambar_sihir, 685, 380, self.angle)
            group_serangan.add(sihir)
        # reset mouse click
        if pygame.mouse.get_pressed()[0] == False:
            self.image = pygame.transform.scale(self.gambar_dasar, (self.width, self.height))
            self.display(screen)
            self.fired = False


class Dukun2(Dukun):
    def __init__(self, gambar, lebar, tinggi, x, y):
        base_sihir = pygame.image.load("assets/dukun/sihir_2.png").convert_alpha()
        self.dukun1_shoot = pygame.image.load("assets/dukun/dukun_2_attack.png").convert_alpha()
        s_w = base_sihir.get_width()
        s_h = base_sihir.get_height()
        self.gambar_sihir = pygame.transform.scale(base_sihir, (int(s_w* 0.080), int(s_h* 0.080)))
        super().__init__(gambar, lebar, tinggi, x, y)
    
    def display(self, screen):
        gambar_rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        screen.blit(self.image, gambar_rect)
    
    def shoot(self, screen):
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect[0]
        y_dist = -(pos[1] - self.rect[1])
        self.angle = math.degrees(math.atan2(y_dist, x_dist))
        # get mouse click
        if pygame.mouse.get_pressed()[0] and self.fired == False and pos[0] < 720 and pos[1] > 70:
            self.fired = True
            self.image = pygame.transform.scale(self.dukun1_shoot, (self.width, self.height))
            self.display(screen)
            sihir = Serangan(self.gambar_sihir, 685, 380, self.angle)
            group_serangan.add(sihir)
        # reset mouse click
        if pygame.mouse.get_pressed()[0] == False:
            self.image = pygame.transform.scale(self.gambar_dasar, (self.width, self.height))
            self.display(screen)
            self.fired = False

class Dukun3(Dukun):
    def __init__(self, gambar, lebar, tinggi, x, y):
        base_sihir = pygame.image.load("assets/dukun/sihir_3.png").convert_alpha()
        self.dukun1_shoot = pygame.image.load("assets/dukun/dukun_3_attack.png").convert_alpha()
        s_w = base_sihir.get_width()
        s_h = base_sihir.get_height()
        self.gambar_sihir = pygame.transform.scale(base_sihir, (int(s_w* 0.080), int(s_h* 0.080)))
        super().__init__(gambar, lebar, tinggi, x, y)
    
    def display(self, screen):
        gambar_rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        screen.blit(self.image, gambar_rect)
    
    def shoot(self, screen):
        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - self.rect[0]
        y_dist = -(pos[1] - self.rect[1])
        self.angle = math.degrees(math.atan2(y_dist, x_dist))
        # get mouse click
        if pygame.mouse.get_pressed()[0] and self.fired == False and pos[0] < 720 and pos[1] > 70:
            self.fired = True
            self.image = pygame.transform.scale(self.dukun1_shoot, (self.width, self.height))
            self.display(screen)
            sihir = Serangan(self.gambar_sihir, 685, 380, self.angle)
            group_serangan.add(sihir)
        # reset mouse click
        if pygame.mouse.get_pressed()[0] == False:
            self.image = pygame.transform.scale(self.gambar_dasar, (self.width, self.height))
            self.display(screen)
            self.fired = False