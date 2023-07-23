from dataclasses import dataclass
from datetime import datetime,timedelta
@dataclass
class SnakeNode():
    x:int = 0
    y:int = 0
    next_node = None
    old_move_x = None
    old_move_y = None
    last_move = None
    dead = False
    def reset(self,):
        if self.next_node:
            self.next_node._delete()
        self.next_node = None
        self.x = 10
        self.y = 10
        self.dead = False
    def _delete(self,):
        if self.next_node:
            self.next_node._delete()
        del self
    def should_move(self)->bool:
            if self.last_move is None or datetime.now() >= self.last_move + timedelta(milliseconds=100):
                self.last_move = datetime.now()
                return True
            return False
    def move_tail(self,x,y):
        if self.next_node:
            self.next_node.move_tail(self.x,self.y)
        self.x = x
        self.y = y 
    def move(self,move_x,move_y):
        if self.next_node:
            self.next_node.move_tail(self.x,self.y)
        self.x += move_x
        self.y += move_y
        if self.x <=-1:
            self.x = 19
        if self.x >=20:
            self.x = 0
        if self.y <= -1:
            self.y  = 19
        if self.y >= 20:
            self.y = 0 
              
        node = self
        while node.next_node and not self.dead:
                node = node.next_node
                if self.x == node.x and self.y == node.y:
                    self.dead = True
        if self.dead:
            print("kaboom")
    def put_tail(self):
        prev = None
        node = self
        count = 0
        while node:
            prev = node
            node = node.next_node
            count += 1
        prev.next_node = SnakeNode(prev.x ,prev.y)

    