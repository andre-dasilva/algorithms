from typing import Any, List


class Node:
    def __init__(self, data: Any):
        self.data = data


class Stack:
    def __init__(self):
        self.stack: List[Node] = []
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, node: Node) -> None:
        self.stack.append(node)
        self.size += 1

    def top(self) -> Node:
        if self.is_empty():
            return None
        return self.stack[self.size - 1]

    def pop(self) -> Node:
        if self.is_empty():
            return None
        node = self.stack.pop()
        self.size -= 1
        return node
