#!/usr/bin/python3
"""
This is a singly linked list module.
"""


class Node:
    """This class defines the nodes.

    The node takes in two Attributes

    Atrributes:
    data: Data to set in a linked list
    next_node: linked node in a singly linked list

    Methods:
    Data: property to retrieve the data
    next_node: property to retrieve the next_node
    """

    def __init__(self, data=None, next_node=None):
        """This is a constructor method

        It initializes the class with data and next_node attributes

        Args:
            Value: Must be an integer
            Nodes: must be an objct.
        """
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
        self.__data = value

    @property
    def next_node(self):
        """Property to retrieve the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property to set the next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The class of singly linked list.

    Attribute:
        is_empty: Check if linked likst is empty
        append: Add new nodes to the end of the linked list
        sorted: Arrange position in ascending order in a linked list
        display: Display element of the linked list.

    Args:
        data: Integer in a list
        value: Element in the node

    """

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.__head is None

    def append(self, data):
        """Add new node with the given data to the end of the linked list."""
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
        else:
            current_node = self.__head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position
        in the linked list."""
        new_node = Node(value)
        if self.is_empty() or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None) and \
                    (current_node.next_node < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def display(self):
        """Display the element of the linked list."""
        current_node = self.__head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")

    def __str__(self):
        """Return a string representation of the linked list."""
        current_node = self.__head
        element = []
        while current_node is not None:
            element.append(str(current_node.data))
            current_node = current_node.next_node
        return " -> ".join(element) + " -> None"
