
class Player:
    """
    Player class that has two properties
    1. UniqueID of type string
    2. Player Name of type string

    This class has a initialise method to instantiate the Player object
    which takes two inputs unique_id and player_name
    and has two Get methods to return the data
    a) uid that returns string
    b) name that returns string
    """

    def __init__(self, unique_id: str, player_name: str) -> None:
        """
        Initialise the Player object

        :param unique_id:
        :param player_name:
        """
        self._uid = unique_id
        self._player_name = player_name

    @property
    def uid(self) -> str:
        """
        Gets the Unique ID of Player

        :return:
            str: Unique IF of Player
        """
        return self._uid

    @property
    def name(self) -> str:
        """
        Gets the Player Name
        :return:
            str: Player name
        """
        return self._player_name

    def __str__(self) -> str:
        """
            Prints the Player object
        :return:
            str: A formatted string of the Player object
        """
        return f"Player ID: {self._uid}, Name: {self._player_name}"
