import unittest
import pygame
from game import Pendopo, Menu, Button

class TestGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_image = pygame.Surface((800, 600))  # Gambar latar belakang
        self.btn_image = pygame.Surface((100, 50))  # Gambar tombol
        self.menu = Menu(800, 600, self.bg_image, self.btn_image, "Arial")
        self.pendopo = Pendopo(pygame.Surface((100, 100)), pygame.Surface((50, 50)), 
                                pygame.Surface((25, 25)), self.bg_image, 100, 100, 1.0)
        self.button = Button(200, 200, self.btn_image, 1.0)

    def tearDown(self):
        pygame.quit()

    def test_menu_init(self):
        self.assertEqual(self.menu.width, 800)
        self.assertEqual(self.menu.height, 600)
        self.assertEqual(self.menu.bg_img, self.bg_image)
        self.assertEqual(self.menu.btn_img, self.btn_image)
        self.assertEqual(self.menu.font, "Arial")

    def test_pendopo_init(self):
        self.assertEqual(self.pendopo.get_kesehatan(), 1000)
        self.assertEqual(self.pendopo.get_maks_kesehatan(), 1000)
        self.assertEqual(self.pendopo.get_uang(), 0)
        self.assertEqual(self.pendopo.get_skor(), 0)

    def test_button_init(self):
        self.assertEqual(self.button.rect.topleft, (200, 200))
        self.assertFalse(self.button.clicked)

    def test_button_draw(self):
        self.assertFalse(self.button.draw(self.screen))

    def test_pendopo_render(self):
        self.assertIsNone(self.pendopo.render())

    def test_pendopo_perbaiki(self):
        self.pendopo.set_uang(1000)
        self.pendopo.set_kesehatan(500)
        self.pendopo.perbaiki()
        self.assertEqual(self.pendopo.get_uang(), 0)
        self.assertEqual(self.pendopo.get_kesehatan(), 1000)

    def test_pendopo_pertahanan(self):
        self.pendopo.set_uang(500)
        self.pendopo.pertahanan()
        self.assertEqual(self.pendopo.get_uang(), 0)
        self.assertEqual(self.pendopo.get_maks_kesehatan(), 1250)

if __name__ == '__main__':
    unittest.main()
