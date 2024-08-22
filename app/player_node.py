from app.player import Player


class PlayerNode:
    """

    """
    def __init__(self, player: Player):
        self._player = player
        self._nextplayer = None
        self._prevplayer = None

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, value: Player):
        self._player = value

    @property
    def next(self) -> 'PlayerNode':
        return self._nextplayer

    @next.setter
    def next(self, value: 'PlayerNode'):
        self._nextplayer = value

    @property
    def prev(self) -> 'PlayerNode':
        return self._prevplayer

    @prev.setter
    def prev(self, value: 'PlayerNode'):
        self._prevplayer = value

    @property
    def key(self) -> str:
        return self._player.uid

    def __str__(self) -> str:
        return f"PlayerNode(Key: {self.key}, Player: {self._player})"
