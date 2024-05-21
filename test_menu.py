import unittest
import pygame
from game import Menu, Button

class TestMenu(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_image = pygame.Surface((800, 600))  # Gambar latar belakang
        self.btn_image = pygame.Surface((100, 50))  # Gambar tombol
        self.menu = Menu(800, 600, self.bg_image, self.btn_image, "Arial")
        self.button = Button(200, 200, self.btn_image, 1.0)

    def tearDown(self):
        pygame.quit()

    def test_menu_init(self):
        self.assertEqual(self.menu.width, 800)
        self.assertEqual(self.menu.height, 600)
        self.assertEqual(self.menu.bg_img, self.bg_image)
        self.assertEqual(self.menu.btn_img, self.btn_image)
        self.assertEqual(self.menu.font, "Arial")

    def test_button_init(self):
        self.assertEqual(self.button.rect.topleft, (200, 200))
        self.assertFalse(self.button.clicked)

    def test_button_draw(self):
        self.assertFalse(self.button.draw(self.screen))

    def test_menu_play(self):
        self.assertEqual(self.menu.get_pilihan(1), 1)
        self.assertEqual(self.menu.get_pilihan(2), 2)
        self.assertEqual(self.menu.get_pilihan(3), 3)

if __name__ == '__main__':
    unittest.main()
