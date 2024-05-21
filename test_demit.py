import unittest
import pygame
from demit import Demit

class TestDemit(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.demit = Demit(75, "jalan", -100, 490, 5)
    
    def test_getters(self):
        self.assertEqual(self.demit.get_darah(), 75)
        self.assertEqual(self.demit.get_kecepatan(), 5)
    
    def test_setters(self):
        self.demit.set_kurang_darah(25)
        self.assertEqual(self.demit.get_darah(), 50)

if __name__ == "__main__":
    unittest.main()