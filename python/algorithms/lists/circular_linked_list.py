from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Node = None

    def __repr__(self):
        return repr(self.data)


class CircularLinkedList:
    def __init__(self):
        self.tail: Node = None
        self.size: int = 0

    def is_empty(self) -> int:
        return self.size == 0

    def first(self) -> Optional[Node]:
        if self.is_empty():
            return None
        return self.tail.next

    def last(self) -> Optional[Node]:
        if self.is_empty():
            return None
        return self.tail

    def add_first(self, node: Node) -> None:
        if self.is_empty():
            self.tail = node
            self.tail.next = self.tail
        else:
            node.next = self.tail.next
            self.tail.next = node
        self.size += 1

    def add_last(self, node: Node) -> None:
        self.add_first(node)
        self.tail = self.tail.next

    def rotate(self) -> None:
        if self.tail is not None:
            self.tail = self.tail.next

    def remove_first(self) -> None:
        if self.is_empty():
            return None

        head = self.tail.next
        if head == self.tail:
            self.tail = None
        else:
            self.tail.next = head.next
        self.size -= 1
