#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (type(value) is not int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        if ((type(node) is Node or Node is None) is False):
            raise TypeError("next_node must be a Node object")
        self.__next_node = node

    def __lt__(self, other):
        return self.__data < other.data


class SinglyLinkedList:
    """Single linked list class
    """

    def __init__(self, head=None):
        """init the class

        Args:
            head (Node, optional): head Node for list. Defaults to None.
        """
        self.__head = None

    def __str__(self):
        """string representation of list

        Returns:
            str: Linked list elements
        """
        temp = self.__head
        sll_str = ""
        if self.__head is not None:
            while temp is not None:
                sll_str += str(temp.data) + "\n"
                temp = temp.next_node
        return sll_str[:-1]

    def sorted_insert(self, value):
        """Adds elements to list in sorted order

        Args:
            value (int): Data to add to list
        """
        if (self.__head is None or self.__head.data >= value):
            self.__head = Node(value, self.__head)
        else:
            temp = self.__head
            if (value < self.__head.data):
                self.__head = Node(value, temp)
                return
            else:
                while (temp.next_node is not None):
                    if (temp.next_node.data < value):
                        temp = temp.next_node
                    else:
                        break
                temp.next_node = Node(value, temp.next_node)
