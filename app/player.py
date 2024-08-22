
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
        self._uid = unique_id
        self._player_name = player_name

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._player_name

    def __str__(self) -> str:
        return f"Player ID: {self._uid}, Name: {self._player_name}"
