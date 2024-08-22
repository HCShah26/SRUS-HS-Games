import unittest
from logging import debug

from app.player import Player
from app.player_list import PlayerList


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        """ Set up the Player List before each test. """
        self.PlayerList = PlayerList()

    def test_initial_setup(self):
        """ Test for empty condition """
        self.assertEqual(len(self.PlayerList), 0)
        self.assertTrue(self.PlayerList.is_empty())

    def test_insert_new_player(self):
        """ Test for a single insert of Player to PlayerList """
        player: Player = Player("123456", "Hiten")

        self.PlayerList = PlayerList()
        self.PlayerList.insert_at_head(player)

        self.assertFalse(self.PlayerList.is_empty())
        self.assertEqual(self.PlayerList._head.key, player.uid)
        self.assertEqual(self.PlayerList._head.next, None)
        self.assertEqual(self.PlayerList._head.prev, None)
        self.assertEqual(len(self.PlayerList),1)

    def test_insert_three_players_at_head(self):
        """
        Testing multiple inserts of Player to the top of Player List

        Check that list order is correct and the nodes are set correctly
        """
        player1: Player = Player("123456", "Hiten")
        player2: Player = Player("123789", "Shah")
        player3: Player = Player("135796", "Test")

        self.PlayerList = PlayerList()
        self.PlayerList.insert_at_head(player1)
        self.PlayerList.insert_at_head(player2)
        self.PlayerList.insert_at_head(player3)

        self.assertEqual(self.PlayerList._head.key, player3.uid)
        self.assertEqual(self.PlayerList._head.next.key , player2.uid)
        self.assertEqual(self.PlayerList._head.prev, None)
        self.assertEqual(self.PlayerList._tail.next, None)
        self.assertEqual(len(self.PlayerList), 3)

    def test_insert_three_players_at_tail(self):
        """
        Testing multiple inserts of Player to the bottom of Player List

        Checking that list order is correct and the nodes are set correctly
        """
        player1: Player = Player("123456", "Hiten")
        player2: Player = Player("123789", "Shah")
        player3: Player = Player("135796", "Test")

        self.PlayerList = PlayerList()
        self.PlayerList.insert_at_tail(player1)
        self.PlayerList.insert_at_tail(player2)
        self.PlayerList.insert_at_tail(player3)

        self.assertEqual(self.PlayerList._head.key, player1.uid)
        self.assertEqual(self.PlayerList._tail.key, player3.uid)
        self.assertEqual(self.PlayerList._head.next.key, player2.uid)
        self.assertEqual(self.PlayerList._head.prev, None)
        self.assertEqual(self.PlayerList._tail.next, None)
        self.assertEqual(len(self.PlayerList), 3)

    def test_delete_from_head(self):
        """
        Testing the deletion of Player from the top of Player List

        Check that the nodes are updated correctly after the deletion,
        and the length of list is also updated correctly
        """
        player1: Player = Player("123456", "Hiten")
        player2: Player = Player("123789", "Shah")
        player3: Player = Player("135796", "Test")
        self.PlayerList = PlayerList()
        self.PlayerList.insert_at_head(player1)
        self.PlayerList.insert_at_head(player2)
        self.PlayerList.insert_at_head(player3)
        self.PlayerList.delete_from_head()
        self.assertEqual(self.PlayerList._head.key, player2.uid)
        self.assertEqual(self.PlayerList._tail.key, player1.uid)
        self.assertEqual(len(self.PlayerList), 2)

    def test_delete_from_tail(self):
        """
        Testing the deletion of Player from the bottom of Player List

        Check that the nodes are updated correctly after the deletion,
        and the length of list is also updated correctly
        """
        player1: Player = Player("123456", "Hiten")
        player2: Player = Player("123789", "Shah")
        player3: Player = Player("135796", "Test")
        self.PlayerList = PlayerList()
        self.PlayerList.insert_at_head(player1)
        self.PlayerList.insert_at_head(player2)
        self.PlayerList.insert_at_head(player3)
        self.PlayerList.delete_from_tail()
        self.assertEqual(self.PlayerList._head.key, player3.uid)
        self.assertEqual(self.PlayerList._tail.key, player2.uid)
        self.assertEqual(len(self.PlayerList), 2)

    def test_iter(self):
        """
        Testing the iteration behaviour of the Player List

        Checking that the order of the PlayerNodes in the list is correct when traversing forward
        """
        player1: Player = Player("123456", "Hiten")
        player2: Player = Player("123789", "Shah")
        player3: Player = Player("135796", "Test")
        self.PlayerList = PlayerList()
        self.PlayerList.insert_at_head(player1)
        self.PlayerList.insert_at_head(player2)
        self.PlayerList.insert_at_head(player3)
        nodes = []
        for node in self.PlayerList:
            nodes.append(node)
        data = [node.player.uid for node in nodes]
        self.assertEqual(data, ["135796", "123789", "123456"])

    def test_reverse(self):
        """
        Testing the reverse behaviour of the Player List

        Checking that the order of the PlayerNodes in the list is correct when traversing in the reverse
        """
        player1: Player = Player("123456", "Hiten")
        player2: Player = Player("123789", "Shah")
        player3: Player = Player("135796", "Test")
        self.PlayerList = PlayerList()
        self.PlayerList.insert_at_head(player1)
        self.PlayerList.insert_at_head(player2)
        self.PlayerList.insert_at_head(player3)
        nodes = []
        for node in reversed(self.PlayerList):
            nodes.append(node)
        data = [node.player.uid for node in nodes]
        self.assertEqual(data, ["123456", "123789", "135796"])

