#!/usr/bin/python3
""" Define class for a singly-linked list. """


class Node:
    """ A class Node for a singly-linked list. """

    def __init__(self, data, next_node=None):
        """ Instantiate the node.

        Args:
            data (int): The data of the node.
            next_node (None): The next of the node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ class for singly-linked list """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new node into the correct sorted
        position in the list(increasing order).

        Args:
            value (Node): The new node to insert
        """
        new_Node = Node(value)
        if self.__head is None:
            new_Node.next_node = None
            self.__head = new_Node
        elif self.__head.data > value:
            new_Node.next_node = self.__head
            self.__head = new_Node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_Node.next_node = tmp.next_node
            tmp.next_node = new_Node

    def __str__(self):
        """function to print content of a Singly-linked list. """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
