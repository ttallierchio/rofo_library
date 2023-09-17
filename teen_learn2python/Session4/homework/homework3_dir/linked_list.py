# required code
from __future__ import annotations
from typing import Optional, List


class Node:
    value: int
    next: Self | None

    def __init__(self, value: int):
        self.value = value


class LinkedList:
    _node_root: Node
    _last_node: Node | None

    def __init__(self, node_root_value: List[int]):
        if node_root_value:
            if len(node_root_value) == 1:
                self._node_root = Node(node_root_value[0])
            else:
                self._node_root = Node(node_root_value[0])
                work_node = self._node_root
                for x in node_root_value[1:]:
                    work_node.next = Node(x)
                    work_node = work_node.next
                    self._last_node = work_node
                work_node.next = None  # need to make sure the attribute exists.

    def find_value(self, value_to_find: int) -> bool:
        node = self._node_root
        while node:
            if node.value == value_to_find:
                return True
            node = node.next
        return False
    
    def append(self,value):
        # get last node, and make a "next" one
        node = self._last_node
        node.next = Node(value)
        
        # get the next node, and make sure it terminates. assign last node to this node.
        node = node.next
        node.next = None
        self._last_node = node
        
    def print_nodes(self) -> None:
        node = self._node_root

        while node:
            print(node.value)
            node = node.next

    def __str__(self) -> str:
        node = self._node_root
        node_values = []

        while node:
            node_values.append(str(node.value))
            node = node.next

        return ",".join(node_values)
