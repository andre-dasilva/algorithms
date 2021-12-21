from __future__ import annotations
from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional[Node] = None

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    def append(self, node: Node) -> SinglyLinkedList:
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

        return self

    def remove(self, node: Node) -> None:
        curr = self.head
        prev = None

        while curr is not None and curr != node:
            prev = curr
            curr = curr.next

        if prev is None:
            self.head = curr.next
        elif curr.next is None:
            self.tail = prev
        elif curr:
            prev.next = curr.next
            self.size -= 1

        print(prev, curr)


    def first(self) -> Optional[Node]:
        return self.head

    def last(self) -> Optional[Node]:
        return self.tail

    def search(self, data: Any) -> Optional[Node]:
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def is_empty(self) -> bool:
        return self.size == 0
