
class Player:
    """
    A class representing a Player with two properties.

    Attributes:
        _uid (str): UniqueID of the player.
        _Player_name (str): Name of the player.

    This class has a initialise method to instantiate the Player object
    which takes two inputs unique_id and player_name
    and has two Get methods to return the data
    a) uid that returns string
    b) name that returns string
    """

    def __init__(self, unique_id: str, player_name: str) -> None:
        """
        Initialise the Player object.

        Args:
            unique_id: (str): The unique id of the player.
            player_name (str): The name of the player.
        """
        self._uid = unique_id
        self._player_name = player_name

    @property
    def uid(self) -> str:
        """
        Gets the Unique ID of the player.

        Returns:
            str: Unique ID of the player.
        """
        return self._uid

    @property
    def name(self) -> str:
        """
        Gets the Player Name.

        Returns:
            str: The player's name.
        """
        return self._player_name

    def __str__(self) -> str:
        """
        Returns a sting representation of the Player object

        Returns:
            str: A formatted string of the Player object
        """
        return f"Player ID: {self._uid}, Name: {self._player_name}"
