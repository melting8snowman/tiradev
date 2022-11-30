import unittest
import pygame
from settings import Settings


class TestSettings(unittest.TestCase):
    #def setUp(self):
    #    self.settings = Settings

    def test_created_settings_exists(self):
        self.settings = Settings(6,7,4,100, "HUMAN")
        self.assertNotEqual(self.settings, None)
    
    def test_created_settings_exists_opponent_human(self):
        self.settings2 = Settings(6,7,4,100, "HUMAN")
        self.assertEqual(self.settings2.opponent, 2)
        
    def test_created_settings_exists_opponent_ai(self):
        self.settings3 = Settings(6,7,4,100, "AI")
        self.assertEqual(self.settings3.opponent, 3)
    
   