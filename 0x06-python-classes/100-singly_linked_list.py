#!/usr/bin/python3
"""This is a singly linked list module."""


class Node:
    """This class defines the nodes."""

    def __init__(self, data=None, next_node=None):
        """This is a constructor method"""
        self.__data = None
        self.data = data
        self.__next_node = None
        self.next_node = next_node

    @property
    def data(self):
        """property to retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Property to set the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        return self.__data = value

    @property
    def next_node(self):
        """Property to retrieve the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property to set the next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        return self.__next_node = value


class Node:
    """Node class for singly linked list."""

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """The class of singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self._head = None

    def is_empty(self):
        """Check if the linked list is empty."""
        return self._head is None

    def append(self, data):
        """Add new node with the given data to the end of the linked list."""
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
        else:
            current_node = self._head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def sorted.insert(self, value):
        """Insert a new node into the correct sorted position
        in the linked list."""
        new_node = Node(value)
        if self.is_empty() or value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current_node = self._head
            while (current_node.next_node is not None) and
            (current_node.next_node < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def display(self):
        """Display the element of the linked list."""
        current_node = self._head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("Node")


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
