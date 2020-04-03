from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.prev: Node = None
        self.next: Node = None

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        # Sentinels
        self.header: Node = Node(data=None)
        self.trailer: Node = Node(data=None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def first(self) -> Optional[Node]:
        if self.is_empty():
            return None
        return self.header.next

    def last(self) -> Optional[Node]:
        if self.is_empty():
            return None
        return self.trailer.prev

    def add_first(self, node):
        self.add_between(node, self.header, self.header.next)

    def add_last(self, node):
        self.add_between(node, self.trailer.prev, self.trailer)

    def add_between(self, new_node: Node, predecessor: Node, successor: Node):
        new_node.prev = predecessor
        new_node.next = successor
        predecessor.next = new_node
        successor.prev = new_node
        self.size += 1

    def remove_first(self) -> None:
        if self.is_empty():
            return None
        self.remove(self.header.next)

    def remove_last(self) -> None:
        if self.is_empty():
            return None
        self.remove(self.trailer.prev)

    def remove(self, node: Node) -> None:
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1

    def get(self, node: Node) -> Optional[Node]:
        curr = self.header
        while curr.next:
            if curr == node:
                return node
            curr = curr.next
        return None
