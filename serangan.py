import pygame
import math

# Inisialisasi pygame
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 650

class Serangan(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = math.radians(angle)
        self.speed = 10
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)

    def update(self):
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()

        self.rect.x += self.dx
        self.rect.y += self.dy


class Crosshair():
    def __init__(self, scale):
        image = pygame.image.load("assets/crosshair.png").convert_alpha()
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
    
    def draw(self, screen):
        mx, my = pygame.mouse.get_pos()
        self.rect.center = (mx, my)

        # menghilangkan mouse
        pygame.mouse.set_visible(False)
        
        screen.blit(self.image, self.rect)

# membuat grup serangan
group_serangan = pygame.sprite.Group()
