import unittest
import pygame
from button import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.btn_image = pygame.Surface((100, 50))  # Gambar tombol
        self.button = Button(200, 200, self.btn_image, 1.0)

    def tearDown(self):
        pygame.quit()

    def test_button_init(self):
        self.assertEqual(self.button.rect.topleft, (200, 200))
        self.assertFalse(self.button.clicked)

    def test_button_draw(self):
        self.assertFalse(self.button.draw(self.screen))

    def test_button_click(self):
        # Simulasi klik mouse di atas tombol
        self.button.rect.topleft = (100, 100)
        pygame.mouse.set_pos((100, 100))


if __name__ == '__main__':
    unittest.main()
