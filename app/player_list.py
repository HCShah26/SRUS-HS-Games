from http.cookiejar import debug

from app.player import Player
from app.player_node import PlayerNode


class PlayerList:

    def __init__(self):
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
        _newplayer: PlayerNode = PlayerNode(player)

        if self.is_empty():
            """" Empty list -> we set the both the head and tail nodes """
            self._head = _newplayer
            self._tail = _newplayer
        else:
            """" Adding new node to the head of the list"""
            _newplayer.next = self._head
            self._head.prev = _newplayer
            self._head = _newplayer
        self._size += 1

    def insert_at_tail(self, player: Player):
        _newplayer: PlayerNode = PlayerNode(player)
        if self.is_empty():
            """" Empty list -> we set the both the head and tail nodes """
            self._tail = _newplayer
            self._head = _newplayer
        else:
            """" Adding new node to the tail of the list"""
            _newplayer.prev = self._tail
            self._tail.next = _newplayer
            self._tail = _newplayer
        self._size += 1


    def delete_from_head(self):
        if self.is_empty():
            """" Empty list -> Raise exception """
            raise Exception("Cannot delete from an empty list")
        else:
            self._head = self._head.next
            if self._head:
                """ Head node exist, set the prev of the head node to None"""
                self._head.prev = None
                self._size -= 1

    def delete_from_tail(self):
        if self.is_empty():
            """" Empty list -> Raise exception """
            raise Exception("Cannot delete from an empty list")
        else:
            self._tail = self._tail.prev
            if self._tail:
                """ Tail node exist, set the prev of the head node to None"""
                self._tail.next = None
                self._size -= 1

    def __iter__(self):
        current = self._head
        while current:
            yield current.key
            current = current.next

    def __reversed__(self):
        current = self._tail
        while current:
            yield current.key
            current = current.prev

    def __len__(self):
        return self._size
