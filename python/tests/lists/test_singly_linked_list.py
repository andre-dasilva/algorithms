from algorithms.lists.singly_linked_list import LinkedList, Node


def test_initialization():
    slinked_list = LinkedList()
    assert slinked_list.size == 0
    assert slinked_list.head is None


def test_append_one():
    slinked_list = LinkedList()
    node = Node("String as test data")
    slinked_list.append(node)
    assert slinked_list.head == node


def test_append_multiple():
    slinked_list = LinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    slinked_list.append(node1).append(node2).append(node3)
    assert slinked_list.size == 3
    assert slinked_list.first() == node1
    assert slinked_list.last() == node3


def test_search_existing():
    slinked_list = LinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    slinked_list.append(node1).append(node2).append(node3)

    assert slinked_list.search("test 2") == node2


def test_search_not_existing():
    slinked_list = LinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    slinked_list.append(node1).append(node2).append(node3)

    assert slinked_list.search("test 4") is None


def test_remove_first():
    slinked_list = LinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    slinked_list.append(node1).append(node2).append(node3)
    slinked_list.remove(node1)
    assert slinked_list.first() == node2
    assert slinked_list.last() == node3


def test_remove_last():
    slinked_list = LinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    slinked_list.append(node1).append(node2).append(node3)
    slinked_list.remove(node3)
    assert slinked_list.first() == node1
    assert slinked_list.last() == node2


def test_remove_between():
    slinked_list = LinkedList()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")
    node4 = Node("test 4")
    node5 = Node("test 5")

    slinked_list.append(node1).append(node2).append(
        node3).append(node4).append(node5)
    slinked_list.remove(node3)
    assert slinked_list.first() == node1
    assert slinked_list.last() == node5
