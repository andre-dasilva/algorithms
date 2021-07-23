from dataclasses import dataclass
from typing import List, Tuple

import pytest
from algorithms.trees.binary_tree import (BinaryTree, Node, in_order_traversal,
                                          post_order_traversal,
                                          pre_order_traversal)


@dataclass
class BinaryTreeResult:
    pre_order: List[Node]
    post_order: List[Node]
    in_order: List[Node]
    root: Node


@pytest.fixture
def binary_search_tree() -> Tuple[List[Node], BinaryTree]:
    """
    Binary Tree:
         6
      4    8
    3  5  7  9
    """
    node6 = Node(data=6)
    node4 = Node(data=4)
    node3 = Node(data=3)
    node5 = Node(data=5)
    node8 = Node(data=8)
    node7 = Node(data=7)
    node9 = Node(data=9)

    node6.left = node4
    node6.right = node8

    node4.left = node3
    node4.right = node5

    node8.left = node7
    node8.right = node9

    return BinaryTreeResult(
        pre_order=[node6, node4, node3, node5, node8, node7, node9],
        post_order=[node3, node5, node4, node7, node9, node8, node6],
        in_order=[node3, node4, node5, node6, node7, node8, node9],
        root=node6
    )


def test_empty_tree():
    assert BinaryTree().root == None


def test_pre_order_traversal(binary_search_tree: BinaryTreeResult):
    assert pre_order_traversal(
        binary_search_tree.root) == binary_search_tree.pre_order


def test_post_order_traversal(binary_search_tree: BinaryTreeResult):
    assert post_order_traversal(
        binary_search_tree.root) == binary_search_tree.post_order


def test_in_order_traversal(binary_search_tree: BinaryTreeResult):
    assert in_order_traversal(
        binary_search_tree.root) == binary_search_tree.in_order
