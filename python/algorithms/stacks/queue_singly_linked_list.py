from typing import Any

from algorithms.lists.singly_linked_list_tail import SinglyLinkedListTail


class Node:
    def __init__(self, data: Any):
        self.data = data


class Queue:
    def __init__(self, max_size=None):
        self.queue: SinglyLinkedListTail = SinglyLinkedListTail()

    @property
    def size(self):
        return self.queue.size

    def is_empty(self) -> bool:
        return self.queue.is_empty()

    def enqueue(self, node: Node) -> None:
        return self.queue.add_last(node)

    def first(self) -> Node:
        return self.queue.first()

    def dequeue(self) -> Node:
        return self.queue.remove_first()
