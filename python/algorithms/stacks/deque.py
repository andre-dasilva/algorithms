from typing import Any

from algorithms.lists.doubly_linked_list import DoublyLinkedList


class Node:
    def __init__(self, data: Any):
        self.data = data


# Adapter pattern -> Deque with DoublyLinkedList
class Deque:
    def __init__(self, max_size=None):
        self.deque: DoublyLinkedList = DoublyLinkedList()

    @property
    def size(self):
        return self.deque.size

    def is_empty(self) -> bool:
        return self.deque.is_empty()

    def first(self) -> Node:
        return self.deque.first()

    def last(self) -> Node:
        return self.deque.last()

    def add_first(self, node: Node) -> None:
        self.deque.add_first(node)

    def add_last(self, node: Node) -> None:
        self.deque.add_last(node)

    def remove_first(self) -> None:
        self.deque.remove_first()

    def remove_last(self) -> None:
        self.deque.remove_last()
