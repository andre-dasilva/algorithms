from algorithms.stacks.deque import Deque, Node


def test_initialization():
    deque = Deque()
    assert deque.size == 0


def test_add_first():
    deque = Deque()
    node = Node("test 1")

    deque.add_first(node)

    assert deque.first() == node


def test_add_last():
    deque = Deque()
    node = Node("test 1")

    deque.add_last(node)

    assert deque.last() == node


def test_add_multiple():
    deque = Deque()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    deque.add_first(node1)
    deque.add_last(node3)
    deque.add_last(node2)

    assert deque.first() == node1
    assert deque.last() == node2


def test_remove_first():
    deque = Deque()
    node = Node("test 1")

    deque.add_first(node)
    deque.remove_first()

    assert deque.first() is None
    assert deque.last() is None


def test_remove_last():
    deque = Deque()
    node = Node("test 1")

    deque.add_last(node)
    deque.remove_last()

    assert deque.last() is None
    assert deque.first() is None


def test_remove_mutliple():
    deque = Deque()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    deque.add_first(node1)
    deque.add_last(node3)
    deque.add_last(node2)

    deque.remove_last()
    deque.remove_first()

    assert deque.first() == node3
    assert deque.last() == node3
