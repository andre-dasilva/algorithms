from typing import Any, List, Optional


class Node:
    def __init__(self, left: Optional['Node'] = None,
                 right: Optional['Node'] = None,
                 data: Optional[Any] = None) -> None:
        self.left = left
        self.right = right
        self.data = data

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.data})'


class BinaryTree:
    def __init__(self, root: Optional['Node'] = None) -> None:
        self.root = root
        self.length = 1 if self.root else 0

    def has_root(self):
        if self.root is None:
            return True
        return False


def pre_order_traversal(node: Node, nodes: List[Node] = None):
    if nodes is None:
        nodes = []

    if node:
        nodes.append(node)
        pre_order_traversal(node.left, nodes)
        pre_order_traversal(node.right, nodes)
        return nodes


def post_order_traversal(node: Node, nodes: List[Node] = None):
    if nodes is None:
        nodes = []

    if node:
        post_order_traversal(node.left, nodes)
        post_order_traversal(node.right, nodes)
        nodes.append(node)
        return nodes


def in_order_traversal(node: Node, nodes: List[Node] = None):
    if nodes is None:
        nodes = []

    if node:
        in_order_traversal(node.left, nodes)
        nodes.append(node)
        in_order_traversal(node.right, nodes)
        return nodes
