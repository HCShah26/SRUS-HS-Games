class Player:

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
