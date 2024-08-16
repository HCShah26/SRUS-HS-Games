from app.player_node import PlayerNode
class PlayerList:

    def __init__(self):
        self._head = None

    def is_empty(self) -> bool:
        """
        Checks if the first node is null in the PlayerList, returns true if it is empty, false otherwise
        :return:
        """
        return self._head is None

    def insert_node(self, player_node: PlayerNode):
        if self.is_empty():
            self._head = player_node
        else:
            player_node.next_node = self._head
            self._head = player_node
