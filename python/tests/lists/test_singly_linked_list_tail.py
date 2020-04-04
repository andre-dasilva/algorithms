from algorithms.lists.singly_linked_list_tail import SinglyLinkedListTail, Node


def test_initialization():
    slinked_list = SinglyLinkedListTail()
    assert slinked_list.size == 0
    assert slinked_list.head is None
    assert slinked_list.tail is None


def test_add_first():
    slinked_list = SinglyLinkedListTail()
    node = Node("String as test data")

    slinked_list.add_first(node)

    assert slinked_list.first() == node
    assert slinked_list.last() == node
    assert slinked_list.size == 1


def test_add_last():
    slinked_list = SinglyLinkedListTail()
    node = Node("test 1")

    slinked_list.add_last(node)

    assert slinked_list.first() == node
    assert slinked_list.last() == node


def test_remove_first():
    slinked_list = SinglyLinkedListTail()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")

    slinked_list.add_last(node1)
    slinked_list.add_last(node2)
    slinked_list.add_last(node3)

    slinked_list.remove_first()

    assert slinked_list.first() == node2
    assert slinked_list.last() == node3


def test_remove_last():
    slinked_list = SinglyLinkedListTail()
    node1 = Node("test 1")
    node2 = Node("test 2")
    node3 = Node("test 3")
    node4 = Node("test 4")
    node5 = Node("test 5")

    slinked_list.add_last(node1)
    slinked_list.add_last(node2)
    slinked_list.add_last(node3)
    slinked_list.add_last(node4)
    slinked_list.add_last(node5)

    slinked_list.remove_last()

    assert slinked_list.first() == node1
    assert slinked_list.last() == node4
