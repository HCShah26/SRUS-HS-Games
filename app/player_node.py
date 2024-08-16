from app.player import Player


class PlayerNode:

    def __init__(self, player: Player):
        self._player = player
        self._nextNode = None
        self._prevNode = None

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, value: Player):
        self._player = value

    @property
    def next(self) -> 'PlayerNode':
        return self._nextNode

    @next.setter
    def next(self, value: 'PlayerNode'):
        self._nextNode = value

    @property
    def prev(self) -> 'PlayerNode':
        return self._prevNode

    @prev.setter
    def prev(self, value: 'PlayerNode'):
        self._prevNode = value

    @property
    def key(self) -> str:
        return self._player.uid

    def __str__(self) -> str:
        return f"PlayerNode(Key: {self.key}, Player: {self._player})"
