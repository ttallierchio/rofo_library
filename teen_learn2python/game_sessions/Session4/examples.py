#!/usr/bin/python3

# required code
from __future__ import annotations
from typing import Optional, List

# examples
import requests
from string import ascii_lowercase, ascii_uppercase, whitespace


class Node:
    value: int
    next: Self | None

    def __init__(self, value: int):
        self.value = value


class LinkedList:
    _node_root: Node

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
                work_node.next = None  # need to make sure the attribute exists.

    def print_nodes(self):
        node = self._node_root

        while node:
            print(node.value)
            node = node.next

    def __str__(self):
        node = self._node_root
        node_values = []

        while node:
            node_values.append(str(node.value))
            node = node.next

        return ",".join(node_values)


def example_function():
    return "do nothing"


def example_function_parameter(value: str):
    return f"do {value}"


def add(value_1: int, value_2: int):
    return value_1 + value_2


def power_to(value, power=2):
    # we square it if it does not have a power by default
    return value**power


if __name__ == "__main__":
    my_linked_list = LinkedList(range(1, 201))
    my_linked_list.print_nodes()

    print(my_linked_list)
    print(
        example_function(),
        example_function_parameter("something"),
        add(10, 10),
        power_to(2),
        power_to(2, 3),
    )
