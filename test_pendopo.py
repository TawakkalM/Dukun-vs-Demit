import unittest
import pygame
from pendopo import Pendopo

class TestPendopo(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((800, 600)) 
        self.image100 =  pygame.image.load("assets/castle/Castle_100.png").convert_alpha()
        self.image50 = pygame.image.load('assets/castle/Castle_50.png').convert_alpha()
        self.image25 = pygame.image.load('assets/castle/Castle_25.png').convert_alpha()
        self.bg =  pygame.image.load('assets/castle/Latar_belakang.png').convert_alpha()

        self.pendopo = Pendopo(self.image100, self.image50, self.image25, self.bg, x=100, y=100, scale=1)

    def test_getters(self):
        self.assertEqual(self.pendopo.get_uang(), 0)
        self.assertEqual(self.pendopo.get_skor(), 0)
        self.assertEqual(self.pendopo.get_kesehatan(), 1000)
        self.assertEqual(self.pendopo.get_maks_kesehatan(), 1000)

    def test_setters(self):
        self.pendopo.set_tambah_uang(100)
        self.assertEqual(self.pendopo.get_uang(), 100)

        self.pendopo.set_tambah_skor(100)
        self.assertEqual(self.pendopo.get_skor(), 100)

        self.pendopo.set_kurang_kesehatan(200)
        self.assertEqual(self.pendopo.get_kesehatan(), 800)

        self.pendopo.set_maks_kesehatan(1500)
        self.assertEqual(self.pendopo.get_maks_kesehatan(), 1500)

    def test_perbaiki(self):
        self.pendopo.set_kurang_kesehatan(500)
        self.pendopo.set_tambah_uang(1000)
        self.pendopo.perbaiki()
        self.assertEqual(self.pendopo.get_kesehatan(), 1000)

    def test_pertahanan(self):
        self.pendopo.set_tambah_uang(500)
        self.pendopo.pertahanan()
        self.assertEqual(self.pendopo.get_maks_kesehatan(), 1250)

if __name__ == "__main__":
    unittest.main()
