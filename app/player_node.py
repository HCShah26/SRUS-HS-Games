from app.player import Player


class PlayerNode:
    """
    Represents a player node in double linked list.

    Attributes:
        player (Player): Contains the player object.
        next (PlayerNode): Reference to the next player node in the list.
        prev (PlayerNode): Reference to the previous player node in the list.
    """

    def __init__(self, player: Player = None):
        """
        Initializes the player node.

        Args:
             player (Player, optional): The player object to be stored in the node.
                Defaults to None.
        """
        self._player = player
        self._next_player = None
        self._prev_player = None

    @property
    def player(self) -> Player:
        """
        Gets the player object of the player node.

        Returns:
            Player object of the player node.
        """
        return self._player

    @player.setter
    def player(self, value: Player):
        """
        Sets the player object of the player node.

        Args: value (Player): The player object to set.
        """
        self._player = value

    @property
    def next(self) -> 'PlayerNode':
        """
        Gets the reference for the next player node in the list.

        Returns:
            PlayerNode: The next player node in the list.
        """
        return self._next_player

    @next.setter
    def next(self, value: 'PlayerNode'):
        """
        Sets the reference for the next player node in the list.

        Args: value (PlayerNode): The next player node to set.
        """
        self._next_player = value

    @property
    def prev(self) -> 'PlayerNode':
        """
        Gets the reference for the previous player node in the list.

        Returns:
            PlayerNode: The previous player node in the list.
        """
        return self._prev_player

    @prev.setter
    def prev(self, value: 'PlayerNode'):
        """
        Sets the reference for the previous player node in the list.

       Args: value (PlayerNode): The previous player node to set.
        """
        self._prev_player = value

    @property
    def key(self) -> str:
        """
        Gets the key of the player node in the list

        Returns:
            str: The unique ID (key) of player.
        """
        return self._player.uid

    def __str__(self) -> str:
        """
        Returns a string representation of the player node

        Returns:
            str: Formatted Player node
        """
        return f"PlayerNode(Key: {self.key}, Player: {self._player}, Next Player: {self._next_player}, Prev Player: {self._prev_player})"
