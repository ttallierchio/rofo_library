from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class SnakeNode:
    x: int = 0
    y: int = 0
    next_node = None
    old_move_x = None
    old_move_y = None
    last_move = None
    dead = False

    def reset(
        self,
    ):
        """
        reset the snake head and start the game over
        """
        if self.next_node:
            self.next_node._delete()
        self.next_node = None
        self.x = 10
        self.y = 10
        self.dead = False

    def _delete(
        self,
    ):
        """
        utility to clean up the snakenode for a new game
        """
        if self.next_node:
            self.next_node._delete()
        del self

    def should_move(self) -> bool:
        """if the snake is ready to move after waiting a 100 milliseconds

        Returns:
            bool: should we update the snake position?
        """
        if self.last_move is None or datetime.now() >= self.last_move + timedelta(
            milliseconds=100
        ):
            self.last_move = datetime.now()
            return True
        return False

    def move_tail(self, x: int, y: int):
        """
            recursive function move the current coords to the next node,
            then update with the parent coords.

        Args:
            x (int): the x pos on the grid
            y (int): the y pos on the grid
        """
        if self.next_node:
            self.next_node.move_tail(self.x, self.y)
        self.x = x
        self.y = y

    def move(self, move_x:int, move_y:int):
        """
            move the snake head and start moving each tail node

        Args:
            move_x (int): adjust which way we are moving x
            move_y (int): adjust which way we are moving y
        """
        if self.next_node:
            self.next_node.move_tail(self.x, self.y)
        self.x += move_x
        self.y += move_y
        if self.x <= -1:
            self.x = 19
        if self.x >= 20:
            self.x = 0
        if self.y <= -1:
            self.y = 19
        if self.y >= 20:
            self.y = 0

        node = self
        while node.next_node and not self.dead:
            node = node.next_node
            if self.x == node.x and self.y == node.y:
                self.dead = True
        if self.dead:
            print("kaboom")

    def add_tail(self):
        """
        add a new tail node
        """
        prev = None
        node = self
        count = 0
        while node:
            prev = node
            node = node.next_node
            count += 1
        prev.next_node = SnakeNode(prev.x, prev.y)
