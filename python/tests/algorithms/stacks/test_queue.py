import pytest

from algorithms.stacks.queue import Node, Queue


@pytest.fixture
def queue():
    return Queue()


def test_initialization(queue):
    assert queue.is_empty()
    assert queue.first() is None
    assert queue.dequeue() is None


def test_enqueue_one(queue):
    node = Node("test 1")

    queue.enqueue(node)

    assert queue.size == 1
    assert queue.first() == node


def test_enqueue_multiple(queue):
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    queue.enqueue(node1)
    queue.enqueue(node2)
    queue.enqueue(node3)

    assert queue.size == 3
    assert queue.first() == node1


def test_dequeue_one(queue):
    node = Node("test 1")

    queue.enqueue(node)
    queue.dequeue()

    assert queue.size == 0
    assert queue.first() is None


def test_pop_multiple(queue):
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    queue.enqueue(node1)
    queue.enqueue(node2)
    queue.enqueue(node3)

    queue.dequeue()
    queue.dequeue()

    assert queue.size == 1
    assert queue.first() == node3


def test_max_size_queue():
    queue = Queue(max_size=2)
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    queue.enqueue(node1)
    queue.enqueue(node2)

    with pytest.raises(ValueError):
        queue.enqueue(node3)
