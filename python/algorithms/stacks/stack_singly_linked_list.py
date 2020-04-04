from typing import Any, List

from algorithms.lists.singly_linked_list_tail import SinglyLinkedListTail


class Node:
    def __init__(self, data: Any):
        self.data = data


# Adapter pattern -> Stack with SinglyLinkedListTail instead of list
class Stack:
    def __init__(self):
        self.stack: SinglyLinkedListTail = SinglyLinkedListTail()

    @property
    def size(self):
        return self.stack.size

    def is_empty(self) -> bool:
        return self.stack.is_empty()

    def push(self, node: Node) -> None:
        self.stack.add_first(node)

    def top(self) -> Node:
        return self.stack.first()

    def pop(self) -> Node:
        return self.stack.remove_first()
