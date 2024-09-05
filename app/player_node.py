from app.player import Player


class PlayerNode:
    """
    Represents a player node in double linked list.

    Attributes:
        player: Contains the player object
        next player: Reference to the next player node in the list
        prev player: Reference to the previous player node in the list
    """

    def __init__(self, player: Player = None):
        """
        Initializes the player node

        :param player: The player object to be stored in the node
                Default: Null value
        """
        self._player = player
        self._next_player = None
        self._prev_player = None

    @property
    def player(self) -> Player:
        """
        Gets the player object of the player node

        :return:
            Player object of the player node
        """
        return self._player

    @player.setter
    def player(self, value: Player):
        """
        Sets the player object of the player node

        :param value:
        """
        self._player = value

    @property
    def next(self) -> 'PlayerNode':
        """
        Gets the reference for the next player node in the list

        :return:
            The next player node in the list
        """
        return self._next_player

    @next.setter
    def next(self, value: 'PlayerNode'):
        """
        Sets the reference for the next player node in the list

        :param value:
        """
        self._next_player = value

    @property
    def prev(self) -> 'PlayerNode':
        """
        Gets the reference for the previous player node in the list

        :return:
            The previous player node in the list
        """
        return self._prev_player

    @prev.setter
    def prev(self, value: 'PlayerNode'):
        """
        Sets the reference for the previous player node in the list

\       :param value:
        """
        self._prev_player = value

    @property
    def key(self) -> str:
        """
        Gets the key of the player node in the list

        :return:
            The key (Unique ID of Player) of the player node in the list
        """
        return self._player.uid

    def __str__(self) -> str:
        """
        Prints the player node

        :return:
            str: Formatted Player node
        """
        return f"PlayerNode(Key: {self.key}, Player: {self._player}, Next Player: {self._next_player}, Prev Player: {self._prev_player})"
