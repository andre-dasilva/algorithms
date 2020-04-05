import pytest

from algorithms.stacks.stack import Node, Stack


@pytest.fixture
def stack():
    return Stack()


def test_initialization(stack):
    assert stack.size == 0
    assert stack.top() is None
    assert stack.pop() is None


def test_push_one(stack):
    node = Node("test 1")

    stack.push(node)
    assert stack.size == 1
    assert stack.top() == node


def test_push_multiple(stack):
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    stack.push(node1)
    stack.push(node2)
    stack.push(node3)

    assert stack.size == 3
    assert stack.top() == node3


def test_pop_one(stack):
    node = Node("test 1")

    stack.push(node)
    stack.pop()

    assert stack.size == 0
    assert stack.top() is None


def test_pop_multiple(stack):
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    stack.push(node1)
    stack.push(node2)
    stack.push(node3)

    stack.pop()
    stack.pop()

    assert stack.size == 1
    assert stack.top() == node1


def test_max_size_stack():
    stack = Stack(max_size=2)
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    stack.push(node1)
    stack.push(node2)

    with pytest.raises(ValueError):
        stack.push(node3)
