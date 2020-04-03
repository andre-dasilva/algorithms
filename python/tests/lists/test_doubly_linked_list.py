from algorithms.lists.doubly_linked_list import DoublyLinkedList, Node


def test_initialization():
    dlinked_list = DoublyLinkedList()
    assert dlinked_list.header.next == dlinked_list.trailer
    assert dlinked_list.trailer.prev == dlinked_list.header
    assert dlinked_list.size == 0


def test_add_first():
    dlinked_list = DoublyLinkedList()
    node = Node("test 1")

    dlinked_list.add_first(node)
    assert dlinked_list.first() == node


def test_add_last():
    dlinked_list = DoublyLinkedList()
    node = Node("test 1")

    dlinked_list.add_last(node)
    assert dlinked_list.last() == node


def test_add_multiple():
    dlinked_list = DoublyLinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    dlinked_list.add_first(node1)
    dlinked_list.add_last(node3)
    dlinked_list.add_between(node2, node1, node3)

    first = dlinked_list.first()
    last = dlinked_list.last()
    middle = dlinked_list.get(node2)
    assert first.next == node2
    assert last.prev == node2
    assert middle.prev == node1
    assert middle.next == node3
    assert dlinked_list.size == 3


def test_remove_first():
    dlinked_list = DoublyLinkedList()
    node = Node("test 1")

    dlinked_list.add_first(node)
    dlinked_list.remove_first()
    assert dlinked_list.first() == None


def test_remove_last():
    dlinked_list = DoublyLinkedList()
    node = Node("test 1")

    dlinked_list.add_last(node)
    dlinked_list.remove_last()
    assert dlinked_list.last() == None


def test_remove_mutliple():
    dlinked_list = DoublyLinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    dlinked_list.add_first(node1)
    dlinked_list.add_last(node3)
    dlinked_list.add_between(node2, node1, node3)

    dlinked_list.remove(node2)
    first = dlinked_list.first()
    last = dlinked_list.last()
    middle = dlinked_list.get(node2)
    assert first.next == last
    assert last.prev == first
    assert middle is None
    assert dlinked_list.size == 2
