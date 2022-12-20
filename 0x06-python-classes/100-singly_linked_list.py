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
        return self.next_node

    @next_node.setter
    def data(self, node):
        if ((type(node) is Node or Node is None) is False):
            raise TypeError("next_node must be a Node object")
        self.__data = node

    def __lt__(self, other):
        return self.__data < other.data


class SinglyLinkedList:

    def __init__(self, head=None):
        self.__head = head

    def sorted_insert(self, value):
        sorted_list = []
        temp = self.__head
        while (temp.next_node is not None):
            sorted_list.append(temp)
            temp = temp.next_node
        sorted_list.append(Node(value, None))
        
        sorted_list = sorted(sorted_list)

    
        temp = self.__head
        for i in sorted_list:
            temp = i
            temp = temp.next
        return self.__head
    
    def print(self):
        while(self.__head is None):
            print(self.__head.data)
            self.__head = self.__head.new_node




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
