#!/usr/bin/python3
"""module for a singly linked list"""

class Node:
    """defines a node of a singly linked list by"""

    def __init__(self, data, next_node=None):
        """Initializing this node class """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets data attribute"""

        return self.__data

    @data.setter
    def data(self, value):
        """sets data attribute"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get next_node attribute"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
         """set value of next node"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """that defines a singly linked list """

    def __init__(self):
        """Initializing this Singlylinkedlist class """

        self.head = None

    def sorted_insert(self, value):
        """sort the inserted node"""

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """make list printable"""

        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
