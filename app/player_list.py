from app.player import Player
from app.player_node import PlayerNode
from typing import Optional


class PlayerList:
    """
        An implementation of double linked list to manage list of players

        Attributes:
            _head (PlayerNode): The first node in the PlayerList.
            _tail (PlayerNode): The last node in the PlayerList.
            _size (int): Keeps track of the number of nodes in the list.
    """

    def __init__(self):
        """
        Initialise an empty PlayerList with no nodes
        """
        self._head: PlayerNode = None
        self._tail: PlayerNode = None
        self._size = 0

    def is_empty(self) -> bool:
        """
        Checks if the PlayerList is empty.
    
        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self._size == 0

    def insert_at_head(self, player: Player):
        """
        Inserts a new player node at the head of the list.
    
        Args: player (Player): The player object is inserted into the list at the top.
        """
        new_player: PlayerNode = PlayerNode(player)

        if self.is_empty():
            # Empty list -> we set the both the head and tail nodes
            self._head = new_player
            self._tail = new_player
        else:
            # Adding new node to the head of the list
            new_player.next = self._head
            self._head.prev = new_player
            self._head = new_player

        self._size += 1  # increase size 1 on successful insertion of player into the list

    def insert_at_tail(self, player: Player):
        """
        Inserts a new player node at the tail of the list.
    
        Args: player (Player): The player object is inserted into the list at the bottom.
        """
        new_player: PlayerNode = PlayerNode(player)
        if self.is_empty():
            # Empty list -> we set the both the head and tail nodes
            self._tail = new_player
            self._head = new_player
        else:
            # Adding new node to the tail of the list
            new_player.prev = self._tail
            self._tail.next = new_player
            self._tail = new_player
        self._size += 1  # increase size 1 on successful insertion of player into the list

    def delete_from_head(self):
        """
        Deletes the top most node (head node) from the list
    
        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty():
            # Empty list -> Raise exception
            raise IndexError("Cannot delete from an empty list")
        else:
            self._head = self._head.next
            if self._head:
                # Head node exist, set the prev of the head node to None
                self._head.prev = None
                self._size -= 1  # decrease size 1 on successful insertion of player into the list

    def delete_from_tail(self):
        """
        Deletes the bottom most node (tail node) from the list.
    
        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty():
            # Empty list -> Raise exception
            raise IndexError("Cannot delete from an empty list")
        else:
            self._tail = self._tail.prev
            if self._tail:
                # Tail node exist, set the prev of the head node to None
                self._tail.next = None
                self._size -= 1  # decrease size 1 on successful insertion of player into the list

    def delete_by_key(self, key):
        """
        Delete a player node by its key.

        Args: key: The key of the node to be deleted.

        Raises:
            IndexError: If the list is empty.
            KeyError: If no node is found with the given key.
        """
        is_deleted: bool = False

        if self.is_empty():
            raise IndexError("Cannot delete from an empty list")

        deleted_player: PlayerNode = self.search_by_key(key)

        if not deleted_player:
            raise KeyError(f"Node with key {key} was not found")

        if deleted_player:
            if deleted_player == self._head:
                # Delete player node deletion at Head
                self._head = deleted_player.next
                self._head.prev = None
                is_deleted = True

            elif deleted_player == self._tail:
                # Delete player node deletion at Tail
                self._tail = deleted_player.prev
                self._tail.next = None
                is_deleted = True

            else:
                # Delete player node somewhere in the middle of the list
                deleted_player.next.prev = deleted_player.prev
                deleted_player.prev.next = deleted_player.next
                deleted_player.next = None
                deleted_player.prev = None
                is_deleted = True

        if is_deleted:
            self._size -= 1

    def find(self, player: Player, searchByKey: bool ) -> PlayerNode:
        """
        Finds a player node by key or name.
    
        Args:
            player (Player): The Player object used for searching.
            search_by_key (bool): True to search by key, False to search by name.

        Returns:
            PlayerNode: The found player node.
        """
        if search_by_key:
            return self.search_by_key(player.uid)
        else:
            return self.search_by_name(player.name)
        
    def search_by_key(self, key) -> Optional[PlayerNode]:
        """
        Searches for a player node by its key.

        Args:
            key: The key to search for player node.

        Returns:
            Optional[PlayerNode]: The found player node, or None if not found.
        """
        if self.is_empty():
            return None # Indicates no Players Nodes (Empty list)

        current: PlayerNode = self._head

        while current:
            if current.key == key:
                return current
            else:
                current = current.next

    def search_by_name(self, playerName) -> Optional[PlayerNode]:
        """
        Searches for a player node by player name.

        Args:
            player_name: The name of the player to search for.

        Returns:
            Optional[PlayerNode]: The found player node, or None if not found.
        """
        if self.is_empty():
            return None # Indicates no Players Nodes (Empty list)

        current: PlayerNode = self._head

        while current:
            if current.player.name == playerName:
                return current
            else:
                current = current.next


    def __iter__(self):
        """
        Iterates over the Player Nodes forward from Head to Tail

        :return: An iterator of Player Nodes
            key: The unique identifier of the node, ideally should return the whole node,
                 but for testing purposes
        """

        current = self._head
        while current:
            yield current
            current = current.next

    def __reversed__(self):
        """
        Iterates in reverse order over the Player Nodes from Tail to Head.

        Yields:
            PlayerNode: The previous player node in the list.
        """
        current = self._tail
        while current:
            yield current
            current = current.prev

    def __len__(self):
        """
        Returns the size of the list (No iterations required to return the length).

        Returns:
            int: Integer value representing the size of the list.
        """
        return self._size
