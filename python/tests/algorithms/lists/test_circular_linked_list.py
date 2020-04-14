from algorithms.lists.circular_linked_list import CircularLinkedList, Node


def test_initialization():
    clinked_list = CircularLinkedList()
    assert clinked_list.size == 0
    assert clinked_list.tail is None


def test_add_first():
    clinked_list = CircularLinkedList()
    node = Node("test 1")

    clinked_list.add_first(node)
    assert clinked_list.size == 1
    assert clinked_list.last() == node
    assert clinked_list.first() == node


def test_add_last():
    clinked_list = CircularLinkedList()
    node = Node("test 1")

    clinked_list.add_last(node)
    assert clinked_list.size == 1
    assert clinked_list.last() == node
    assert clinked_list.first() == node


def test_add_multiple():
    clinked_list = CircularLinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")
    node4 = Node("test 4")

    clinked_list.add_first(node1)
    clinked_list.add_last(node2)
    clinked_list.add_last(node3)
    clinked_list.add_last(node4)

    assert clinked_list.size == 4
    assert clinked_list.last() == node4
    assert clinked_list.first() == node1


def test_rotate():
    clinked_list = CircularLinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")
    node4 = Node("test 4")

    clinked_list.add_first(node1)
    clinked_list.add_last(node2)
    clinked_list.add_last(node3)
    clinked_list.add_last(node4)

    clinked_list.rotate()

    assert clinked_list.size == 4
    assert clinked_list.last() == node1
    assert clinked_list.first() == node2


def test_remove():
    clinked_list = CircularLinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")
    node4 = Node("test 4")

    clinked_list.add_first(node1)
    clinked_list.add_last(node2)
    clinked_list.add_last(node3)
    clinked_list.add_last(node4)

    clinked_list.remove_first()

    assert clinked_list.size == 3
    assert clinked_list.last() == node4
    assert clinked_list.first() == node2
