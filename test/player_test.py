import unittest

from app.player import Player


class PlayerTest(unittest.TestCase):

    def test_uid(self):
        test_player = Player("123456", "Hiten")
        self.assertEqual(test_player.uid, "123456")

    def test_player_name(self):
        test_player = Player("123456", "Hiten")
        self.assertEqual(test_player.name, "Hiten")
