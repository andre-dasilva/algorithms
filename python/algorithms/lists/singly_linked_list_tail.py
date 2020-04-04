from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Node = None

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedListTail:
    def __init__(self, head: Node = None):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def first(self) -> Optional[Node]:
        if self.is_empty():
            return None
        return self.head

    def last(self) -> Optional[Node]:
        if self.is_empty():
            return None
        return self.tail

    def add_first(self, node: Node) -> None:
        node.next = self.head
        self.head = node

        if self.is_empty():
            self.tail = self.head
        self.size += 1

    def add_last(self, node: Node) -> None:
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def remove_first(self) -> None:
        if self.is_empty():
            return None
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None

    def remove_last(self) -> None:
        if self.is_empty():
            return None

        prev = self.head
        curr = self.head.next
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        self.tail = prev
        self.size -= 1
