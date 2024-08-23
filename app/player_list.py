from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    """
    An implementation of double linked list to manage list of players
    """

    def __init__(self):
        """
        Initialise an empty PlayerList with no nodes
        :param
            _head: Keeps track of the first item in the PlayerNode
            _tail: Keeps track of the last item in the PlayerNode
            _size: counter to keep track of the number of nodes in this list.
                   (This makes the code more efficient when the list size gets bigger
                    as the length method does not need to iterate through the list to get its size.)
        """
        self._head: PlayerNode = None
        self._tail: PlayerNode = None
        self._size = 0

    def is_empty(self) -> bool:
        """
        Checks if the first node is null in the PlayerList, returns true if it is empty, false otherwise
        :return:
        """
        return self._size == 0

    def insert_at_head(self, player: Player):
        """
        Inserts a new node at the head of the list
        :param player: The player object is inserted into the list at the top
        """
        _newplayer: PlayerNode = PlayerNode(player)

        if self.is_empty():
            """ Empty list -> we set the both the head and tail nodes """
            self._head = _newplayer
            self._tail = _newplayer
        else:
            """ Adding new node to the head of the list"""
            _newplayer.next = self._head
            self._head.prev = _newplayer
            self._head = _newplayer
        self._size += 1  # increase size 1 on successful insertion of player into the list

    def insert_at_tail(self, player: Player):
        """
        Inserts a new node at the tail of the list
        :param playerNode: The player object is inserted into the list at the bottom
        """
        _newplayer: PlayerNode = PlayerNode(player)
        if self.is_empty():
            """ Empty list -> we set the both the head and tail nodes """
            self._tail = _newplayer
            self._head = _newplayer
        else:
            """ Adding new node to the tail of the list"""
            _newplayer.prev = self._tail
            self._tail.next = _newplayer
            self._tail = _newplayer
        self._size += 1  # increase size 1 on successful insertion of player into the list

    def delete_from_head(self):
        """
        Deletes the top most node (head node) from the list
        :param playerNode: The player object is deleted from the top of the list
        """
        if self.is_empty():
            """" Empty list -> Raise exception """
            raise Exception("Cannot delete from an empty list")
        else:
            self._head = self._head.next
            if self._head:
                """ Head node exist, set the prev of the head node to None"""
                self._head.prev = None
                self._size -= 1  # decrease size 1 on successful insertion of player into the list

    def delete_from_tail(self):
        """
        Deletes the bottom most node (tail node) from the list
        :param playerNode: The player object is deleted from the bottom of the list
        """
        if self.is_empty():
            """" Empty list -> Raise exception """
            raise Exception("Cannot delete from an empty list")
        else:
            self._tail = self._tail.prev
            if self._tail:
                """ Tail node exist, set the prev of the head node to None"""
                self._tail.next = None
                self._size -= 1  # decrease size 1 on successful insertion of player into the list

    def delete_by_key(self, key):
        _isDeleted: bool = False

        deletePlayer: PlayerNode = self.search_by_key(key)

        if deletePlayer:
            if deletePlayer == self._head:
                # Delete player node deletion at Head
                self._head = deletePlayer.next
                self._prev = None
                _isDeleted = True

            elif deletePlayer == self._tail:
                # Delete player node deletion at Tail
                self._tail = deletePlayer.prev
                self._tail.next = None
                _isDeleted = True

            else:
                # Delete player node somewhere in the middle of the list
                deletePlayer.next.prev = deletePlayer.prev
                deletePlayer.prev.next = deletePlayer.next
                deletePlayer.next = None
                deletePlayer.prev =None
                _isDeleted = True

        if _isDeleted:
            self._size -= 1

    def find(self, player: Player, searchByKey: bool ) -> PlayerNode:
        if searchByKey:
            return self.search_by_key(player.uid)
        else:
            return self.search_by_name(player.name)
    def search_by_key(self, key) -> PlayerNode:
        if self.is_empty():
            raise Exception("List is empty")

        current: PlayerNode = self._head

        while current:
            if current.key == key:
                return current
            else:
                current = current.next

    def search_by_name(self, playerName) -> PlayerNode:
        if self.is_empty():
            raise Exception("List is empty")

        current: PlayerNode = self._head

        while current:
            if current.player.name == playerName:
                return current
            else:
                current = current.next


    def __iter__(self):
        """
        Iterates over the Player Nodes forward from Head to Tail
        :return:
            key: The unique identifier of the node, ideally should return the whole node,
                 but for testing purposes
        """

        current = self._head
        while current:
            yield current
            current = current.next

    def __reversed__(self):
        """
        Iterates in reverse order over the Player Nodes from Tail to Head
        :return:
            PlayerNode
        """
        current = self._tail
        while current:
            yield current
            current = current.prev

    def __len__(self):
        """
        Returns the size of the list (No iterations required to return the length)
        :return:
            int: Integer value representing the size of the list
        """
        return self._size
