import pygame
import math

pygame.init()

# Serangan load gambar
img_serangan = pygame.image.load('<<<LOKASI GAMBAR>>>').convert_alpha()
b_w = img_serangan.get_width()
b_h = img_serangan.get_height()
img_serangan = pygame.transform.scale(img_serangan, (int(b_w * 0.07), int(b_h * 0.07)))

class Serangan(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = math.radians(angle)
        self.speed = 12
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)
    
    def update(self):
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
        
        self.rect.x += self.dx
        self.rect.y += self.dy

# Grouping Serangan
group_serangan = pygame.sprite.Group()

# Mekanisme Serangan di Loop main
group_serangan.update()
group_serangan.draw('<<<SCREEN>>>')
print(len(group_serangan))