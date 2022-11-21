import unittest
from gameboard import gameboard

class Testgameboard(unittest.TestCase):
    def setUp(self):
        self.gameboard = gameboard()

    def test_luotu_gameboard_on_olemassa(self):
        self.assertNotEqual(self.gameboard, None)