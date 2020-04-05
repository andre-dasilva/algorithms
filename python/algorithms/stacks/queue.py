from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data


class Queue:
    def __init__(self, max_size=None):
        self.queue: List[Node] = []
        self.size: int = 0
        if max_size is not None:
            self.max_size = max_size

    def is_empty(self) -> bool:
        return self.size == 0

    def enqueue(self, node: Node) -> None:
        if hasattr(self, "max_size"):
            if self.max_size == self.size:
                raise ValueError("Queue is full")

        self.queue.append(node)
        self.size += 1

    def first(self) -> Node:
        if self.is_empty():
            return None
        return self.queue[0]

    def dequeue(self) -> Node:
        if self.is_empty():
            return None
        node = self.queue.pop(0)
        self.size -= 1
        return node
