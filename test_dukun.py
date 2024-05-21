import unittest
import pygame
from dukun import Dukun1, Dukun2, Dukun3

class TestDukun(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.gambar1 = pygame.Surface((100, 100))  # Gambar untuk Dukun1
        self.gambar2 = pygame.Surface((100, 100))  # Gambar untuk Dukun2
        self.gambar3 = pygame.Surface((100, 100))  # Gambar untuk Dukun3
        self.x = 100  # Koordinat X awal
        self.y = 100  # Koordinat Y awal
        self.lebar = 100  # Lebar gambar Dukun
        self.tinggi = 100  # Tinggi gambar Dukun
        self.dukun1 = Dukun1(self.gambar1, self.lebar, self.tinggi, self.x, self.y)
        self.dukun2 = Dukun2(self.gambar2, self.lebar, self.tinggi, self.x, self.y)
        self.dukun3 = Dukun3(self.gambar3, self.lebar, self.tinggi, self.x, self.y)

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        self.assertEqual(self.dukun1.pos_x, self.x)
        self.assertEqual(self.dukun1.pos_y, self.y)
        self.assertEqual(self.dukun1.width, self.lebar)
        self.assertEqual(self.dukun1.height, self.tinggi)
        self.assertEqual(self.dukun2.pos_x, self.x)
        self.assertEqual(self.dukun2.pos_y, self.y)
        self.assertEqual(self.dukun2.width, self.lebar)
        self.assertEqual(self.dukun2.height, self.tinggi)
        self.assertEqual(self.dukun3.pos_x, self.x)
        self.assertEqual(self.dukun3.pos_y, self.y)
        self.assertEqual(self.dukun3.width, self.lebar)
        self.assertEqual(self.dukun3.height, self.tinggi)

    def test_display(self):
        self.assertIsNone(self.dukun1.display(self.screen))
        self.assertIsNone(self.dukun2.display(self.screen))
        self.assertIsNone(self.dukun3.display(self.screen))

    def test_shoot(self):
        self.dukun1.fired = False
        self.dukun2.fired = False
        self.dukun3.fired = False
        self.assertIsNone(self.dukun1.shoot(self.screen))
        self.assertIsNone(self.dukun2.shoot(self.screen))
        self.assertIsNone(self.dukun3.shoot(self.screen))

if __name__ == '__main__':
    unittest.main()
