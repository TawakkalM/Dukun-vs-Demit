import unittest
import pygame
import math
from unittest.mock import patch

# Pastikan untuk mengimpor Serangan, SCREEN_WIDTH, dan SCREEN_HEIGHT dari file utama
from serangan import Serangan, SCREEN_WIDTH, SCREEN_HEIGHT

class TestSerangan(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.image = pygame.Surface((10, 10))  # Dummy image for testing
        self.image.fill((255, 0, 0))  # Fill with red color for visibility
        self.x = 100
        self.y = 100
        self.angle = 45
        self.serangan = Serangan(self.image, self.x, self.y, self.angle)

    def test_initialization(self):
        self.assertEqual(self.serangan.rect.x, self.x)
        self.assertEqual(self.serangan.rect.y, self.y)
        self.assertAlmostEqual(self.serangan.dx, math.cos(math.radians(self.angle)) * self.serangan.speed, places=5)
        self.assertAlmostEqual(self.serangan.dy, -(math.sin(math.radians(self.angle)) * self.serangan.speed), places=5)
        self.assertEqual(self.serangan.speed, 10)  # Ubah ini sesuai nilai yang diharapkan
        
    def test_update_outside_screen(self):
        self.serangan.rect.x = -10  # Move out of bounds
        self.serangan.update()
        self.assertFalse(self.serangan.alive())

        self.serangan.rect.x = SCREEN_WIDTH + 10  # Move out of bounds
        self.serangan.update()
        self.assertFalse(self.serangan.alive())

        self.serangan.rect.y = -10  # Move out of bounds
        self.serangan.update()
        self.assertFalse(self.serangan.alive())

        self.serangan.rect.y = SCREEN_HEIGHT + 10  # Move out of bounds
        self.serangan.update()
        self.assertFalse(self.serangan.alive())

if __name__ == '__main__':
    unittest.main()
