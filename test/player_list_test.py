import unittest
from logging import debug

from app.player import Player
from app.player_node import PlayerNode
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
        searchedPlayerNode: PlayerNode = self.PlayerList.search_by_key("123789")

        self.assertEqual(self.PlayerList._head.key, player1.uid)
        self.assertEqual(self.PlayerList._tail.key, player3.uid)
        self.assertEqual(self.PlayerList._head.next.key, player2.uid)
        self.assertEqual(self.PlayerList._head.prev, None)
        self.assertEqual(self.PlayerList._tail.next, None)
        self.assertEqual(len(self.PlayerList), 3)
        self.assertEqual(searchedPlayerNode.player.uid, "123789")

    def test_find_player_node(self):
        """
        Testing find player node

        Checking that the correct player node is returned from the search method
        Three different calls are made for searching
        1) Search by key
        2) Search by name
        3) Find player node by Player and selecting the search be key or name
        """

        player1: Player = Player("123456", "Hiten")
        player2: Player = Player("123789", "Shah")
        player3: Player = Player("135796", "Test")

        self.PlayerList = PlayerList()
        self.PlayerList.insert_at_tail(player1)
        self.PlayerList.insert_at_tail(player2)
        self.PlayerList.insert_at_tail(player3)

        searched_by_key: PlayerNode = self.PlayerList.search_by_key("123789")
        searched_by_name: PlayerNode = self.PlayerList.search_by_name("Hiten")
        searched_by_find_key: PlayerNode = self.PlayerList.find(player2, True)
        searched_by_find_name: PlayerNode = self.PlayerList.find(player3, False)

        self.assertEqual(searched_by_key.player.uid, "123789")
        self.assertEqual(searched_by_name.player.name, "Hiten")
        self.assertEqual(searched_by_find_key.player, player2)
        self.assertEqual(searched_by_find_name.player, player3)


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

    def test_delete_by_key(self):
        """
        Testing the deletion of Player from the top of Player List

        Check that the nodes are updated correctly after the deletion,
        and the length of list is also updated correctly
        """
        player1: Player = Player("123456", "Hiten")
        player2: Player = Player("123789", "Dylan")
        player3: Player = Player("135796", "Brett")
        player4: Player = Player("185462", "Sam")

        self.PlayerList = PlayerList()
        self.PlayerList.insert_at_head(player1)
        self.PlayerList.insert_at_head(player2)
        self.PlayerList.insert_at_head(player3)
        self.PlayerList.insert_at_head(player4)

        # Check that we have 4 nodes in the list
        self.assertEqual(len(self.PlayerList), 4)

        # Test any node to delete - that is not a Head or Tail
        self.PlayerList.delete_by_key("123789")
        self.assertEqual(len(self.PlayerList), 3)

        # Test Head Node Delete
        self.PlayerList.delete_by_key("185462")
        self.assertEqual(len(self.PlayerList), 2)

        # Test Tail Node Delete
        self.PlayerList.delete_by_key("123456")
        self.assertEqual(len(self.PlayerList), 1)

        # Test delete only node on the list
        self.PlayerList.delete_by_key("135796")
        self.assertEqual(len(self.PlayerList), 0)




