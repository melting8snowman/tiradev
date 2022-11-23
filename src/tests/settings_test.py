import unittest
import pygame
from settings import Settings


class TestSettings(unittest.TestCase):
    #def setUp(self):
    #    self.settings = Settings

    def test_created_settings_exists(self):
        self.settings = Settings(6,7,100)
        self.assertNotEqual(self.settings, None)
    
   