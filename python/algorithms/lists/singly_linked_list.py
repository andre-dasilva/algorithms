from __future__ import annotations
from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Node = None

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self, head: Node = None):
        self.head: Node = None
        self.size: int = 0

    def append(self, node: Node) -> SinglyLinkedList:
        self.size += 1
        if self.first() is None:
            self.head = node
            return self

        end = self.last()
        end.next = node
        return self

    def remove(self, node: Node) -> None:
        curr = self.head
        prev = None

        while curr is not None and curr != node:
            prev = curr
            curr = curr.next

        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
            self.size -= 1

    def first(self) -> Node:
        return self.head

    def last(self) -> Node:
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr

    def search(self, data: Any) -> Optional[Node]:
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def is_empty(self) -> bool:
        return self.size == 0
